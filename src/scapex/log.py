#!/usr/bin/env python3

"""Logging module

Provides an application logger and a testing interface.
"""

# Standard imports
import logging

# Package imports

try:
    # If `__name__ == "__main__"`, this will load with success.
    # We do not use `scapex.constants` to NOT run `__init__.py`,
    # otherwise, when testing this module, two loggers will be initialized.
    from constants import PACKAGE_NAME
except ModuleNotFoundError:
    from scapex.constants import PACKAGE_NAME

class AppLogger():
    """Application logger

    Class storing the Logger, the Handler and the Formatter configured
    accordingly to our preferences.
    """

    # Formats for INFO and DEBUG levels
    FMT_INFO = "[%(levelname)s] {}: %(message)s".format(PACKAGE_NAME)
    FMT_DEBUG = "[%(levelname)s] %(name)s: %(message)s"

    logger = None           # logging.Logger object
    handler = None          # logging.Handler object
    formatter_info = None   # logging.Formatter object
    formatter_debug = None  # logging.Formatter object

    def __init__(self, level = None):
        """Initialize the application logger with its Logger, Handler and Formatters"""
        assert level is None or level in [logging.INFO, logging.DEBUG]

        # Create the formatters
        self.formatter_info = logging.Formatter(self.FMT_INFO)
        self.formatter_debug = logging.Formatter(self.FMT_DEBUG)
        # Create the console handler
        self.handler = logging.StreamHandler()
        # Create the parent logger of our application
        self.logger = logging.getLogger(PACKAGE_NAME)
        self.logger.addHandler(self.handler)

        # Defines default to INFO
        if level is None:
            level = logging.INFO

        # Connect everything
        self.set_level(level)

    def set_level(self, level):
        """Set the logging level of the application logger"""
        assert level in [logging.INFO, logging.DEBUG]

        # Choose Formatter based on level
        if level == logging.INFO:
            formatter = self.formatter_info
        elif level == logging.DEBUG:
            formatter = self.formatter_debug

        # Update level
        self.handler.setFormatter(formatter)
        self.handler.setLevel(level)
        self.logger.setLevel(level)

# Testing purpose
if __name__ == "__main__":
    applogger = AppLogger()

    print("Test at INFO level")

    applogger.logger.info("Info message from app logger")
    applogger.logger.debug("Debug message from app logger")
    modulelogger = logging.getLogger('scapex.log')
    modulelogger.info("Info message from module logger")
    modulelogger.debug("Debug message from module logger")

    print("Test at DEBUG level")

    applogger.set_level(logging.DEBUG)
    applogger.logger.info("Info message from app logger")
    applogger.logger.debug("Debug message from app logger")
    modulelogger.info("Info message from module logger")
    modulelogger.debug("Debug message from module logger")
