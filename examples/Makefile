# Source files.
INKSCAPE_SRC_FILES := $(shell find . -type f -name '*.svg')

# Output filetype [pdf | eps].
INKSCAPE_BUILD_FT := pdf

# Suffix for files rendered using Inkscape fonts.
INKSCAPE_FONTS_SUFFIX := _inkscape-fonts

# Exported files (do not contains layered exportation).
INKSCAPE_BUILD_FILES := $(patsubst %.svg,%.$(INKSCAPE_BUILD_FT),$(INKSCAPE_SRC_FILES))

# Custom layers definitions.
INKSCAPE_LAYERS_PATH := layers.json

# Custom exporter script arguments.
INKSCAPE_SCRIPT_ARGS += -l $(INKSCAPE_LAYERS_PATH)

# .svg -> {INKSCAPE_FONTS_SUFFIX.pdf, .pdf, .pdf_tex}
%.$(INKSCAPE_BUILD_FT): %.svg
	inkscape2latex $(INKSCAPE_SCRIPT_ARGS) $< $@
	inkscape2latex $(INKSCAPE_SCRIPT_ARGS) --inkscape-fonts $< $(patsubst %.$(INKSCAPE_BUILD_FT),%$(INKSCAPE_FONTS_SUFFIX).$(INKSCAPE_BUILD_FT),$@)

all: $(INKSCAPE_BUILD_FILES)

clean:
	rm -f $(INKSCAPE_BUILD_FILES) \
		$(patsubst %.pdf,%-step*.pdf,$(INKSCAPE_BUILD_FILES)) \
		$(patsubst %.pdf,%*.pdf_tex,$(INKSCAPE_BUILD_FILES)) \
		$(patsubst %.pdf,%_inkscape-fonts*.pdf,$(INKSCAPE_BUILD_FILES))
