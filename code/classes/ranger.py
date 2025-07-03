"""
Ranger class data for D&D character creator.
Contains class definition, level progression, features, and subclasses.
"""

from __future__ import annotations
from typing import Any, Dict, List, Union

RANGER_CLASS: Dict[str, Any] = {}
RANGER_LEVELS: Dict[int, Dict[str, Any]] = {}
RANGER_FEATURES: Dict[str, Any] = {}
# Add subclass dictionaries as needed, e.g. HUNTER: Dict[Union[str, int], Any] = {}
