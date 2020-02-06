.PHONY: all clean

%.pdf: resume.tex Makefile

matthieu.berthome.resume.fr.text.pdf:
	sed 's/\\entrue/\\frtrue/g' resume.tex | pdflatex -jobname=matthieu.berthome.resume.fr.text

matthieu.berthome.resume.en.text.pdf:
	sed 's/\\frtrue/\\entrue/g' resume.tex | pdflatex -jobname=matthieu.berthome.resume.en.text

matthieu.berthome.resume.%.pdf: matthieu.berthome.resume.%.text.pdf
	gs -o matthieu.berthome.resume.$*.pdf -dNoOutputFonts -sDEVICE=pdfwrite matthieu.berthome.resume.$*.text.pdf
	
all: matthieu.berthome.resume.fr.pdf matthieu.berthome.resume.en.pdf

clean:
	rm matthieu.berthome.resume.*
	
