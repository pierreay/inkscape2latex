# Variables
# ==============================================================================

# Source files directory (current directory = .)
SRC_DIR := ../doc

# Source files (SVGs)
SRC_FILES := $(shell find $(SRC_DIR) -type f -name '*.svg')

# Configuration files (TOMLs)
CONFIG_FILES := $(patsubst $(SRC_DIR)/%.svg,$(SRC_DIR)/%.toml,$(SRC_FILES))

# Output directory
BUILD_DIR := build

# Output filetype (PDF)
BUILD_FT := pdf

# Output files (do not contains fragments) (PDFs)
BUILD_FILES := $(patsubst $(SRC_DIR)/%.svg,$(BUILD_DIR)/%.$(BUILD_FT),$(SRC_FILES))

# Goals
# ==============================================================================

all: $(BUILD_FILES)

clean:
	rm -f $(BUILD_FILES) \
		$(patsubst %.pdf,%@*.pdf,$(BUILD_FILES)) \
		$(patsubst %.pdf,%.pdf_tex,$(BUILD_FILES)) \
		$(patsubst %.pdf,%@.pdf_tex,$(BUILD_FILES))
	test $(BUILD_DIR) != "." -a -d $(BUILD_DIR) && rmdir $(BUILD_DIR) || true

printenv:
	@echo SRC_FILES=$(SRC_FILES)
	@echo CONFIG_FILES=$(CONFIG_FILES)
	@echo BUILD_FT=$(BUILD_FT)
	@echo BUILD_DIR=$(BUILD_DIR)
	@echo BUILD_FILES=$(BUILD_FILES)

# Targets
# ==============================================================================

# Create the build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Convert a SVG into a PDF or a set of PDFs (potentially with `.pdf_tex` sidecars)
$(BUILD_DIR)/%.$(BUILD_FT): $(SRC_DIR)/%.svg $(SRC_DIR)/%.toml | $(BUILD_DIR)
	scapex -o $(BUILD_DIR) $<
	touch $@

# Generate a default configuration file
%.toml:
	scapex --generate $(patsubst %.toml,%.svg,$@)
