"""
Rogue class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

ROGUE_CLASS: Dict[str, Any] = {}
ROGUE_LEVELS: Dict[int, Dict[str, Any]] = {}
ROGUE_FEATURES: Dict[str, Any] = {}
# Add subclass dictionaries as needed, e.g. THIEF: Dict[Union[str, int], Any] = {}
