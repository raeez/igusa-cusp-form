#!/usr/bin/env python3
"""
build_architecture.py -- extract the mathematical architecture of the manuscript.

Walks main.tex's \\input{} closure, scans every theorem-like block
(theorem, lemma, proposition, corollary, definition, conjecture,
computation, example, remark, fact, principle, observation, claim,
question, problem), records label / status / chapter location / line /
statement excerpt, and the cross-references inside the body.

Outputs:
  out/architecture.json  -- {meta, nodes, edges} graph data
  out/architecture.html  -- self-contained interactive viewer
                            (cytoscape.js + KaTeX from CDN)

Run from the repo root:
  python3 scripts/build_architecture.py [--root .] [--main main.tex]
                                        [--out out] [--volume vol1]

Stdlib-only.  No install.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

THEOREM_ENVS = (
    "theorem", "thm",
    "lemma", "lem",
    "proposition", "prop",
    "corollary", "cor",
    "definition", "defn", "def",
    "conjecture", "conj",
    "computation", "comp",
    "example", "ex",
    "remark", "rem", "rmk",
    "fact",
    "principle",
    "observation", "obs",
    "claim",
    "question",
    "problem", "prob",
    "criterion",
    "construction", "constr",
    "convention",
    "warning",
    "statement", "stmt",
    "axiom",
    "notation",
    "hypothesis",
    "exercise",
)

TYPE_NORMALIZE = {
    "thm": "theorem",
    "lem": "lemma",
    "prop": "proposition",
    "cor": "corollary",
    "defn": "definition",
    "def": "definition",
    "conj": "conjecture",
    "comp": "computation",
    "ex": "example",
    "rem": "remark",
    "rmk": "remark",
    "obs": "observation",
    "prob": "problem",
    "constr": "construction",
    "stmt": "statement",
}

STATUS_TAGS = (
    ("ProvedHere", r"\\ClaimStatusProvedHere"),
    ("ProvedElsewhere", r"\\ClaimStatusProvedElsewhere"),
    ("Conjectured", r"\\ClaimStatusConjectured"),
    ("Conditional", r"\\ClaimStatusConditional"),
    ("Evidence", r"\\ClaimStatusEvidence"),
    ("Heuristic", r"\\ClaimStatusHeuristic"),
    ("Retracted", r"\\ClaimStatusRetracted"),
)
STATUS_RE = [(name, re.compile(pat)) for name, pat in STATUS_TAGS]

LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|cref|Cref|autoref|nameref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}")
INPUT_RE = re.compile(r"\\(?:input|include|subincludefrom)\{([^}]+)\}")

CHAPTER_RE = re.compile(r"\\chapter\*?(?:\[[^\]]*\])?\{([^}]*)\}")
SECTION_RE = re.compile(r"\\section\*?(?:\[[^\]]*\])?\{([^}]*)\}")
SUBSECTION_RE = re.compile(r"\\subsection\*?(?:\[[^\]]*\])?\{([^}]*)\}")

COMMENT_RE = re.compile(r"(?<!\\)%[^\n]*")


def strip_comments(text: str) -> str:
    """Remove LaTeX % comments while preserving \\%."""
    return COMMENT_RE.sub("", text)


def find_main_tex(repo_root: Path, override: str | None) -> Path | None:
    if override:
        p = repo_root / override
        return p if p.exists() else None
    for cand in ("main.tex",):
        p = repo_root / cand
        if p.exists():
            return p
    return None


def resolve_input(token: str, current_file: Path, repo_root: Path) -> Path | None:
    """Resolve \\input{token} to an absolute path."""
    token = token.strip().split("%", 1)[0].strip()
    bases = [current_file.parent, repo_root]
    for base in bases:
        for ext in (".tex", ""):
            p = (base / (token + ext))
            if p.exists() and p.is_file():
                return p.resolve()
    return None


def gather_files(main_path: Path, repo_root: Path, visited: set[Path] | None = None) -> list[Path]:
    """Recursively gather all .tex files reachable from main_path."""
    if visited is None:
        visited = set()
    main_path = main_path.resolve()
    if main_path in visited:
        return []
    visited.add(main_path)
    files = [main_path]
    try:
        text = main_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return files
    text = strip_comments(text)
    for token in INPUT_RE.findall(text):
        sub = resolve_input(token, main_path, repo_root)
        if sub:
            files.extend(gather_files(sub, repo_root, visited))
    return files


def build_env_regex() -> re.Pattern:
    """Build the regex matching any theorem-like \\begin{...} ... \\end{...}."""
    alt = "|".join(re.escape(e) for e in sorted(THEOREM_ENVS, key=len, reverse=True))
    return re.compile(
        r"\\begin\{(" + alt + r")\*?\}"
        r"(\[(?:[^\[\]]|\[[^\]]*\])*\])?"
        r"(.*?)"
        r"\\end\{\1\*?\}",
        re.DOTALL,
    )


ENV_RE = build_env_regex()


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def detect_status(snippet: str) -> str | None:
    for name, pat in STATUS_RE:
        if pat.search(snippet):
            return name
    return None


def first_label(body: str) -> tuple[str | None, int]:
    m = LABEL_RE.search(body)
    if not m:
        return None, -1
    return m.group(1), m.end()


def extract_refs(body: str) -> list[str]:
    out = []
    for m in REF_RE.findall(body):
        for k in m.split(","):
            k = k.strip()
            if k:
                out.append(k)
    seen = set()
    uniq = []
    for r in out:
        if r not in seen:
            seen.add(r)
            uniq.append(r)
    return uniq


def extract_cites(body: str) -> list[str]:
    out = []
    for m in CITE_RE.findall(body):
        for k in m.split(","):
            k = k.strip()
            if k:
                out.append(k)
    seen = set()
    uniq = []
    for c in out:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def excerpt_of(body: str, max_chars: int = 320) -> str:
    s = re.sub(r"\\label\{[^}]+\}", "", body)
    s = re.sub(r"\\index\{[^}]*\}", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > max_chars:
        s = s[:max_chars].rstrip() + " …"
    return s


def extract_theorems(file_path: Path, repo_root: Path) -> list[dict]:
    rel = str(file_path.relative_to(repo_root))
    try:
        raw = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    text = strip_comments(raw)

    chapter_pos = [(m.start(), m.group(1)) for m in CHAPTER_RE.finditer(text)]
    section_pos = [(m.start(), m.group(1)) for m in SECTION_RE.finditer(text)]
    subsec_pos = [(m.start(), m.group(1)) for m in SUBSECTION_RE.finditer(text)]

    def loc_at(pos: int) -> tuple[str | None, str | None, str | None]:
        ch = next((t for p, t in reversed(chapter_pos) if p <= pos), None)
        sec = next((t for p, t in reversed(section_pos) if p <= pos), None)
        sub = next((t for p, t in reversed(subsec_pos) if p <= pos), None)
        return ch, sec, sub

    nodes = []
    for m in ENV_RE.finditer(text):
        env_raw = m.group(1).rstrip("*")
        env = TYPE_NORMALIZE.get(env_raw, env_raw)
        title = (m.group(2) or "").strip("[]").strip()
        body = m.group(3)

        label, label_end = first_label(body)
        if not label:
            continue

        status = detect_status(title) or detect_status(body[:300])

        refs = extract_refs(body)
        refs = [r for r in refs if r != label]
        cites = extract_cites(body)

        body_after_label = body[label_end:] if label_end > 0 else body
        excerpt = excerpt_of(body_after_label)

        ch, sec, sub = loc_at(m.start())

        nodes.append(
            {
                "id": label,
                "type": env,
                "title": title,
                "status": status,
                "chapter": ch,
                "section": sec,
                "subsection": sub,
                "file": rel,
                "line": line_of(text, m.start()),
                "excerpt": excerpt,
                "refs": refs,
                "cites": cites,
            }
        )

    return nodes


def build_graph(nodes: list[dict]) -> tuple[list[dict], list[dict]]:
    label_set = {n["id"] for n in nodes}
    edges = []
    for n in nodes:
        for ref in n.get("refs", []):
            if ref in label_set and ref != n["id"]:
                edges.append({"source": n["id"], "target": ref, "kind": "cites"})
    return nodes, edges


def emit_json(data: dict, out_path: Path) -> None:
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__TITLE__ — Mathematical Architecture</title>
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    macros: {
      Eone: '{E_1}', Etwo: '{E_2}', Ethree: '{E_3}',
      Ran: '{\\mathrm{Ran}}', Conf: '{\\mathrm{Conf}}',
      ChirHoch: '{\\mathrm{ChirHoch}}', ch: '{\\mathrm{ch}}',
      ord: '{\\mathrm{ord}}', cl: '{\\mathrm{cl}}',
      cA: '{\\mathcal{A}}', cB: '{\\mathcal{B}}', cC: '{\\mathcal{C}}',
      cD: '{\\mathcal{D}}', cF: '{\\mathcal{F}}', cH: '{\\mathcal{H}}',
      cM: '{\\mathcal{M}}', cO: '{\\mathcal{O}}', cV: '{\\mathcal{V}}',
      cW: '{\\mathcal{W}}', cZ: '{\\mathcal{Z}}',
      fg: '{\\mathfrak{g}}', fh: '{\\mathfrak{h}}',
      Bbarch: '{\\bar B^{\\mathrm{ch}}}', Omegach: '{\\Omega^{\\mathrm{ch}}}',
      barB: '{\\bar B}', Tw: '{\\mathrm{Tw}}',
      MC: '{\\mathrm{MC}}', PVA: '{\\mathrm{PVA}}',
      Hom: '{\\mathrm{Hom}}', Ext: '{\\mathrm{Ext}}', Tor: '{\\mathrm{Tor}}',
      Sym: '{\\mathrm{Sym}}', End: '{\\mathrm{End}}', Aut: '{\\mathrm{Aut}}',
      Spec: '{\\mathrm{Spec}}', Proj: '{\\mathrm{Proj}}',
      KZ: '{\\mathrm{KZ}}', BRST: '{\\mathrm{BRST}}',
      Vir: '{\\mathrm{Vir}}', Heis: '{\\mathrm{Heis}}',
      ProvedHere: '{}', ProvedElsewhere: '{}', Conjectured: '{}',
      ClaimStatusProvedHere: '{}', ClaimStatusProvedElsewhere: '{}',
      ClaimStatusConjectured: '{}', ClaimStatusConditional: '{}',
      ClaimStatusEvidence: '{}', ClaimStatusHeuristic: '{}',
      ClaimStatusRetracted: '{}',
      textnormal: ['{\\textrm{#1}}', 1],
      texorpdfstring: ['{#1}', 2]
    }
  },
  svg: { fontCache: 'global' },
  options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] },
  startup: { typeset: false }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js" crossorigin="anonymous"></script>
<style>
  :root { --bg:#fafaf6; --fg:#1a1a1a; --muted:#6b6b6b; --rule:#d8d4c9; --accent:#7d2b2b; --link:#1f4d8b; }
  * { box-sizing: border-box; }
  html,body { margin:0; padding:0; height:100%; font-family: "EB Garamond", Garamond, Georgia, serif; color:var(--fg); background:var(--bg); }
  #app { display:grid; grid-template-columns: 360px 1fr 420px; height:100vh; overflow:hidden; }
  #sidebar { border-right:1px solid var(--rule); padding:1rem; overflow-y:auto; font-size:0.9rem; }
  #sidebar h1 { font-size:1.1rem; margin:0 0 0.25rem; color:var(--accent); }
  #sidebar .meta { color:var(--muted); margin-bottom:0.75rem; font-size:0.8rem; }
  #search { width:100%; padding:0.4rem; font-family:inherit; border:1px solid var(--rule); border-radius:3px; margin-bottom:0.5rem; }
  fieldset { border:1px solid var(--rule); border-radius:3px; padding:0.4rem 0.6rem; margin:0.5rem 0; }
  fieldset legend { font-weight:600; padding:0 0.3rem; font-size:0.78rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.04em; }
  fieldset label { display:block; padding:1px 0; cursor:pointer; font-size:0.85rem; }
  fieldset label input { margin-right:0.4rem; }
  .badge { display:inline-block; padding:1px 5px; border-radius:8px; font-size:0.7rem; margin-left:0.3rem; vertical-align:1px; }
  .b-ProvedHere { background:#cfe6c8; color:#244a17; }
  .b-ProvedElsewhere { background:#dde6c8; color:#3e4818; }
  .b-Conditional { background:#fde9c4; color:#7a5a14; }
  .b-Evidence { background:#cfdff0; color:#1f4d8b; }
  .b-Conjectured { background:#ffd6d0; color:#a32d1d; }
  .b-Heuristic { background:#f0d8eb; color:#6e2660; }
  .b-Retracted { background:#999; color:#fff; text-decoration:line-through; }
  .b-Unmarked { background:#e6e3da; color:#6b6b6b; }
  ul.node-list { list-style:none; padding:0; margin:0.5rem 0 0; }
  ul.node-list li { padding:4px 6px; border-bottom:1px dotted var(--rule); cursor:pointer; }
  ul.node-list li:hover { background:#f4f1e6; }
  ul.node-list li.selected { background:#efe7ce; }
  ul.node-list .nl-id { font-family: "SFMono-Regular", Menlo, Consolas, monospace; font-size:0.78rem; color:var(--muted); }
  ul.node-list .nl-title { font-size:0.88rem; }
  ul.node-list .nl-loc { font-size:0.72rem; color:var(--muted); display:block; }
  #cy { height:100%; background:#fbfaf3; position:relative; }
  #cy-status { position:absolute; top:8px; left:50%; transform:translateX(-50%); background:rgba(255,255,255,0.95); border:1px solid var(--rule); padding:6px 12px; border-radius:4px; font-size:0.78rem; color:var(--muted); z-index:10; pointer-events:none; }
  #cy-status button { pointer-events:auto; margin-left:0.5rem; padding:2px 8px; font-size:0.78rem; cursor:pointer; }
  #cy-error { padding:2rem; color:#a32d1d; background:#fdf0ee; border:1px solid #f3c0b8; margin:1rem; border-radius:4px; font-family:Menlo,monospace; font-size:0.85rem; white-space:pre-wrap; }
  #detail { border-left:1px solid var(--rule); padding:1rem; overflow-y:auto; font-size:0.92rem; }
  #detail .empty { color:var(--muted); font-style:italic; }
  #detail h2 { margin:0 0 0.4rem; font-size:1.1rem; color:var(--accent); font-weight:600; }
  #detail .label { font-family:Menlo,monospace; font-size:0.78rem; color:var(--muted); margin-bottom:0.5rem; word-break:break-all; }
  #detail .where { font-size:0.8rem; color:var(--muted); margin-bottom:0.7rem; }
  #detail .excerpt { line-height:1.5; margin-bottom:0.8rem; padding:0.6rem; background:#fff; border-left:3px solid var(--rule); }
  #detail h3 { font-size:0.85rem; margin:1rem 0 0.3rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.04em; font-weight:600; }
  #detail ul.refs { margin:0.2rem 0; padding-left:1rem; font-size:0.85rem; }
  #detail ul.refs li { padding:1px 0; }
  #detail ul.refs li a { color:var(--link); cursor:pointer; text-decoration:none; }
  #detail ul.refs li a:hover { text-decoration:underline; }
  .legend-row { display:flex; flex-wrap:wrap; gap:0.4rem; margin-top:0.4rem; }
</style>
</head>
<body>
<div id="app">
  <aside id="sidebar">
    <h1>__TITLE__</h1>
    <div class="meta">__META__</div>
    <input id="search" placeholder="Search labels, titles, statements…">
    <fieldset>
      <legend>Status</legend>
      <div id="status-filters"></div>
    </fieldset>
    <fieldset>
      <legend>Type</legend>
      <div id="type-filters"></div>
    </fieldset>
    <fieldset>
      <legend>Chapter</legend>
      <select id="chapter-filter" style="width:100%; padding:0.3rem;"><option value="">All chapters</option></select>
    </fieldset>
    <ul id="node-list" class="node-list"></ul>
  </aside>
  <main id="cy"><div id="cy-status">initializing graph…</div></main>
  <aside id="detail"><p class="empty">Click a node or list item.</p></aside>
</div>
<script>
const DATA = __PAYLOAD__;
const RENDER_CAP = 2000;

const STATUS_ORDER = ["ProvedHere","ProvedElsewhere","Conditional","Evidence","Conjectured","Heuristic","Retracted","Unmarked"];
const STATUS_COLOR = {
  ProvedHere:"#7aa86a", ProvedElsewhere:"#9aa86a", Conditional:"#d6a04a", Evidence:"#5a86c4",
  Conjectured:"#c4585a", Heuristic:"#a45e9c", Retracted:"#9b9b9b", Unmarked:"#b8b3a3"
};
const TYPE_SHAPE = {
  theorem:"hexagon", lemma:"round-rectangle", proposition:"round-rectangle",
  corollary:"diamond", definition:"rectangle", conjecture:"star", computation:"triangle",
  remark:"ellipse", example:"vee", fact:"ellipse", principle:"hexagon",
  observation:"ellipse", claim:"ellipse", question:"ellipse", problem:"ellipse",
  criterion:"ellipse", construction:"rectangle", convention:"tag", warning:"vee"
};
function statusOf(n){ return n.status || "Unmarked"; }

const state = {
  selected: null,
  filters: {
    statuses: new Set(STATUS_ORDER),
    types: new Set(),
    chapter: "",
    query: ""
  }
};

function buildFilters(){
  const sCounts = {}, tCounts = {};
  const chapters = new Set();
  for (const n of DATA.nodes){
    const s = statusOf(n); sCounts[s] = (sCounts[s]||0)+1;
    tCounts[n.type] = (tCounts[n.type]||0)+1;
    if (n.chapter) chapters.add(n.chapter);
  }
  const sBox = document.getElementById("status-filters");
  for (const s of STATUS_ORDER){
    const c = sCounts[s]||0; if (!c) continue;
    const id = "f-st-"+s;
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" id="${id}" checked> <span class="badge b-${s}">${s}</span> <span style="color:var(--muted); font-size:0.78rem;">${c}</span>`;
    sBox.appendChild(lbl);
    lbl.querySelector("input").addEventListener("change", e => {
      if (e.target.checked) state.filters.statuses.add(s); else state.filters.statuses.delete(s);
      apply();
    });
  }
  const tBox = document.getElementById("type-filters");
  const tSorted = Object.entries(tCounts).sort((a,b)=>b[1]-a[1]);
  for (const [t,c] of tSorted){
    state.filters.types.add(t);
    const id = "f-tp-"+t;
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" id="${id}" checked> ${t} <span style="color:var(--muted); font-size:0.78rem;">${c}</span>`;
    tBox.appendChild(lbl);
    lbl.querySelector("input").addEventListener("change", e => {
      if (e.target.checked) state.filters.types.add(t); else state.filters.types.delete(t);
      apply();
    });
  }
  const chSel = document.getElementById("chapter-filter");
  const chSorted = [...chapters].sort();
  for (const ch of chSorted){
    const o = document.createElement("option"); o.value = ch; o.textContent = ch.length>52 ? ch.slice(0,50)+"…" : ch; chSel.appendChild(o);
  }
  chSel.addEventListener("change", e => { state.filters.chapter = e.target.value; apply(); });
  document.getElementById("search").addEventListener("input", e => { state.filters.query = e.target.value.toLowerCase(); apply(); });
}

function passes(n){
  if (!state.filters.statuses.has(statusOf(n))) return false;
  if (!state.filters.types.has(n.type)) return false;
  if (state.filters.chapter && n.chapter !== state.filters.chapter) return false;
  if (state.filters.query){
    const hay = ((n.id||"")+" "+(n.title||"")+" "+(n.excerpt||"")).toLowerCase();
    if (!hay.includes(state.filters.query)) return false;
  }
  return true;
}

let cy;
let renderingAll = false;
function pickRenderNodes(all){
  if (renderingAll || all.length <= RENDER_CAP) return all;
  // Score nodes: status priority + type priority + has-deps signal
  const statusW = { ProvedHere:5, Conditional:4, ProvedElsewhere:4, Conjectured:3, Evidence:3, Heuristic:2, Retracted:1, Unmarked:0 };
  const typeW = { theorem:5, proposition:4, lemma:3, corollary:3, definition:2, conjecture:4, computation:3, principle:5, construction:2 };
  const inDeg = {};
  for (const e of DATA.edges){ inDeg[e.target] = (inDeg[e.target]||0) + 1; }
  const scored = all.map(n => ({ n, s: (statusW[statusOf(n)]||0) + (typeW[n.type]||0) + Math.min(5, inDeg[n.id]||0) }));
  scored.sort((a,b) => b.s - a.s);
  return scored.slice(0, RENDER_CAP).map(x => x.n);
}

function setStatus(html){
  const el = document.getElementById("cy-status");
  if (el) el.innerHTML = html;
}

function buildCy(){
  try {
    if (typeof cytoscape === "undefined"){
      throw new Error("cytoscape failed to load (check network / CDN access)");
    }
    const total = DATA.nodes.length;
    const rendered = pickRenderNodes(DATA.nodes);
    const renderedIds = new Set(rendered.map(n => n.id));
    const elements = [];
    for (const n of rendered){
      elements.push({ data:{ id:n.id, label:(n.title||n.id).slice(0,30), type:n.type, status:statusOf(n) }});
    }
    for (const e of DATA.edges){
      if (renderedIds.has(e.source) && renderedIds.has(e.target)){
        elements.push({ data:{ id: e.source+"->"+e.target, source:e.source, target:e.target, kind:e.kind || "cites" }});
      }
    }
    cy = cytoscape({
      container: document.getElementById("cy"),
      elements,
      style: [
        { selector: "node", style: {
            "label": "data(label)", "font-size": 8, "color":"#222",
            "text-wrap":"ellipsis", "text-max-width": 64,
            "background-color": "data(status)",
            "shape": "ellipse",
            "border-color":"#555","border-width":0.4,
            "width": 14, "height": 14
        }},
        ...Object.entries(STATUS_COLOR).map(([s,c]) => ({ selector: `node[status = '${s}']`, style: { "background-color": c }})),
        ...Object.entries(TYPE_SHAPE).map(([t,sh]) => ({ selector: `node[type = '${t}']`, style: { "shape": sh }})),
        { selector: "edge", style: {
            "width":0.5, "line-color":"#9c948a", "curve-style":"haystack",
            "target-arrow-shape":"none", "opacity":0.4
        }},
        { selector: "node:selected", style: {
            "border-width": 2, "border-color":"#1a1a1a",
            "width":22, "height":22, "font-size":11, "z-index":99
        }},
        { selector: "node.faded", style: {"opacity":0.08, "text-opacity":0}},
        { selector: "edge.faded", style: {"opacity":0.04}},
        { selector: "node.highlight", style: {"border-width":1.5, "border-color":"#7d2b2b", "z-index":50}},
        { selector: "edge.highlight", style: {"opacity":0.95, "line-color":"#7d2b2b", "width":1.4, "z-index":40}},
      ],
      layout: { name: "cose", animate: false, fit: true, padding: 30, idealEdgeLength: 50, nodeRepulsion: 3000, gravity: 0.3, numIter: 250, randomize: true },
      wheelSensitivity: 0.2,
      minZoom: 0.05, maxZoom: 5,
    });
    cy.on("tap", "node", evt => select(evt.target.id()));
    cy.on("tap", e => { if (e.target === cy) clearHighlight(); });
    if (rendered.length < total){
      setStatus(`rendering ${rendered.length} of ${total} top-priority nodes · <button id="render-all-btn">render all</button>`);
      const btn = document.getElementById("render-all-btn");
      if (btn) btn.addEventListener("click", () => {
        renderingAll = true;
        setStatus(`re-laying out ${total} nodes (this may take 30s+)…`);
        setTimeout(() => { try { cy.destroy(); } catch(_){} buildCy(); }, 50);
      });
    } else {
      setStatus(`${rendered.length} nodes rendered`);
      setTimeout(() => { const el = document.getElementById("cy-status"); if (el) el.style.display = "none"; }, 2000);
    }
  } catch (err) {
    const cyDiv = document.getElementById("cy");
    cyDiv.innerHTML = `<div id="cy-error">Graph failed to render:\n\n${(err && err.stack) || err}\n\nThe sidebar list and detail panel still work — click a node label there.</div>`;
    console.error(err);
  }
}

function buildList(){
  const ul = document.getElementById("node-list");
  ul.innerHTML = "";
  const visible = DATA.nodes.filter(passes);
  visible.sort((a,b)=>(a.file||"").localeCompare(b.file||"") || (a.line||0)-(b.line||0));
  for (const n of visible){
    const li = document.createElement("li");
    li.dataset.id = n.id;
    const status = statusOf(n);
    li.innerHTML = `<div class="nl-title">${escapeHtml(n.title || n.id)} <span class="badge b-${status}">${n.type}</span></div>
                    <span class="nl-id">${escapeHtml(n.id)}</span>
                    <span class="nl-loc">${escapeHtml(n.chapter || "")}${n.section ? " · "+escapeHtml(n.section) : ""}</span>`;
    li.addEventListener("click", () => select(n.id));
    ul.appendChild(li);
  }
}

function clearHighlight(){
  if (!cy) return;
  cy.elements().removeClass("faded highlight");
  cy.nodes(":selected").unselect();
  state.selected = null;
  document.getElementById("detail").innerHTML = `<p class="empty">Click a node or list item.</p>`;
  document.querySelectorAll("#node-list li.selected").forEach(li=>li.classList.remove("selected"));
}

function select(id){
  state.selected = id;
  const node = DATA.nodes.find(x => x.id === id);
  if (!node) return;
  if (cy){
    const ele = cy.getElementById(id);
    if (ele && ele.length){
      cy.elements().addClass("faded").removeClass("highlight");
      ele.removeClass("faded").addClass("highlight");
      const neighbours = ele.neighborhood();
      neighbours.removeClass("faded").addClass("highlight");
      cy.animate({ center: { eles: ele }, zoom: Math.max(cy.zoom(), 0.6), duration: 300 });
    }
  }
  document.querySelectorAll("#node-list li.selected").forEach(li=>li.classList.remove("selected"));
  const li = document.querySelector(`#node-list li[data-id="${cssEscape(id)}"]`);
  if (li){ li.classList.add("selected"); li.scrollIntoView({block:"nearest", behavior:"smooth"}); }
  renderDetail(node);
}

function renderDetail(n){
  const el = document.getElementById("detail");
  const status = statusOf(n);
  const incoming = DATA.edges.filter(e => e.target === n.id).map(e => e.source);
  const outgoing = (n.refs || []).filter(r => DATA.nodes.some(x => x.id === r));
  const externalRefs = (n.refs || []).filter(r => !DATA.nodes.some(x => x.id === r));
  el.innerHTML = `
    <h2>${escapeHtml(n.title || n.id)} <span class="badge b-${status}">${status}</span></h2>
    <div class="label">${escapeHtml(n.type)} · <code>${escapeHtml(n.id)}</code></div>
    <div class="where">
      ${n.chapter ? "📖 "+escapeHtml(n.chapter) : ""}
      ${n.section ? " · §"+escapeHtml(n.section) : ""}
      ${n.subsection ? " · "+escapeHtml(n.subsection) : ""}
      <br>📄 <code>${escapeHtml(n.file)}:${n.line}</code>
    </div>
    <div class="excerpt">${renderMath(n.excerpt || "")}</div>
    ${outgoing.length ? `<h3>Cites (in-graph) — ${outgoing.length}</h3><ul class="refs">${outgoing.map(r=>`<li><a data-id="${escapeHtml(r)}">${escapeHtml(r)}</a></li>`).join("")}</ul>` : ""}
    ${incoming.length ? `<h3>Cited by — ${incoming.length}</h3><ul class="refs">${incoming.map(r=>`<li><a data-id="${escapeHtml(r)}">${escapeHtml(r)}</a></li>`).join("")}</ul>` : ""}
    ${externalRefs.length ? `<h3>External refs — ${externalRefs.length}</h3><ul class="refs" style="color:var(--muted)">${externalRefs.map(r=>`<li>${escapeHtml(r)}</li>`).join("")}</ul>` : ""}
    ${n.cites && n.cites.length ? `<h3>Bibliography — ${n.cites.length}</h3><ul class="refs" style="color:var(--muted)">${n.cites.slice(0,40).map(r=>`<li>${escapeHtml(r)}</li>`).join("")}${n.cites.length>40?"<li>…</li>":""}</ul>` : ""}
  `;
  el.querySelectorAll("a[data-id]").forEach(a => a.addEventListener("click", e => select(e.target.dataset.id)));
  if (window.MathJax && window.MathJax.typesetPromise){
    window.MathJax.typesetPromise([el]).catch(e => console.warn("MathJax typeset error:", e));
  }
}

function renderMath(s){ return escapeHtml(s); }
function escapeHtml(s){ if (s==null) return ""; return String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"})[c]); }
function cssEscape(s){ return String(s).replace(/[^a-zA-Z0-9_-]/g, c => "\\"+c); }

function apply(){
  if (cy){
    cy.batch(() => {
      for (const n of DATA.nodes){
        const ele = cy.getElementById(n.id);
        if (!ele.length) continue;
        if (passes(n)) ele.removeClass("faded"); else ele.addClass("faded");
      }
    });
  }
  buildList();
}

buildFilters();
buildCy();
buildList();
</script>
</body>
</html>
"""


