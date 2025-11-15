#!/usr/bin/env python3

"""Inkscape exporter configuration module"""

# Standard imports
from os import path
import sys
import tomllib
import logging

# Module logger
LOGGER = logging.getLogger(__name__)

class ExporterConfig():
    """Configuration for an Exporter

    This class can be configured from command-line or a sidecar TOML file on-disk
    The configuration is stored in single and common dictionary
    """

    # Constants ================================================================

    # Export all the area defining the page
    INKSCAPE_OPT_AREA = "--export-area-page"

    # Export in PDF rather than EPS
    INKSCAPE_OPT_TYPE = "--export-type=pdf"

    # Export with sidecar `pdf_tex` file such that LaTeX will render fonts during compilation
    INKSCAPE_OPT_FONTS_LATEX = "--export-latex"

    # Export in current working directory by default
    OUTPUT_DIR_DEFAULT = "."

    # Templates for output file based on exportation mode
    OUTPUT_FILE_FULL_TEMPLATE = "{}.pdf"
    OUTPUT_FILE_FRAGMENTS_TEMPLATE = "{}@{}.pdf"

    # Default which fonts engine will do font rendering ["inkscape" | "latex"]
    FONTS_ENGINE_DEFAULT = "inkscape"

    # Default exportation mode (False = Full, True = Fragments) [bool]
    FRAGMENTS_DEFAULT = False

    # Runtime variables ========================================================

    # Input SVG file to export [string]
    input_file = None
  
    # Basename of input file (without leading directories and extension) [string]
    input_file_basename = None

    # Output directory for exportation [string]
    output_dir = OUTPUT_DIR_DEFAULT

    # Common dictionary to command-line and TOML file
    config_dict = {
        "params": {
            "fonts_engine": FONTS_ENGINE_DEFAULT,
            "fragments": FRAGMENTS_DEFAULT,
        },
        # Series of fragments exportation. Scheme:
        # [{"name": "NAME", "excluded_layers": ["step1", "step3", "step3"]}]
        "fragments": None,
    }

    # Functions ================================================================

    @staticmethod
    def generate_toml_template(input_file):
        """Generate a template TOML configuration file for a given input file"""
        # Define output file and template to write into
        output_file = input_file.replace(".svg", ".toml")

        # Define template to write into output file
        template = '[params]\n' \
            + '# Set the font rendering engine ["latex" | "inkscape"]\n' \
            + 'fonts_engine = "inkscape"\n' \
            + '# Enable or disable fragments exportation [false | true]\n' \
            + 'fragments = false\n' \
            + '\n' \
            + '# Define the fragment exportation NAME1\n' \
            + '[fragments.NAME1]\n' \
            + 'excluded_layers = ["LAYER1", "LAYER2"]\n' \
            + '\n' \
            + '# Define the fragment exportation NAME2\n' \
            + '[fragments.NAME2]\n' \
            + 'excluded_layers = ["LAYER2", "LAYER3"]'

        # Perform the writing
        LOGGER.info("Generate template TOML configuration file: {}".format(output_file))
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(template)

    # Methods ==================================================================

    def __init__(self, input_file):
        """Initialize an exporter configuration with an input file and default values"""
        # Get an input file
        self.input_file = input_file
        # Derive basename
        self.input_file_basename = path.splitext(path.basename(self.input_file))[0]

    def load_toml(self):
        """Load configuration from a sidecar TOML file

        If no TOML configuration is found, silently return.
        """
        config_file_name = self.input_file.replace(".svg", ".toml")
        # If found a corresponding TOML file...
        if path.exists(config_file_name):
            LOGGER.debug("Loading configuration from: {}".format(config_file_name))
            with open(config_file_name, "rb") as f:
                # Load it and update our object configuration dictionary
                # from the TOML configuration
                self.config_dict.update(tomllib.load(f))

    def load_args(self, output_dir=None, fonts_engine=None, fragments=None):
        """Load configuration from method arguments (typically, command-line arguments)

        Purpose is to configure manually for testing purpose or overriding after loading from a TOML file.
        """
        LOGGER.debug("Loading configuration from: {}".format(sys.argv))
        if output_dir is not None:
            self.output_dir = output_dir
        if fonts_engine is not None:
            self.config_dict["params"]["fonts_engine"] = fonts_engine
        if fragments is not None:
            self.config_dict["params"]["fragments"] = fragments

    def __str__(self):
        """Return a textual representation of the current configuration"""
        return "\n[v] input_file={}\n[v] output_dir={}\n[v] config_dict={}".format(
            self.input_file,
            self.output_dir,
            self.config_dict
        )
