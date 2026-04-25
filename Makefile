# ============================================================================
#  Makefile -- Igusa cusp form paper
# ============================================================================
#
#  Usage:
#    make            Full paper build -> out/main.pdf
#    make fast       Single pdflatex pass -> out/main.pdf
#    make release    Full rebuild -> out/main.pdf + standalones + iCloud
#    make standalone Build standalone documents -> out/
#    make icloud     Copy latest PDFs to iCloud Drive
#    make clean      Remove LaTeX build debris
#    make veryclean  Remove build debris; preserve tracked out/main.pdf
#    make help       Show available targets
#
# ============================================================================

SHELL := /bin/zsh

MAIN      := main
BIB       := proj
TEX       := pdflatex
BIBTEX    := bibtex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0
LOG_DIR   := .build_logs
OUT_DIR   := out
PDF       := $(OUT_DIR)/$(MAIN).pdf
PASSES    := 4
TEX_SOURCES := $(MAIN).tex $(wildcard appendices/*.tex)

ICLOUD_DIR := /Users/raeez/Library/Mobile Documents/com~apple~CloudDocs/research

STANDALONE_TEX := $(wildcard standalone/*.tex)
STANDALONE_PDFS := $(patsubst standalone/%.tex,$(OUT_DIR)/%.pdf,$(STANDALONE_TEX))
STANDALONE_PASSES := 3

AUX_EXTS := aux bbl blg idx ilg ind log out toc synctex.gz fdb_latexmk fls

.DEFAULT_GOAL := all

.PHONY: all fast release standalone icloud view watch clean veryclean count help

all: $(PDF)

$(PDF): $(TEX_SOURCES) $(BIB).bib Makefile
	@echo "  -- Building $(MAIN).tex -> $(PDF) --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-pass1.log 2>&1 || { \
		echo "  fail  pdflatex pass 1 failed. See $(LOG_DIR)/$(MAIN)-pass1.log"; \
		tail -n 40 $(LOG_DIR)/$(MAIN)-pass1.log; \
		exit 1; \
	}
	@cd $(OUT_DIR) && BIBINPUTS="..:$$BIBINPUTS" BSTINPUTS="..:$$BSTINPUTS" $(BIBTEX) $(MAIN) >../$(LOG_DIR)/$(MAIN)-bibtex.log 2>&1 || { \
		echo "  fail  bibtex failed. See $(LOG_DIR)/$(MAIN)-bibtex.log"; \
		tail -n 40 $(LOG_DIR)/$(MAIN)-bibtex.log; \
		exit 1; \
	}
	@for pass in $$(seq 2 $(PASSES)); do \
		$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-pass$$pass.log 2>&1 || { \
			echo "  fail  pdflatex pass $$pass failed. See $(LOG_DIR)/$(MAIN)-pass$$pass.log"; \
			tail -n 40 $(LOG_DIR)/$(MAIN)-pass$$pass.log; \
			exit 1; \
		}; \
		if [ -f $(OUT_DIR)/$(MAIN).idx ]; then makeindex -q $(OUT_DIR)/$(MAIN).idx >/dev/null 2>&1 || true; fi; \
	done
	@echo "  ok  $(PDF)"

fast:
	@echo "  -- Fast build --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) -output-directory=$(OUT_DIR) $(MAIN).tex >$(LOG_DIR)/$(MAIN)-fast.log 2>&1 || { \
		echo "  fail  Fast build failed. See $(LOG_DIR)/$(MAIN)-fast.log"; \
		tail -n 40 $(LOG_DIR)/$(MAIN)-fast.log; \
		exit 1; \
	}
	@echo "  ok  $(PDF)"

release:
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@echo ""
	@echo "  =========================================="
	@echo "  -- RELEASE BUILD (Igusa cusp form) --"
	@echo "  =========================================="
	@echo ""
	@echo "  [1/2] Paper"
	@$(MAKE) --no-print-directory -B $(PDF)
	@echo ""
	@echo "  [2/2] Standalone documents and iCloud"
	@$(MAKE) --no-print-directory icloud
	@echo ""
	@echo "  =========================================="
	@echo "  Release complete. Canonical output:"
	@echo "    $(PDF)"
	@if [ -n "$(strip $(STANDALONE_TEX))" ]; then \
		echo "  Standalone output:"; \
		for pdf in $(STANDALONE_PDFS); do \
			if [ -f "$$pdf" ]; then echo "    $$pdf"; fi; \
		done; \
	fi
	@echo "  =========================================="

standalone:
	@echo "  -- Building standalone documents --"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@if [ -z "$(strip $(STANDALONE_TEX))" ]; then \
		echo "  (no standalone documents found)"; \
	else \
		failures=0; \
		for tex in $(STANDALONE_TEX); do \
			if [ ! -f "$$tex" ]; then continue; fi; \
			base=$$(basename "$$tex" .tex); \
			if [ -f "$(OUT_DIR)/$$base.pdf" ] && [ "$(OUT_DIR)/$$base.pdf" -nt "$$tex" ]; then \
				echo "  ok  $(OUT_DIR)/$$base.pdf (up to date)"; \
				continue; \
			fi; \
			tmpdir=$$(mktemp -d "/tmp/mkd-$$(basename "$$(pwd)")-standalone-$$base.XXXXXX"); \
			echo "  [standalone] $$tex -> $(OUT_DIR)/$$base.pdf"; \
			for pass in $$(seq 1 $(STANDALONE_PASSES)); do \
				TEXINPUTS="$$tmpdir:$$(pwd):$$(pwd)/standalone:" $(TEX) $(TEXFLAGS) -output-directory="$$tmpdir" "$$tex" >"$(LOG_DIR)/standalone-$$base-pass$$pass.log" 2>&1; rc=$$?; \
				if [ -f "$$tmpdir/$$base.idx" ]; then makeindex -q "$$tmpdir/$$base.idx" >/dev/null 2>&1 || true; fi; \
				if [ $$rc -ne 0 ]; then \
					if grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOG_DIR)/standalone-$$base-pass$$pass.log" >/dev/null 2>&1; then \
						echo "  fail  $$tex failed on pass $$pass. See $(LOG_DIR)/standalone-$$base-pass$$pass.log"; \
						grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' "$(LOG_DIR)/standalone-$$base-pass$$pass.log" | head -n 20 || tail -n 40 "$(LOG_DIR)/standalone-$$base-pass$$pass.log"; \
						failures=$$((failures + 1)); \
						break; \
					else \
						echo "  warn  $$tex returned $$rc on pass $$pass; continuing."; \
					fi; \
				fi; \
			done; \
			if [ -f "$$tmpdir/$$base.pdf" ]; then \
				cp "$$tmpdir/$$base.pdf" "$(OUT_DIR)/$$base.pdf"; \
				echo "  ok  $(OUT_DIR)/$$base.pdf"; \
			elif [ $$failures -eq 0 ]; then \
				echo "  fail  no PDF produced for $$tex"; \
				failures=$$((failures + 1)); \
			fi; \
		done; \
		if [ $$failures -ne 0 ]; then \
			echo "  fail  $$failures standalone document(s) failed."; \
			exit 1; \
		fi; \
	fi

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
	@echo "  out/main.pdf is tracked; veryclean preserves $(OUT_DIR)."
	@echo "  ok  Clean."

count:
	@echo ""
	@echo "  -- Igusa paper statistics --"
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './out/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:    %s\n" "$$(find . -name '*.tex' -not -path './out/*' -exec cat {} + | wc -l | tr -d ' ')"
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
	@echo "  make release    Full rebuild -> out/main.pdf + standalones + iCloud"
	@echo "  make standalone Build standalone documents -> out/"
	@echo "  make icloud     Copy latest PDFs to iCloud Drive"
	@echo "  make clean      Remove build debris"
	@echo "  make veryclean  Remove build debris; preserve tracked out/main.pdf"
	@echo "  make count      Paper statistics"
	@echo "  make help       This message"
	@echo ""
