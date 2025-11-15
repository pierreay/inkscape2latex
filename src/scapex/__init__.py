#!/usr/bin/env python3

"""Package initialization.

Defines constants, global variables, and initialization code."""

# Constants
# ==============================================================================

APPLICATION_NAME = "ScapeX"
PACKAGE_NAME = "scapex"

# Global variables
# ==============================================================================

# Application logger
APPLOGGER = None    # scapex.log.AppLogger

# Package initialization
# ==============================================================================

# Import a package module.
from scapex import mylib

# Initialize the package.
print("Call mylib.hello_init() from '__init__.py'...")
mylib.hello_init()
