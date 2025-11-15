# Program: scapex
# Author: Pierre Ayoub
# Date: 2025-09-19

# Source files
INKSCAPE_SRC_FILES := $(shell find . -type f -name '*.svg')

# Configuration files
INKSCAPE_CONFIG_FILES := $(patsubst ./%.svg,./%.toml,$(INKSCAPE_SRC_FILES))

# Output filetype
INKSCAPE_BUILD_FT := pdf

# Output directory
INKSCAPE_BUILD_DIR := build

# Exported files (do not contains fragments)
INKSCAPE_BUILD_FILES := $(patsubst ./%.svg,$(INKSCAPE_BUILD_DIR)/%.$(INKSCAPE_BUILD_FT),$(INKSCAPE_SRC_FILES))

all: $(INKSCAPE_CONFIG_FILES) $(INKSCAPE_BUILD_FILES)

# .svg -> {.pdf, .pdf_tex}
$(INKSCAPE_BUILD_DIR)/%.$(INKSCAPE_BUILD_FT): %.svg
	scapex -o $(INKSCAPE_BUILD_DIR) $<
	touch $@

# Create the build directory
$(INKSCAPE_BUILD_DIR):
	mkdir -p $(INKSCAPE_BUILD_DIR)

# Generate a default configuration file if not existing
%.toml:
	scapex --generate $(patsubst %.toml,%.svg,$@)

clean:
	rm -f $(INKSCAPE_BUILD_FILES) \
		$(patsubst %.pdf,%@*.pdf,$(INKSCAPE_BUILD_FILES)) \
		$(patsubst %.pdf,%.pdf_tex,$(INKSCAPE_BUILD_FILES)) \
		$(patsubst %.pdf,%@.pdf_tex,$(INKSCAPE_BUILD_FILES))
	test $(INKSCAPE_BUILD_DIR) != "." -a -d $(INKSCAPE_BUILD_DIR) && rmdir $(INKSCAPE_BUILD_DIR) || true

printenv:
	@echo INKSCAPE_SRC_FILES=$(INKSCAPE_SRC_FILES)
	@echo INKSCAPE_BUILD_FT=$(INKSCAPE_BUILD_FT)
	@echo INKSCAPE_BUILD_DIR=$(INKSCAPE_BUILD_DIR)
	@echo INKSCAPE_BUILD_FILES=$(INKSCAPE_BUILD_FILES)
