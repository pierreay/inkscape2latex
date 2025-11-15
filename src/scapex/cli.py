#!/usr/bin/env python3

"""Command-line interface module"""

# Standard imports
from os import path
import sys
import argparse
import logging

# Package module imports
from scapex import APPLOGGER
from scapex.config import ExporterConfig

# Module logger
LOGGER = logging.getLogger(__name__)

class CLI:
    """Command-line interface"""

    def __init__(self):
        """Initialize command-line interface and set log level"""

        # Setup command-line interface =========================================

        parser = argparse.ArgumentParser(
            prog='scapex',
            description='TODO'
        )

        parser.add_argument('FILE', help="Inkscape drawing in SVG format to export", type=str)

        parser.add_argument('-v', '--verbose', default=False, action="store_true",
                            help="Increase verbosity if set")
        parser.add_argument("-o", "--output-dir", type=str, default=None,
                            help="Set the output directory [default = {}]".format(ExporterConfig.OUTPUT_DIR_DEFAULT))
        parser.add_argument("--generate", action="store_true",
                            help="Generate a TOML template configuration file for input SVG file")
        parser.add_argument("--fonts-engine", type=str, choices=["latex", "inkscape"], default=None,
                            help="Set the font rendering engine [default = {}]".format(ExporterConfig.FONTS_ENGINE_DEFAULT))
        parser.add_argument("--fragments", action=argparse.BooleanOptionalAction, default=None,
                            help="Enable (or disable) fragments exportation (instead of full exportation) [default = {}]".format(ExporterConfig.FRAGMENTS_DEFAULT))

        self.args = parser.parse_args()

        # Setup logging interface ==============================================

        if self.args.verbose:
            level = logging.DEBUG
        else:
            level = logging.INFO
        APPLOGGER.set_level(level)
        LOGGER.debug("Debug mode enabled!") # Will be printed only if DEBUG level is set

    def run(self):
        """Execute the command-line"""
        # Check user-input consistency
        if not path.exists(self.args.FILE):
            LOGGER.critical("{} not found!".format(self.args.FILE))
            sys.exit(1)
        if not path.splitext(self.args.FILE)[1] == ".svg":
            LOGGER.critical("{} not an SVG!".format(self.args.FILE))
            sys.exit(1)

        # Process special options acting as subcommands
        # that differs from main command (exportation)
        # ----------------------------------------------------------------------

        if self.args.generate:
            ExporterConfig.generate_toml_template(self.args.FILE)
            exit(0)

        # From here, we are going to perform an exportation
        # ----------------------------------------------------------------------

        # Create the configuration for the input file
        config = ExporterConfig(input_file=self.args.FILE)

        # By default, load from TOML if detected
        config.load_toml()
        LOGGER.debug(config)

        # Override with command-line parameters
        config.load_args(
            output_dir=self.args.output_dir,
            fonts_engine=self.args.fonts_engine,
            fragments=self.args.fragments
        )
        LOGGER.debug(config)

        # Create and run the exportation
        exporter = Exporter(config)
        exporter.run()

# Main function of our package
def main():
    cli = CLI()
    cli.run()

# Interpreter entrypoint
if __name__ == "__main__":
    main()
