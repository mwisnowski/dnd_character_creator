"""
Wizard class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

WIZARD_CLASS: Dict[str, Any] = {}
WIZARD_LEVELS: Dict[int, Dict[str, Any]] = {}
WIZARD_FEATURES: Dict[str, Any] = {}
# Add subclass dictionaries as needed, e.g. SCHOOL_OF_EVOCATION: Dict[Union[str, int], Any] = {}
