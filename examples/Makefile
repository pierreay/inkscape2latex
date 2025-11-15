# Source files
SRC_FILES := $(shell find . -type f -name '*.svg')

# Configuration files
CONFIG_FILES := $(patsubst ./%.svg,./%.toml,$(SRC_FILES))

# Output filetype
BUILD_FT := pdf

# Output directory
BUILD_DIR := build

# Exported files (do not contains fragments)
BUILD_FILES := $(patsubst ./%.svg,$(BUILD_DIR)/%.$(BUILD_FT),$(SRC_FILES))

all: $(CONFIG_FILES) $(BUILD_FILES)

# .svg -> {.pdf, .pdf_tex}
$(BUILD_DIR)/%.$(BUILD_FT): %.svg %.toml
	scapex -o $(BUILD_DIR) $<
	touch $@

# Create the build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Generate a default configuration file if not existing
%.toml:
	scapex --generate $(patsubst %.toml,%.svg,$@)

clean:
	rm -f $(BUILD_FILES) \
		$(patsubst %.pdf,%@*.pdf,$(BUILD_FILES)) \
		$(patsubst %.pdf,%.pdf_tex,$(BUILD_FILES)) \
		$(patsubst %.pdf,%@.pdf_tex,$(BUILD_FILES))
	test $(BUILD_DIR) != "." -a -d $(BUILD_DIR) && rmdir $(BUILD_DIR) || true

printenv:
	@echo SRC_FILES=$(SRC_FILES)
	@echo BUILD_FT=$(BUILD_FT)
	@echo BUILD_DIR=$(BUILD_DIR)
	@echo BUILD_FILES=$(BUILD_FILES)
