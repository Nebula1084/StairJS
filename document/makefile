#source
BASE_NAME ?= document
TARGET ?= $(BASE_NAME).pdf
PICTURE_DIRECTORY = pictures
PICTURES = \
	$(PICTURE_DIRECTORY)\AST.eps

#excutable
2EPS = bmeps
TEX = latex
DVI2PS = dvips
PS2PDF = ps2pdf

TARGET: $(TARGET)
	copy $(TARGET) ..\$(TARGET)

%.pdf: %.ps
	$(PS2PDF) $<

%.ps: %.dvi
	$(DVI2PS) $<

#cancel built in rule
%.dvi: %.tex 
%.dvi: %.tex pictures
	$(TEX) $<
	$(TEX) $<

%.eps: %.png
	$(2EPS) $< $@
%.eps: %.pgm
	$(2EPS) $< $@
%.eps: %.jpg
	$(2EPS) $< $@

.PHONY: clean pictures redo_pictures clean_pictures TARGET
.PRECIOUS: %.eps

clean:
	del $(BASE_NAME).ps $(BASE_NAME).dvi $(BASE_NAME).pdf 

clean_pictures:
	del $(PICTURES)

pictures: $(PICTURES)

redo_pictures:
	$(MAKE) clean_pictures
	$(MAKE) pictures