def render_html(data: dict, title: str) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    meta = data["meta"]
    sc = ", ".join(f"{k}={v}" for k, v in sorted(meta.get("status_counts", {}).items(), key=lambda kv: -kv[1]))
    meta_str = (
        f"{meta['total_nodes']} blocks · {meta['total_edges']} internal edges · "
        f"{meta['files_scanned']} files · {meta['generated_at'][:19]}Z"
        + (f"<br><span style=\"font-size:0.72rem;\">{sc}</span>" if sc else "")
    )
    return (
        HTML_TEMPLATE
        .replace("__TITLE__", title)
        .replace("__META__", meta_str)
        .replace("__PAYLOAD__", payload)
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", default=".", help="Repo root (default: cwd)")
    ap.add_argument("--main", default=None, help="Entry .tex file (default: main.tex)")
    ap.add_argument("--out", default="out", help="Output dir (default: out)")
    ap.add_argument("--volume", default=None, help="Volume label (default: dirname)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    repo_root = Path(args.root).resolve()
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = repo_root / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    main_path = find_main_tex(repo_root, args.main)
    if not main_path:
        print(f"  fail  no main.tex in {repo_root}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"  -- Architecture extractor --")
        print(f"  root: {repo_root}")
        print(f"  main: {main_path.relative_to(repo_root)}")

    files = gather_files(main_path, repo_root)
    nodes = []
    for f in files:
        nodes.extend(extract_theorems(f, repo_root))
    nodes, edges = build_graph(nodes)

    status_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    for n in nodes:
        s = n.get("status") or "Unmarked"
        status_counts[s] = status_counts.get(s, 0) + 1
        type_counts[n["type"]] = type_counts.get(n["type"], 0) + 1

    volume = args.volume or repo_root.name

    data = {
        "meta": {
            "volume": volume,
            "repo": str(repo_root),
            "main": str(main_path.relative_to(repo_root)),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "files_scanned": len(files),
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "status_counts": status_counts,
            "type_counts": type_counts,
        },
        "nodes": nodes,
        "edges": edges,
    }

    json_path = out_dir / "architecture.json"
    emit_json(data, json_path)
    html_path = out_dir / "architecture.html"
    html_path.write_text(render_html(data, volume), encoding="utf-8")

    if not args.quiet:
        print(f"  scanned {len(files)} files")
        print(f"  found {len(nodes)} theorem-like blocks ({len(edges)} internal edges)")
        for st, c in sorted(status_counts.items(), key=lambda kv: -kv[1]):
            print(f"    {st:>20s}  {c}")
        print(f"  ok  {json_path}")
        print(f"  ok  {html_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
