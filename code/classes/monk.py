"""
Monk class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

MONK_CLASS: Dict[str, Any] = {}
MONK_LEVELS: Dict[int, Dict[str, Any]] = {}
MONK_FEATURES: Dict[str, Any] = {}
# Add subclass dictionaries as needed, e.g. WAY_OF_THE_OPEN_HAND: Dict[Union[str, int], Any] = {}
