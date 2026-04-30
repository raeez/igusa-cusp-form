# A095 session-end build and bibliography audit

No tracked files edited by the agent.

## Command sequence

Run from `/Users/raeez/igusa-cusp-form`:

```zsh
perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){print "$1\n"}' main.tex | sort | uniq -d

comm -23 \
  <(perl -0777 -ne 'while(/\\(?:eqref|ref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){print "$1\n"}' main.tex | sort -u) \
  <(perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){print "$1\n"}' main.tex | sort -u)

perl -ne 'print "$1\n" if /^\s*@\w+\s*\{\s*([^,\s]+)/' proj.bib | sort | uniq -d

comm -23 \
  <(perl -0777 -ne 'while(/\\(?:cite|cites|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){print "$_\n" for grep length, map { s/^\s+|\s+$//gr } split /,/, $1}' main.tex | sort -u) \
  <(perl -ne 'print "$1\n" if /^\s*@\w+\s*\{\s*([^,\s]+)/' proj.bib | sort -u)

python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
make -B
rg -n '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' .build_logs/main-pass*.log
rg -n 'Citation .*undefined|Reference .*undefined|There were undefined|multiply-defined|Label\(s\) may have changed|Warning--' .build_logs/main-pass4.log .build_logs/main-bibtex.log out/main.blg
rg -n 'Overfull \\hbox' .build_logs/main-pass4.log
```

Expected static diagnostics at the time of audit: no duplicate labels, no
undefined refs/cites, no duplicate BibTeX keys. Known unused bib keys:
`ConnesNCG`, `EOT`, `Evd80`, `Gritsenko2018Reflective`, `II10`,
`Ich05`, `KNAPP:1`, `LurieHA`, `Niemann03`, `Schlichting2010`.

The agent reported that a temporary full build against the then-current
files passed with a 234-page PDF and no fatal/undefined scans. Existing
recognition overfulls were small layout warnings near the first-window
and provenance region.

