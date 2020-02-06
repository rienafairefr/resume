.PHONY: all clean

matthieu.berthome.resume.fr.text.pdf: resume.tex Makefile
	sed 's/\\entrue/\\frtrue/g' resume.tex | pdflatex -halt-on-error -jobname=matthieu.berthome.resume.fr.text

matthieu.berthome.resume.en.text.pdf: resume.tex Makefile
	sed 's/\\frtrue/\\entrue/g' resume.tex | pdflatex -halt-on-error -jobname=matthieu.berthome.resume.en.text

matthieu.berthome.resume.%.pdf: matthieu.berthome.resume.%.text.pdf Makefile
	gs -o matthieu.berthome.resume.$*.pdf -dNoOutputFonts -sDEVICE=pdfwrite matthieu.berthome.resume.$*.text.pdf

matthieu.berthome.resume.en-fr.pdf: matthieu.berthome.resume.en.pdf matthieu.berthome.resume.fr.pdf Makefile
	pdfnup --nup 2x1 -o matthieu.berthome.resume.en-fr.pdf matthieu.berthome.resume.en.pdf matthieu.berthome.resume.fr.pdf

all: matthieu.berthome.resume.en-fr.pdf Makefile

clean:
	rm matthieu.berthome.resume.*
	
