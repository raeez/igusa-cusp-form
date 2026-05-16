#!/usr/bin/env python3
"""
build_unified_architecture.py -- aggregate per-repo architecture.json into
the cross-volume mathematical architecture map.

Reads:
  $MATHEMATICS_DIR/architecture/<volume>.json   (one per math repo)

Writes:
  $MATHEMATICS_DIR/architecture.json            (merged graph)
  $MATHEMATICS_DIR/architecture.html            (interactive viewer)

Cross-volume edges are inferred when a node's \\ref{label} target does
not exist in its own volume but does exist in another volume.

Run from any repo:
  python3 scripts/build_unified_architecture.py [--mathematics-dir ~/mathematics]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

VOLUME_TITLES = {
    "vol1": "Vol I — Modular Koszul Duality",
    "vol2": "Vol II — A∞ Chiral Algebras and Chiral Hochschild",
    "vol3": "Vol III — CY-to-Chiral, Yangians, BKM",
    "vol4": "Vol IV — Arithmetic Chiral Homology and Deninger",
    "igusa": "Igusa cusp form — Automorphic corrections",
    "mixed": "Mixed Holomorphic-Topological Strings",
}

VOLUME_COLOR = {
    "vol1": "#7d2b2b",
    "vol2": "#1f4d8b",
    "vol3": "#3a7d44",
    "vol4": "#7a5a14",
    "igusa": "#6e2660",
    "mixed": "#1f6f7d",
    "_other": "#555",
}


def load_volumes(arch_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for jf in sorted(arch_dir.glob("*.json")):
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  warn  {jf}: {e}", file=sys.stderr)
            continue
        vol = jf.stem
        if "meta" in data:
            data["meta"]["volume"] = data["meta"].get("volume", vol) or vol
        out[vol] = data
    return out


def prefixed(volume: str, label: str) -> str:
    return f"{volume}::{label}"


def merge(volumes: dict[str, dict]) -> dict:
    nodes_by_volume_label: dict[tuple[str, str], dict] = {}
    nodes_out: list[dict] = []
    cross_index: dict[str, list[str]] = {}  # bare label -> list of volumes containing it

    for vol, data in volumes.items():
        local_labels = {n["id"] for n in data.get("nodes", [])}
        for n in data.get("nodes", []):
            label = n["id"]
            cross_index.setdefault(label, []).append(vol)
            new = dict(n)
            new["id"] = prefixed(vol, label)
            new["bare_id"] = label
            new["volume"] = vol
            new["local_in_volume"] = True
            nodes_by_volume_label[(vol, label)] = new
            nodes_out.append(new)

    edges_out: list[dict] = []
    intra = 0
    cross = 0
    dangling = 0

    for vol, data in volumes.items():
        local_labels = {n["id"] for n in data.get("nodes", [])}
        for n in data.get("nodes", []):
            src_id = prefixed(vol, n["id"])
            for ref in n.get("refs", []) or []:
                if ref in local_labels:
                    edges_out.append({"source": src_id, "target": prefixed(vol, ref), "kind": "cites"})
                    intra += 1
                else:
                    targets = [v for v in cross_index.get(ref, []) if v != vol]
                    if targets:
                        for t_vol in targets:
                            edges_out.append({"source": src_id, "target": prefixed(t_vol, ref), "kind": "cross-volume"})
                            cross += 1
                    else:
                        dangling += 1

    status_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    volume_counts: dict[str, int] = {}
    for n in nodes_out:
        s = n.get("status") or "Unmarked"
        status_counts[s] = status_counts.get(s, 0) + 1
        type_counts[n.get("type", "?")] = type_counts.get(n.get("type", "?"), 0) + 1
        volume_counts[n.get("volume", "?")] = volume_counts.get(n.get("volume", "?"), 0) + 1

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "volumes": list(volumes.keys()),
        "volume_counts": volume_counts,
        "status_counts": status_counts,
        "type_counts": type_counts,
        "total_nodes": len(nodes_out),
        "total_edges": len(edges_out),
        "intra_volume_edges": intra,
        "cross_volume_edges": cross,
        "dangling_refs": dangling,
        "per_volume": {
            v: data.get("meta", {})
            for v, data in volumes.items()
        },
    }
    return {"meta": meta, "nodes": nodes_out, "edges": edges_out}


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Mathematics — Cross-Volume Architecture</title>
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
  :root { --bg:#fafaf6; --fg:#1a1a1a; --muted:#6b6b6b; --rule:#d8d4c9; --link:#1f4d8b; }
  * { box-sizing: border-box; }
  html,body { margin:0; padding:0; height:100%; font-family:"EB Garamond",Garamond,Georgia,serif; color:var(--fg); background:var(--bg); }
  #app { display:grid; grid-template-columns: 380px 1fr 420px; height:100vh; overflow:hidden; }
  #sidebar { border-right:1px solid var(--rule); padding:1rem; overflow-y:auto; font-size:0.9rem; }
  #sidebar h1 { font-size:1.15rem; margin:0 0 0.25rem; }
  #sidebar .meta { color:var(--muted); margin-bottom:0.75rem; font-size:0.8rem; }
  #search { width:100%; padding:0.4rem; font-family:inherit; border:1px solid var(--rule); border-radius:3px; margin-bottom:0.5rem; }
  fieldset { border:1px solid var(--rule); border-radius:3px; padding:0.4rem 0.6rem; margin:0.5rem 0; }
  fieldset legend { font-weight:600; padding:0 0.3rem; font-size:0.78rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.04em; }
  fieldset label { display:block; padding:1px 0; cursor:pointer; font-size:0.85rem; }
  fieldset label input { margin-right:0.4rem; }
  .badge { display:inline-block; padding:1px 6px; border-radius:8px; font-size:0.7rem; margin-left:0.3rem; vertical-align:1px; color:#fff; }
  .b-vol { color:#fff; }
  .b-ProvedHere { background:#7aa86a; color:#fff; }
  .b-ProvedElsewhere { background:#9aa86a; color:#fff; }
  .b-Conditional { background:#d6a04a; color:#fff; }
  .b-Evidence { background:#5a86c4; color:#fff; }
  .b-Conjectured { background:#c4585a; color:#fff; }
  .b-Heuristic { background:#a45e9c; color:#fff; }
  .b-Retracted { background:#9b9b9b; color:#fff; text-decoration:line-through; }
  .b-Unmarked { background:#b8b3a3; color:#fff; }
  ul.node-list { list-style:none; padding:0; margin:0.5rem 0 0; }
  ul.node-list li { padding:4px 6px; border-bottom:1px dotted var(--rule); cursor:pointer; }
  ul.node-list li:hover { background:#f4f1e6; }
  ul.node-list li.selected { background:#efe7ce; }
  .nl-id { font-family:Menlo,monospace; font-size:0.78rem; color:var(--muted); }
  .nl-loc { font-size:0.72rem; color:var(--muted); display:block; }
  #cy { height:100%; background:#fbfaf3; position:relative; }
  #cy-status { position:absolute; top:8px; left:50%; transform:translateX(-50%); background:rgba(255,255,255,0.95); border:1px solid var(--rule); padding:6px 12px; border-radius:4px; font-size:0.78rem; color:var(--muted); z-index:10; pointer-events:none; }
  #cy-status button { pointer-events:auto; margin-left:0.5rem; padding:2px 8px; font-size:0.78rem; cursor:pointer; }
  #cy-error { padding:2rem; color:#a32d1d; background:#fdf0ee; border:1px solid #f3c0b8; margin:1rem; border-radius:4px; font-family:Menlo,monospace; font-size:0.85rem; white-space:pre-wrap; }
  #detail { border-left:1px solid var(--rule); padding:1rem; overflow-y:auto; font-size:0.92rem; }
  #detail .empty { color:var(--muted); font-style:italic; }
  #detail h2 { margin:0 0 0.4rem; font-size:1.1rem; font-weight:600; }
  #detail .label { font-family:Menlo,monospace; font-size:0.78rem; color:var(--muted); margin-bottom:0.5rem; word-break:break-all; }
  #detail .where { font-size:0.8rem; color:var(--muted); margin-bottom:0.7rem; }
  #detail .excerpt { line-height:1.5; margin-bottom:0.8rem; padding:0.6rem; background:#fff; border-left:3px solid var(--rule); }
  #detail h3 { font-size:0.85rem; margin:1rem 0 0.3rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.04em; font-weight:600; }
  #detail ul.refs { margin:0.2rem 0; padding-left:1rem; font-size:0.85rem; }
  #detail ul.refs li a { color:var(--link); cursor:pointer; text-decoration:none; }
  #detail ul.refs li a:hover { text-decoration:underline; }
</style>
</head>
<body>
<div id="app">
  <aside id="sidebar">
    <h1>Mathematics — cross-volume architecture</h1>
    <div class="meta">__META__</div>
    <input id="search" placeholder="Search labels, titles, statements…">
    <fieldset><legend>Volume</legend><div id="volume-filters"></div></fieldset>
    <fieldset><legend>Status</legend><div id="status-filters"></div></fieldset>
    <fieldset><legend>Type</legend><div id="type-filters"></div></fieldset>
    <fieldset><legend>Edges</legend>
      <label><input type="checkbox" id="show-intra" checked> intra-volume</label>
      <label><input type="checkbox" id="show-cross" checked> cross-volume</label>
    </fieldset>
    <ul id="node-list" class="node-list"></ul>
  </aside>
  <main id="cy"><div id="cy-status">initializing graph…</div></main>
  <aside id="detail"><p class="empty">Click a node or list item.</p></aside>
</div>
<script>
const DATA = __PAYLOAD__;
const RENDER_CAP = 2000;
const VOLUME_TITLES = __VOLUME_TITLES__;
const VOLUME_COLOR = __VOLUME_COLOR__;

const STATUS_ORDER = ["ProvedHere","ProvedElsewhere","Conditional","Evidence","Conjectured","Heuristic","Retracted","Unmarked"];
const TYPE_SHAPE = {
  theorem:"hexagon", lemma:"round-rectangle", proposition:"round-rectangle",
  corollary:"diamond", definition:"rectangle", conjecture:"star", computation:"triangle",
  remark:"ellipse", example:"vee", fact:"ellipse", principle:"hexagon",
  observation:"ellipse", claim:"ellipse", question:"ellipse", problem:"ellipse",
  criterion:"ellipse", construction:"rectangle", convention:"tag", warning:"vee",
  statement:"ellipse", axiom:"hexagon", notation:"tag", hypothesis:"ellipse", exercise:"vee"
};

function statusOf(n){ return n.status || "Unmarked"; }
function colorOf(n){ return VOLUME_COLOR[n.volume] || VOLUME_COLOR._other || "#888"; }

const state = {
  selected: null,
  filters: {
    volumes: new Set(Object.keys(VOLUME_TITLES)),
    statuses: new Set(STATUS_ORDER),
    types: new Set(),
    edges: { intra: true, cross: true },
    query: ""
  }
};

function buildFilters(){
  const vCounts = {}, sCounts = {}, tCounts = {};
  for (const n of DATA.nodes){
    vCounts[n.volume] = (vCounts[n.volume]||0)+1;
    sCounts[statusOf(n)] = (sCounts[statusOf(n)]||0)+1;
    tCounts[n.type] = (tCounts[n.type]||0)+1;
  }
  const vBox = document.getElementById("volume-filters");
  const vSorted = Object.entries(vCounts).sort((a,b)=>(b[1]-a[1]));
  for (const [v,c] of vSorted){
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" checked> <span class="badge" style="background:${VOLUME_COLOR[v]||'#555'}">${v}</span> ${(VOLUME_TITLES[v]||v).split(' — ')[1]||v} <span style="color:var(--muted); font-size:0.78rem;">(${c})</span>`;
    vBox.appendChild(lbl);
    lbl.querySelector("input").addEventListener("change", e => {
      if (e.target.checked) state.filters.volumes.add(v); else state.filters.volumes.delete(v);
      apply();
    });
  }
  const sBox = document.getElementById("status-filters");
  for (const s of STATUS_ORDER){
    const c = sCounts[s]||0; if (!c) continue;
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" checked> <span class="badge b-${s}">${s}</span> <span style="color:var(--muted); font-size:0.78rem;">${c}</span>`;
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
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" checked> ${t} <span style="color:var(--muted); font-size:0.78rem;">(${c})</span>`;
    tBox.appendChild(lbl);
    lbl.querySelector("input").addEventListener("change", e => {
      if (e.target.checked) state.filters.types.add(t); else state.filters.types.delete(t);
      apply();
    });
  }
  document.getElementById("search").addEventListener("input", e => { state.filters.query = e.target.value.toLowerCase(); apply(); });
  document.getElementById("show-intra").addEventListener("change", e => { state.filters.edges.intra = e.target.checked; apply(); });
  document.getElementById("show-cross").addEventListener("change", e => { state.filters.edges.cross = e.target.checked; apply(); });
}

function passesNode(n){
  if (!state.filters.volumes.has(n.volume)) return false;
  if (!state.filters.statuses.has(statusOf(n))) return false;
  if (!state.filters.types.has(n.type)) return false;
  if (state.filters.query){
    const hay = ((n.bare_id||"")+" "+(n.title||"")+" "+(n.excerpt||"")).toLowerCase();
    if (!hay.includes(state.filters.query)) return false;
  }
  return true;
}

let cy;
let renderingAll = false;
function pickRenderNodes(all){
  if (renderingAll || all.length <= RENDER_CAP) return all;
  // Score: status + type + cross-volume edge incidence + intra-volume in-degree
  const statusW = { ProvedHere:5, Conditional:4, ProvedElsewhere:4, Conjectured:3, Evidence:3, Heuristic:2, Retracted:1, Unmarked:0 };
  const typeW = { theorem:5, proposition:4, lemma:3, corollary:3, definition:2, conjecture:4, computation:3, principle:5, construction:2 };
  const inDeg = {}, crossDeg = {};
  for (const e of DATA.edges){
    inDeg[e.target] = (inDeg[e.target]||0) + 1;
    if (e.kind === "cross-volume"){
      crossDeg[e.target] = (crossDeg[e.target]||0) + 1;
      crossDeg[e.source] = (crossDeg[e.source]||0) + 1;
    }
  }
  const scored = all.map(n => ({ n, s: (statusW[statusOf(n)]||0) + (typeW[n.type]||0) + Math.min(5, inDeg[n.id]||0) + 5*Math.min(3, crossDeg[n.id]||0) }));
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
      elements.push({ data:{ id:n.id, label:(n.title||n.bare_id||n.id).slice(0,28), volume:n.volume, type:n.type, status:statusOf(n) }});
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
            "label": "data(label)", "font-size": 7, "color":"#222",
            "text-wrap":"ellipsis", "text-max-width": 56,
            "background-color": "data(volume)",
            "shape": "ellipse",
            "border-color":"#222","border-width":0.4,
            "width": 12, "height": 12, "opacity":0.85
        }},
        ...Object.entries(VOLUME_COLOR).map(([v,c]) => ({ selector: `node[volume = '${v}']`, style: { "background-color": c }})),
        ...Object.entries(TYPE_SHAPE).map(([t,sh]) => ({ selector: `node[type = '${t}']`, style: { "shape": sh }})),
        { selector: "edge[kind = 'cites']", style: {
            "width":0.4, "line-color":"#9c948a", "curve-style":"haystack",
            "target-arrow-shape":"none", "opacity":0.4
        }},
        { selector: "edge[kind = 'cross-volume']", style: {
            "width":1.2, "line-color":"#c4585a", "curve-style":"bezier",
            "target-arrow-shape":"triangle", "target-arrow-color":"#c4585a",
            "arrow-scale":0.6, "opacity":0.85
        }},
        { selector: "node:selected", style: {
            "border-width": 2, "border-color":"#1a1a1a",
            "width":20, "height":20, "font-size":11, "z-index":99
        }},
        { selector: "node.faded", style: {"opacity":0.06, "text-opacity":0}},
        { selector: "edge.faded", style: {"opacity":0.03}},
        { selector: "node.highlight", style: {"border-width":1.5, "border-color":"#000", "z-index":50}},
        { selector: "edge.highlight", style: {"opacity":0.95, "width":1.4, "z-index":40}},
      ],
      layout: { name: "cose", animate: false, fit: true, padding: 30, idealEdgeLength: 40, nodeRepulsion: 2500, gravity: 0.3, numIter: 250, randomize: true },
      wheelSensitivity: 0.2,
      minZoom: 0.03, maxZoom: 5,
    });
    cy.on("tap", "node", evt => select(evt.target.id()));
    cy.on("tap", e => { if (e.target === cy) clearHighlight(); });
    if (rendered.length < total){
      setStatus(`rendering ${rendered.length} of ${total} top-priority nodes (cross-volume edges + ProvedHere/Conditional + theorems prioritized) · <button id="render-all-btn">render all</button>`);
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
  const visible = DATA.nodes.filter(passesNode);
  visible.sort((a,b)=>(a.volume||"").localeCompare(b.volume||"") || (a.file||"").localeCompare(b.file||"") || (a.line||0)-(b.line||0));
  let v = "";
  for (const n of visible.slice(0, 2000)){
    if (n.volume !== v){
      v = n.volume;
      const h = document.createElement("li");
      h.style.background = (VOLUME_COLOR[v]||"#555");
      h.style.color = "#fff";
      h.style.padding = "3px 6px";
      h.style.fontWeight = "600";
      h.style.fontSize = "0.78rem";
      h.style.cursor = "default";
      h.textContent = (VOLUME_TITLES[v]||v);
      ul.appendChild(h);
    }
    const li = document.createElement("li");
    li.dataset.id = n.id;
    const status = statusOf(n);
    li.innerHTML = `<div><span class="badge b-${status}">${n.type}</span> ${escapeHtml(n.title || n.bare_id || n.id)}</div>
                    <span class="nl-id">${escapeHtml(n.bare_id || n.id)}</span>
                    <span class="nl-loc">${escapeHtml(n.chapter || "")}</span>`;
    li.addEventListener("click", () => select(n.id));
    ul.appendChild(li);
  }
  if (visible.length > 2000){
    const m = document.createElement("li");
    m.style.color = "var(--muted)"; m.style.fontStyle = "italic";
    m.textContent = `… ${visible.length-2000} more (refine filters to narrow)`;
    ul.appendChild(m);
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
      cy.animate({ center: { eles: ele }, zoom: Math.max(cy.zoom(), 0.4), duration: 300 });
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
  const incoming = DATA.edges.filter(e => e.target === n.id);
  const outgoing = DATA.edges.filter(e => e.source === n.id);
  const incCross = incoming.filter(e => e.kind === "cross-volume");
  const incIntra = incoming.filter(e => e.kind !== "cross-volume");
  const outCross = outgoing.filter(e => e.kind === "cross-volume");
  const outIntra = outgoing.filter(e => e.kind !== "cross-volume");

  function refLine(e, dir){
    const targetId = dir === "out" ? e.target : e.source;
    const t = DATA.nodes.find(x => x.id === targetId);
    const tStr = t ? `${t.volume} :: ${escapeHtml(t.bare_id || targetId)}` : escapeHtml(targetId);
    return `<li><a data-id="${escapeHtml(targetId)}">${tStr}</a></li>`;
  }

  el.innerHTML = `
    <h2><span class="badge" style="background:${colorOf(n)}">${n.volume}</span> ${escapeHtml(n.title || n.bare_id || n.id)} <span class="badge b-${status}">${status}</span></h2>
    <div class="label">${escapeHtml(n.type)} · <code>${escapeHtml(n.bare_id || n.id)}</code></div>
    <div class="where">
      ${n.chapter ? "📖 "+escapeHtml(n.chapter) : ""}
      ${n.section ? " · §"+escapeHtml(n.section) : ""}
      ${n.subsection ? " · "+escapeHtml(n.subsection) : ""}
      <br>📄 <code>${escapeHtml(n.file)}:${n.line}</code>
    </div>
    <div class="excerpt">${escapeHtml(n.excerpt || "")}</div>
    ${outCross.length ? `<h3>Cites (cross-volume) — ${outCross.length}</h3><ul class="refs">${outCross.map(e=>refLine(e,"out")).join("")}</ul>` : ""}
    ${outIntra.length ? `<h3>Cites (in-volume) — ${outIntra.length}</h3><ul class="refs">${outIntra.map(e=>refLine(e,"out")).join("")}</ul>` : ""}
    ${incCross.length ? `<h3>Cited by (cross-volume) — ${incCross.length}</h3><ul class="refs">${incCross.map(e=>refLine(e,"in")).join("")}</ul>` : ""}
    ${incIntra.length ? `<h3>Cited by (in-volume) — ${incIntra.length}</h3><ul class="refs">${incIntra.map(e=>refLine(e,"in")).join("")}</ul>` : ""}
  `;
  el.querySelectorAll("a[data-id]").forEach(a => a.addEventListener("click", e => select(e.target.dataset.id)));
  if (window.MathJax && window.MathJax.typesetPromise){
    window.MathJax.typesetPromise([el]).catch(e => console.warn("MathJax typeset error:", e));
  }
}

function escapeHtml(s){ if (s==null) return ""; return String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"})[c]); }
function cssEscape(s){ return String(s).replace(/[^a-zA-Z0-9_-]/g, c => "\\"+c); }

function apply(){
  if (cy){
    cy.batch(() => {
      for (const n of DATA.nodes){
        const ele = cy.getElementById(n.id);
        if (!ele.length) continue;
        if (passesNode(n)) ele.removeClass("faded"); else ele.addClass("faded");
      }
      for (const e of DATA.edges){
        const ele = cy.getElementById(e.source+"->"+e.target);
        if (!ele.length) continue;
        const kindOk = (e.kind === "cross-volume") ? state.filters.edges.cross : state.filters.edges.intra;
        const srcN = DATA.nodes.find(x=>x.id===e.source);
        const tgtN = DATA.nodes.find(x=>x.id===e.target);
        const endsOk = srcN && tgtN && passesNode(srcN) && passesNode(tgtN);
        if (kindOk && endsOk) ele.removeClass("faded"); else ele.addClass("faded");
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


def render_unified_html(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    meta = data["meta"]
    sc = ", ".join(f"{k}={v}" for k, v in sorted(meta.get("status_counts", {}).items(), key=lambda kv: -kv[1]))
    vc = ", ".join(f"{k}={v}" for k, v in sorted(meta.get("volume_counts", {}).items(), key=lambda kv: -kv[1]))
    meta_str = (
        f"{meta['total_nodes']} blocks · {meta['total_edges']} edges "
        f"({meta['intra_volume_edges']} intra, {meta['cross_volume_edges']} cross-volume, "
        f"{meta['dangling_refs']} dangling) · {meta['generated_at'][:19]}Z"
        + (f"<br><span style='font-size:0.72rem;'>volumes: {vc}</span>" if vc else "")
        + (f"<br><span style='font-size:0.72rem;'>status: {sc}</span>" if sc else "")
    )
    return (
        HTML_TEMPLATE
        .replace("__META__", meta_str)
        .replace("__PAYLOAD__", payload)
        .replace("__VOLUME_TITLES__", json.dumps(VOLUME_TITLES, ensure_ascii=False))
        .replace("__VOLUME_COLOR__", json.dumps(VOLUME_COLOR, ensure_ascii=False))
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--mathematics-dir", default=str(Path.home() / "mathematics"),
                    help="Mathematics dir (default: ~/mathematics)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    math_dir = Path(args.mathematics_dir).expanduser().resolve()
    arch_dir = math_dir / "architecture"
    arch_dir.mkdir(parents=True, exist_ok=True)

    volumes = load_volumes(arch_dir)
    if not args.quiet:
        print(f"  -- Cross-volume architecture aggregator --")
        print(f"  reading {arch_dir}/")
        for v, d in volumes.items():
            n = len(d.get("nodes", []))
            e = len(d.get("edges", []))
            print(f"    {v:>12s}  {n:>5d} nodes  {e:>5d} edges")
    if not volumes:
        print(f"  fail  no per-volume JSON in {arch_dir}/", file=sys.stderr)
        return 1

    merged = merge(volumes)

    json_out = math_dir / "architecture.json"
    json_out.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    html_out = math_dir / "architecture.html"
    html_out.write_text(render_unified_html(merged), encoding="utf-8")

    m = merged["meta"]
    if not args.quiet:
        print(f"  merged  {m['total_nodes']} nodes  {m['total_edges']} edges "
              f"({m['intra_volume_edges']} intra · {m['cross_volume_edges']} cross-volume · {m['dangling_refs']} dangling)")
        print(f"  ok  {json_out}")
        print(f"  ok  {html_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
