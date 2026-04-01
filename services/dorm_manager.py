"""Dormitory configuration manager.

Manages user dorm configurations for electricity queries.
"""

import json
import asyncio
from pathlib import Path
from typing import Optional, Dict, List
from astrbot.api import logger
from astrbot.core.utils.astrbot_path import get_astrbot_data_path

from ..models import DormConfig, UserDormRegistry


class DormManager:
    """Manages dorm configurations for all users."""

    def __init__(self, plugin_name: str):
        self.plugin_name = plugin_name
        self._data_path: Optional[Path] = None
        self._registry: Optional[UserDormRegistry] = None
        self._lock = asyncio.Lock()

    async def initialize(self):
        """Initialize the manager and load existing data."""
        self._data_path = Path(get_astrbot_data_path()) / "plugin_data" / self.plugin_name
        self._data_path.mkdir(parents=True, exist_ok=True)

        await self._load_registry()

    async def _load_registry(self):
        """Load registry from file."""
        registry_file = self._data_path / "dorm_registry.json"

        async with self._lock:
            if registry_file.exists():
                try:
                    with open(registry_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    self._registry = UserDormRegistry.from_dict(data)
                    logger.info(f"Loaded {len(self._registry.dorms)} dorm configs")
                except Exception as e:
                    logger.error(f"Failed to load dorm registry: {e}")
                    self._registry = UserDormRegistry()
            else:
                self._registry = UserDormRegistry()

    async def _save_registry(self):
        """Save registry to file."""
        if not self._registry:
            return

        registry_file = self._data_path / "dorm_registry.json"

        async with self._lock:
            try:
                with open(registry_file, 'w', encoding='utf-8') as f:
                    json.dump(self._registry.to_dict(), f, ensure_ascii=False, indent=2)
                logger.debug("Dorm registry saved")
            except Exception as e:
                logger.error(f"Failed to save dorm registry: {e}")

    async def set_dorm(self, sender_id: str, dorm: DormConfig) -> bool:
        """
        Set dorm configuration for a user.

        Returns: True if successful
        """
        if not self._registry:
            await self._load_registry()

        self._registry.set_dorm(sender_id, dorm)
        await self._save_registry()
        logger.info(f"Set dorm for {sender_id}: {dorm.get_display_name()}")
        return True

    async def get_dorm(self, sender_id: str) -> Optional[DormConfig]:
        """Get dorm configuration for a user."""
        if not self._registry:
            await self._load_registry()

        return self._registry.get_dorm(sender_id)

    async def remove_dorm(self, sender_id: str) -> bool:
        """
        Remove dorm configuration for a user.

        Returns: True if removed, False if not found
        """
        if not self._registry:
            await self._load_registry()

        removed = self._registry.remove_dorm(sender_id)
        if removed:
            await self._save_registry()
            logger.info(f"Removed dorm for {sender_id}")
        return removed

    async def get_all_dorms(self) -> List[tuple]:
        """Get all dorm configurations as (sender_id, DormConfig) tuples."""
        if not self._registry:
            await self._load_registry()

        return self._registry.get_all_dorms()

    async def get_dorm_count(self) -> int:
        """Get the number of registered dorms."""
        if not self._registry:
            await self._load_registry()

        return len(self._registry.dorms)