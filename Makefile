SOURCE=proj  # set the path to your TeX file here
SHELL=/bin/zsh   # for the while loop below

all:  ## Compile paper
	pdflatex $(SOURCE)

full:  ## Compile everything
	pdflatex $(SOURCE).tex
	pdflatex $(SOURCE).tex
	bibtex $(SOURCE)
	pdflatex $(SOURCE).tex

clean:  ## Clean output files
	rubber --clean $(SOURCE).tex

watch:  ## Recompile on updates to the source file
	@while [ 1 ]; do; inotifywait $(PAPER); sleep 0.01; make all; done
	# for Bash users, replace the while loop with the following
	# @while true; do; inotifywait $(PAPER); sleep 0.01; make all; done
