#  TinyPedal is an open-source overlay application for racing simulation.
#  Copyright (C) 2022-2025 TinyPedal developers, see contributors.md file
#
#  This file is part of TinyPedal.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
API control
"""

import logging

from .api_connector import API_PACK
from .setting import cfg

logger = logging.getLogger(__name__)


class APIControl:
    """API Control"""

    __slots__ = (
        "_api",
        "_same_api_loaded",
        "_state_override",
        "_active_state",
        "read",
    )

    def __init__(self):
        self._api = None
        self._same_api_loaded = False
        self._state_override = False
        self._active_state = False
        self.read = None

    def connect(self, name: str = ""):
        """Connect to API

        Args:
            name: match API name in API_NAME_LIST
        """
        if not name:
            name = cfg.shared_memory_api["api_name"]

        # Do not create new instance if same API already loaded
        self._same_api_loaded = bool(self._api is not None and self._api.NAME == name)
        if self._same_api_loaded:
            logger.info("CONNECTING: same API detected, fast restarting")
            return

        for _api in API_PACK:
            if _api.NAME == name:
                self._api = _api()
                return

        logger.warning("CONNECTING: Invalid API name, fall back to default")
        self._api = API_PACK[0]()

    def start(self):
        """Start API"""
        logger.info("ENCODING: %s", cfg.shared_memory_api["character_encoding"])
        logger.info("CONNECTING: %s API", self._api.NAME)
        self.setup()
        self._api.start()

        # Reload dataset if API changed
        if self.read is None or not self._same_api_loaded:
            init_read = self._api.dataset()
            self.read = init_read
            self._same_api_loaded = True

        logger.info("CONNECTED: %s API (%s)", self._api.NAME, self.version)

    def stop(self):
        """Stop API"""
        logger.info("DISCONNECTING: %s API (%s)", self._api.NAME, self.version)
        self._api.stop()
        logger.info("DISCONNECTED: %s API", self._api.NAME)

    def restart(self):
        """Restart API"""
        self.stop()
        self.connect()
        self.start()

    def setup(self):
        """Setup & apply API changes"""
        self._api.setup(
            cfg.shared_memory_api["access_mode"],
            cfg.shared_memory_api["process_id"],
            cfg.shared_memory_api["enable_player_index_override"],
            cfg.shared_memory_api["player_index"],
            cfg.shared_memory_api["character_encoding"].lower(),
        )
        self._state_override = cfg.shared_memory_api["enable_active_state_override"]
        self._active_state = cfg.shared_memory_api["active_state"]

    def start_websocket_sender(self, uri: str, interval: float = 0.1):
        if hasattr(self._api, "start_websocket_sender"):
            self._api.start_websocket_sender(uri, interval)
        else:
            logger.warning("WebSocket sender not supported by this API")

    def stop_websocket_sender(self):
        if hasattr(self._api, "stop_websocket_sender"):
            self._api.stop_websocket_sender()
        else:
            logger.warning("WebSocket sender not supported by this API")

    @property
    def name(self) -> str:
        """API name output"""
        return self._api.NAME

    @property
    def state(self) -> bool:
        """API state output"""
        if self._state_override:
            return self._active_state
        return self.read.check.api_state()

    @property
    def version(self) -> str:
        """API version output"""
        version = self.read.check.api_version()
        return version if version else "unknown"


api = APIControl()
