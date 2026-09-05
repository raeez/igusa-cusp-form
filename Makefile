# ============================================================================
#  Makefile -- Igusa cusp form paper
# ============================================================================
#
#  Usage:
#    make            Full paper build -> out/main.pdf
#    make fast       Single pdflatex pass -> out/main.pdf
#    make release    Full rebuild -> out/main.pdf + release PDF + standalones + iCloud
#    make standalone Build standalone documents -> out/
#    make icloud     Copy latest PDFs to iCloud Drive
#    make clean      Remove LaTeX build debris
#    make veryclean  Remove build debris and untracked generated PDFs
#    make help       Show available targets
#
# ============================================================================

SHELL := /bin/zsh

MAIN      := main
BIB       := proj
TEX       := pdflatex
BIBTEX    := bibtex
MAKEINDEX := makeindex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0
LOG_DIR   := .build_logs
OUT_DIR   := out
PDF       := $(OUT_DIR)/$(MAIN).pdf
RELEASE_PDF := raeez.lorgat.automorphic-corrections.pdf
PASSES    := 4

# Mathematics publish dir -- release binary copied here under canonical name
MATHEMATICS_DIR := $(HOME)/mathematics
PUBLISHED_PDF   := raeez.lorgat.automorphic-corrections.pdf
VOLUME_KEY      := igusa
PYTHON_BIN      ?= python3
TEX_SOURCES := $(MAIN).tex $(wildcard appendices/*.tex)

ICLOUD_DIR := /Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

STANDALONE_TEX := $(wildcard standalone/*.tex)
STANDALONE_PDFS := $(patsubst standalone/%.tex,$(OUT_DIR)/%.pdf,$(STANDALONE_TEX))
STANDALONE_PASSES := 3

AUX_EXTS := aux bbl blg idx ilg ind log out toc synctex.gz fdb_latexmk fls

# Genuine-arithmetic verifiers (exact, bounded expansion boxes; each
# prints a *_VERIFIED status and exits nonzero on any mismatch).
VERIFY_SCRIPTS := \
	compute/verify_square_root.py \
	compute/verify_lattice.py \
	compute/verify_jacobi_window_fixture.py \
	compute/verify_theta_normalization_fixture.py \
	compute/verify_theta_product_identity.py \
	compute/verify_bkm_kappa_ladder.py

.DEFAULT_GOAL := platonic

.PHONY: platonic all fast release standalone icloud view watch clean veryclean count help mathematics-publish root-publish architecture unified-architecture verify

all: $(PDF)

$(PDF): $(TEX_SOURCES) $(BIB).bib Makefile
	@echo "  -- Building $(MAIN).tex -> $(PDF) --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@rm -f $(PDF)
	@$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-pass1.log 2>&1; \
		tex_status=$$?; \
	if [ $$tex_status -ne 0 ] || [ ! -f $(PDF) ] || grep -qE '^!|^Fatal error|^.+Emergency stop|^!.*No pages of output' $(LOG_DIR)/$(MAIN)-pass1.log; then \
		echo "  fail  pdflatex pass 1 failed (exit $$tex_status, no PDF, or fatal error). See $(LOG_DIR)/$(MAIN)-pass1.log"; \
		tail -n 40 $(LOG_DIR)/$(MAIN)-pass1.log; \
		rm -f $(PDF); \
		exit 1; \
	fi
	@if ! (cd "$(OUT_DIR)" && BIBINPUTS="$(CURDIR):$$BIBINPUTS" BSTINPUTS="$(CURDIR):$$BSTINPUTS" $(BIBTEX) $(MAIN)) >"$(abspath $(LOG_DIR))/$(MAIN)-bibtex.log" 2>&1; then \
		echo "  fail  bibtex failed."; \
		tail -n 40 "$(LOG_DIR)/$(MAIN)-bibtex.log"; \
		rm -f $(PDF); exit 1; \
	fi
	@if grep -qE '^I couldn|^I found no|^Fatal error|^.+Emergency stop' $(LOG_DIR)/$(MAIN)-bibtex.log; then \
		echo "  fail  bibtex reported issues. See $(LOG_DIR)/$(MAIN)-bibtex.log"; \
		tail -n 20 $(LOG_DIR)/$(MAIN)-bibtex.log; \
		rm -f $(PDF); exit 1; \
	fi
	@for pass in $$(seq 2 $(PASSES)); do \
		rm -f $(PDF); \
		$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-pass$$pass.log 2>&1; \
		tex_status=$$?; \
		if [ $$tex_status -ne 0 ] || [ ! -f $(PDF) ] || grep -qE '^!|^Fatal error|^.+Emergency stop|^!.*No pages of output' $(LOG_DIR)/$(MAIN)-pass$$pass.log; then \
			echo "  fail  pdflatex pass $$pass failed (exit $$tex_status, no PDF, or fatal error). See $(LOG_DIR)/$(MAIN)-pass$$pass.log"; \
			tail -n 40 $(LOG_DIR)/$(MAIN)-pass$$pass.log; \
			rm -f $(PDF); \
			exit 1; \
		fi; \
		if [ -f $(OUT_DIR)/$(MAIN).idx ]; then \
			$(MAKEINDEX) -q $(OUT_DIR)/$(MAIN).idx >$(LOG_DIR)/$(MAIN)-index-pass$$pass.log 2>&1; index_status=$$?; \
			if [ $$index_status -ne 0 ]; then \
				tail -n 40 $(LOG_DIR)/$(MAIN)-index-pass$$pass.log; rm -f $(PDF); exit 1; \
			fi; \
		fi; \
	done
	@echo "  ok  $(PDF)"

fast:
	@echo "  -- Fast build --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@rm -f $(PDF)
	@$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-fast.log 2>&1; \
		tex_status=$$?; \
	if [ $$tex_status -ne 0 ] || [ ! -f $(PDF) ] || grep -qE '^!|^Fatal error|^.+Emergency stop' $(LOG_DIR)/$(MAIN)-fast.log; then \
		echo "  fail  Fast build failed (exit $$tex_status, no PDF, or fatal error). See $(LOG_DIR)/$(MAIN)-fast.log"; \
		tail -n 40 $(LOG_DIR)/$(MAIN)-fast.log; \
		rm -f $(PDF); \
		exit 1; \
	fi; \
	echo "  ok  $(PDF)"

release:
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@echo ""
	@echo "  =========================================="
	@echo "  -- RELEASE BUILD (Igusa cusp form) --"
	@echo "  =========================================="
	@echo ""
	@echo "  [1/3] Paper"
	@$(MAKE) --no-print-directory -B $(PDF)
	@echo ""
	@echo "  [2/3] Release PDF"
	@cp $(PDF) "$(RELEASE_PDF)"
	@echo "    ok  $(RELEASE_PDF)"
	@echo ""
	@echo "  [3/6] Standalone documents and iCloud"
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  [4/6] Publish to repo root (canonical PDF name)"
	@$(MAKE) --no-print-directory root-publish
	@echo ""
	@echo "  [5/6] Publish to ~/mathematics + per-volume architecture"
	@$(MAKE) --no-print-directory mathematics-publish
	@$(MAKE) --no-print-directory architecture
	@echo ""
	@echo "  [6/6] Cross-volume architecture aggregation"
	@$(MAKE) --no-print-directory unified-architecture
	@echo ""
	@echo "  =========================================="
	@echo "  Release complete. Canonical output:"
	@echo "    $(PDF)"
	@echo "    $(RELEASE_PDF)"
	@echo "    $(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"
	@if [ -n "$(strip $(STANDALONE_TEX))" ]; then \
		echo "  Standalone output:"; \
		for pdf in $(STANDALONE_PDFS); do \
			if [ -f "$$pdf" ]; then echo "    $$pdf"; fi; \
		done; \
	fi
	@echo "  =========================================="

## platonic: Build the platonic-integrated monograph → out/platonic.pdf
##   THE mathematically current root for this repository: platonic/main.tex,
##   the shared five-volume spine (Volume I-V) plus this repository's own
##   opening and closing chapters, set in EB Garamond via raeez-math-template.
##   See platonic/PLATONIC_LEDGER.md.
platonic:
	@echo "  -- Building the platonic-integrated monograph --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@rm -f $(OUT_DIR)/platonic.pdf
	@set -e; \
	build_dir=$$(mktemp -d "$(abspath $(OUT_DIR))/platonic.XXXXXX"); \
	log_dir="$(abspath $(LOG_DIR))"; source_dir="$(CURDIR)"; \
	cd platonic; \
	for pass in $$(seq 1 $(PASSES)); do \
		rm -f "$$build_dir/main.pdf"; \
		if ! TEXINPUTS=".:..:$$TEXINPUTS" BIBINPUTS=".:..:$$BIBINPUTS" \
			$(TEX) $(TEXFLAGS) -output-directory="$$build_dir" main.tex >"$$log_dir/platonic-pass$$pass.log" 2>&1; then \
			tail -n 40 "$$log_dir/platonic-pass$$pass.log"; exit 1; \
		fi; \
		if [ ! -s "$$build_dir/main.pdf" ] || grep -aEq '^!|Fatal error|Emergency stop|No pages of output' "$$log_dir/platonic-pass$$pass.log"; then \
			tail -n 40 "$$log_dir/platonic-pass$$pass.log"; exit 1; \
		fi; \
		if [ "$$pass" -eq 1 ]; then \
			if ! (cd "$$build_dir" && BIBINPUTS="$$source_dir/platonic:$$source_dir:$$BIBINPUTS" BSTINPUTS="$$source_dir/platonic:$$source_dir:$$BSTINPUTS" $(BIBTEX) main) >"$$log_dir/platonic-bibtex.log" 2>&1; then \
				tail -n 40 "$$log_dir/platonic-bibtex.log"; exit 1; \
			fi; \
			if grep -aEq '^I couldn|^I found no|^Fatal error|Emergency stop' "$$log_dir/platonic-bibtex.log"; then \
				tail -n 40 "$$log_dir/platonic-bibtex.log"; exit 1; \
			fi; \
		fi; \
	done; \
	if grep -aEq 'Reference .* undefined|Citation .* undefined' "$$log_dir/platonic-pass$(PASSES).log"; then \
		tail -n 40 "$$log_dir/platonic-pass$(PASSES).log"; exit 1; \
	fi; \
	cp "$$build_dir/main.pdf" "$(abspath $(OUT_DIR))/platonic.pdf"; \
	echo "  ok  $(OUT_DIR)/platonic.pdf"


## root-publish: Copy the release binary to repo root under its canonical name
root-publish:
	@if [ -f "$(PDF)" ]; then \
		cp "$(PDF)" "$(PUBLISHED_PDF)"; \
		echo "    ok  $(PUBLISHED_PDF) (in repo root)"; \
	else \
		echo "    fail  $(PDF) missing -- skipping root publish"; \
	fi

## mathematics-publish: Copy the release binary to ~/mathematics under its canonical name
mathematics-publish:
	@mkdir -p "$(MATHEMATICS_DIR)"
	@if [ -f "$(PDF)" ]; then \
		cp "$(PDF)" "$(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
		echo "    ok  $(MATHEMATICS_DIR)/$(PUBLISHED_PDF)"; \
	else \
		echo "    fail  $(PDF) missing -- skipping ~/mathematics publish"; \
	fi

## architecture: Build interactive HTML + JSON of the manuscript architecture
architecture:
	@$(PYTHON_BIN) scripts/build_architecture.py --root . --volume $(VOLUME_KEY) --out $(OUT_DIR) --quiet
	@mkdir -p "$(MATHEMATICS_DIR)/architecture"
	@cp "$(OUT_DIR)/architecture.json" "$(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"
	@echo "    ok  $(OUT_DIR)/architecture.html + .json"
	@echo "    ok  $(MATHEMATICS_DIR)/architecture/$(VOLUME_KEY).json"

## unified-architecture: Aggregate all per-volume architecture.json into the cross-volume HTML+JSON
unified-architecture:
	@$(PYTHON_BIN) scripts/build_unified_architecture.py --mathematics-dir "$(MATHEMATICS_DIR)" --quiet
	@echo "    ok  $(MATHEMATICS_DIR)/architecture.html + .json"

standalone:
	@echo "  -- Building standalone documents --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@set -e; \
	for tex in $(STANDALONE_TEX); do \
		base=$$(basename "$$tex" .tex); \
		tmpdir=$$(mktemp -d "$(abspath $(OUT_DIR))/standalone-$$base.XXXXXX"); \
		rm -f "$(OUT_DIR)/$$base.pdf"; \
		for pass in $$(seq 1 $(STANDALONE_PASSES)); do \
			rm -f "$$tmpdir/$$base.pdf"; \
			if ! TEXINPUTS="$$tmpdir:$$(pwd):$$(pwd)/standalone:" $(TEX) $(TEXFLAGS) -output-directory="$$tmpdir" "$$tex" >"$(LOG_DIR)/standalone-$$base-pass$$pass.log" 2>&1; then \
				tail -n 40 "$(LOG_DIR)/standalone-$$base-pass$$pass.log"; exit 1; \
			fi; \
			if [ ! -s "$$tmpdir/$$base.pdf" ] || grep -aEq '^!|Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOG_DIR)/standalone-$$base-pass$$pass.log"; then \
				tail -n 40 "$(LOG_DIR)/standalone-$$base-pass$$pass.log"; exit 1; \
			fi; \
			if [ -f "$$tmpdir/$$base.idx" ]; then \
				if ! $(MAKEINDEX) -q "$$tmpdir/$$base.idx" >"$(LOG_DIR)/standalone-$$base-index-pass$$pass.log" 2>&1; then \
					tail -n 40 "$(LOG_DIR)/standalone-$$base-index-pass$$pass.log"; exit 1; \
				fi; \
			fi; \
		done; \
		if grep -aEq 'Reference .* undefined|Citation .* undefined' "$(LOG_DIR)/standalone-$$base-pass$(STANDALONE_PASSES).log"; then \
			tail -n 40 "$(LOG_DIR)/standalone-$$base-pass$(STANDALONE_PASSES).log"; exit 1; \
		fi; \
		cp "$$tmpdir/$$base.pdf" "$(OUT_DIR)/$$base.pdf"; \
		echo "  ok  $(OUT_DIR)/$$base.pdf"; \
	done

icloud: $(PDF) standalone
	@echo "  -- Copying Igusa PDFs to iCloud --"
	@mkdir -p "$(ICLOUD_DIR)/modular_forms"
	@cp $(PDF) "$(ICLOUD_DIR)/modular_forms/$(MAIN).pdf"
	@echo "    ok  modular_forms/$(MAIN).pdf"
	@cp $(PDF) "$(ICLOUD_DIR)/modular_forms/igusa_cusp_form.pdf"
	@echo "    ok  modular_forms/igusa_cusp_form.pdf"
	@if [ -n "$(strip $(STANDALONE_TEX))" ]; then \
		for pdf in $(STANDALONE_PDFS); do \
			if [ ! -f "$$pdf" ]; then continue; fi; \
			name=$$(basename "$$pdf"); \
			cp "$$pdf" "$(ICLOUD_DIR)/modular_forms/$$name"; \
			echo "    ok  modular_forms/$$name"; \
		done; \
	fi
	@echo "  Igusa PDFs copied to iCloud."

view:
	open $(PDF)

watch:
	@while true; do sleep 2; $(MAKE) --no-print-directory fast; done

clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext $(OUT_DIR)/$(MAIN).$$ext; \
	done
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ok  Clean."

veryclean: clean
	@echo "  Removing generated PDFs..."
	@rm -f $(MAIN).pdf $(BIB).pdf $(OUT_DIR)/$(BIB).pdf $(STANDALONE_PDFS)
	@rmdir $(OUT_DIR) 2>/dev/null || true
	@echo "  ok  Clean."

## verify: Run the genuine-arithmetic verifiers; fails on any mismatch
verify:
	@echo "  -- Running genuine-arithmetic verifiers --"
	@failures=0; \
	for script in $(VERIFY_SCRIPTS); do \
		printf "  [verify] %-52s " "$$script"; \
		if output=$$($(PYTHON_BIN) "$$script" 2>&1); then \
			echo "ok  $$(echo "$$output" | tail -n 1)"; \
		else \
			echo "FAIL"; \
			echo "$$output" | tail -n 20; \
			failures=$$((failures + 1)); \
		fi; \
	done; \
	if [ $$failures -ne 0 ]; then \
		echo "  fail  $$failures verifier(s) failed."; \
		exit 1; \
	fi; \
	echo "  ok  All verifiers passed."

count:
	@echo ""
	@echo "  -- Igusa paper statistics --"
	@printf "  Active sources: %s .tex files\n" "$(words $(TEX_SOURCES))"
	@printf "  Active lines:   %s\n" "$$(cat $(TEX_SOURCES) | wc -l | tr -d ' ')"
	@printf "  Agent material: %s .tex files\n" "$$(find agent_material -name '*.tex' 2>/dev/null | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		printf "  PDF size:       %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:            (not yet built)"; \
	fi
	@echo ""

help:
	@echo ""
	@echo "  Igusa cusp form -- Build System"
	@echo "  --------------------------------"
	@echo "  make            Full paper build -> out/main.pdf"
	@echo "  make fast       Single pdflatex pass -> out/main.pdf"
	@echo "  make release    Full rebuild -> out/main.pdf + release PDF + standalones + iCloud"
	@echo "  make standalone Build standalone documents -> out/"
	@echo "  make icloud     Copy latest PDFs to iCloud Drive"
	@echo "  make verify     Run the genuine-arithmetic verifiers (exact, fast)"
	@echo "  make clean      Remove build debris"
	@echo "  make veryclean  Remove build debris and untracked generated PDFs"
	@echo "  make count      Paper statistics"
	@echo "  make help       This message"
	@echo ""
