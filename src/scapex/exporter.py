#!/usr/bin/env python3

"""Inkscape exporter module"""

# Standard imports
import subprocess
import logging

# Package module imports
from scapex.config import ExporterConfig

# Module logger
LOGGER = logging.getLogger(__name__)

class Exporter():
    """Inkscape Exporter configurable through ExporterConfig"""

    # Configuration [ExporterConfig]
    config = None

    def __init__(self, config):
        assert type(config) == ExporterConfig
        # Get the configuration
        self.config = config

    def run(self):
        """Run the exportation based on current config, either in full or fragments mode"""
        LOGGER.info("Run exportation: {}".format(self.config.input_file))
        if not self.config.config_dict["params"]["fragments"]:
            self._export_full()
        else:
            self._export_fragments()

    def _export_full(self):
        """Export an Inkscape SVG in full mode"""
        # Build exportation option string based on configuration
        inkscape_opts = [ExporterConfig.INKSCAPE_OPT_AREA, ExporterConfig.INKSCAPE_OPT_TYPE]
        if self.config.config_dict["params"]["fonts_engine"] == "latex":
            inkscape_opts += [ExporterConfig.INKSCAPE_OPT_FONTS_LATEX]

        # Build output filename
        output_file = "{}/{}".format(
            self.config.output_dir,
            ExporterConfig.OUTPUT_FILE_FULL_TEMPLATE.format(self.config.input_file_basename)
        )

        # Build command-line
        cmdline = ["inkscape"] + inkscape_opts + ["--export-filename={}".format(output_file), self.config.input_file]

        # Run the exportation
        LOGGER.debug("Run: {}".format(cmdline))
        subprocess.run(cmdline)

    def _export_fragments(self):
        """Export an Inkscape SVG in fragments mode"""
        # Build exportation option string based on configuration
        inkscape_opts = [ExporterConfig.INKSCAPE_OPT_AREA, ExporterConfig.INKSCAPE_OPT_TYPE]
        if self.config.config_dict["params"]["fonts_engine"] == "latex":
            inkscape_opts += [ExporterConfig.INKSCAPE_OPT_FONTS_LATEX]

        # Iterate over all fragments
        for fragment in self.config.config_dict["fragments"]:
            # Build output filename
            output_file = "{}/{}".format(
                self.config.output_dir,
                ExporterConfig.OUTPUT_FILE_FRAGMENTS_TEMPLATE.format(
                    self.config.input_file_basename,
                    fragment)
            )

            # Get layers that should be excluded from current fragment
            excluded_layers = self.config.config_dict["fragments"][fragment]["excluded_layers"]

            # Based on that list, build the Inkscape actions that should be used to exclude those layers
            if len(excluded_layers) >= 1:
                inkscape_actions = ["--actions=select-by-id:{};delete-selection;export-do".format(",".join(excluded_layers))]
            else:
                inkscape_actions = []

            # Build final command-line
            cmdline = ["inkscape"] \
                + inkscape_opts \
                + inkscape_actions \
                + ["--export-filename={}".format(output_file), self.config.input_file]

            # Run the exportation
            LOGGER.debug("Run: {}".format(cmdline))
            subprocess.run(cmdline)
