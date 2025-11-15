#!/usr/bin/env python3

"""Logging module."""

# Standard imports
import logging

class ScapeXLogger():
    """Logger for ScapeX."""

    FMT_INFO = "[%(levelname)s] %(name)s: %(message)s"
    FMT_DEBUG = "[%(levelname)s] %(name)s.%(module)s: %(message)s"

    def __init__(self, level):
        assert level in [logging.INFO, logging.DEBUG]
        # Create the logger
        self.logger = logging.getLogger('scapex')
        self.logger.setLevel(level)

        # Create console handler and set level to debug
        self.handler = logging.StreamHandler()
        self.handler.setLevel(level)

        # Create formatter
        if level == logging.INFO:
            fmt = ScapeXLogger.FMT_INFO
        elif level == logging.DEBUG:
            fmt = ScapeXLogger.FMT_DEBUG
        else:
            fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.formatter = logging.Formatter(fmt)

        # Connect everything
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
