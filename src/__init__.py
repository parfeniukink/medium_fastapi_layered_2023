"""
This package is actually added as a parent package
because of the mypy limitation.
"""

from . import application, config, domain, presentation  # noqa: F401
