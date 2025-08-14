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
Spectate list view
"""

from typing import Callable

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ..api_control import api
from ..setting import cfg
from ._common import UIScaler


class SpectateList(QWidget):
    """Spectate list view"""

    def __init__(self, parent, notify_toggle: Callable):
        super().__init__(parent)
        self.notify_toggle = notify_toggle

        # Label
        self.label_spectating = QLabel("")

        # List box
        self.listbox_spectate = QListWidget(self)
        self.listbox_spectate.setAlternatingRowColors(True)
        self.listbox_spectate.itemDoubleClicked.connect(self.spectate_selected)

        # Button
        self.button_spectate = QPushButton("Spectate")
        self.button_spectate.clicked.connect(self.spectate_selected)

        self.button_refresh = QPushButton("Refresh")
        self.button_refresh.clicked.connect(self.refresh)

        self.button_toggle = QPushButton("")
        self.button_toggle.setCheckable(True)
        self.button_toggle.setChecked(cfg.shared_memory_api["enable_player_index_override"])
        self.button_toggle.toggled.connect(self.toggle_spectate)
        self.refresh()

        layout_button = QHBoxLayout()
        layout_button.addWidget(self.button_spectate)
        layout_button.addWidget(self.button_refresh)
        layout_button.addStretch(1)
        layout_button.addWidget(self.button_toggle)

        # Layout
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.label_spectating)
        layout_main.addWidget(self.listbox_spectate)
        layout_main.addLayout(layout_button)
        margin = UIScaler.pixel(6)
        layout_main.setContentsMargins(margin, margin, margin, margin)
        self.setLayout(layout_main)

    def set_button_state(self, state: bool):
        """Set button state"""
        self.button_toggle.setChecked(state)
        self.button_toggle.setText("Enabled" if state else "Disabled")
        self.listbox_spectate.setDisabled(not state)
        self.button_spectate.setDisabled(not state)
        self.button_refresh.setDisabled(not state)
        self.label_spectating.setDisabled(not state)
        self.notify_toggle(state)

    def toggle_spectate(self, checked: bool):
        """Toggle spectate mode"""
        cfg.shared_memory_api["enable_player_index_override"] = checked
        cfg.save()
        api.setup()
        self.refresh()

    def refresh(self):
        """Refresh spectate list"""
        enabled = cfg.shared_memory_api["enable_player_index_override"]
        if enabled:
            temp_list = list(self.driver_list())
            self.listbox_spectate.clear()
            self.listbox_spectate.addItems(temp_list)
            index = min(
                max(cfg.shared_memory_api["player_index"], -1) + 1,  # +1 offset
                len(temp_list) - 1,  # prevent exceeding max players
            )
            self.listbox_spectate.setCurrentRow(index)
            self.label_spectating.setText(f"Spectating: <b>{temp_list[index]}</b>")
        else:
            self.listbox_spectate.clear()
            self.label_spectating.setText("Spectating: <b>Disabled</b>")

        self.set_button_state(enabled)

    def spectate_selected(self):
        """Spectate selected player"""
        selected_index = self.listbox_spectate.currentRow()
        cfg.shared_memory_api["player_index"] = max(selected_index - 1, -1)
        api.setup()
        self.refresh()
        cfg.save()

    @staticmethod
    def driver_list():
        """Create driver list"""
        yield "Anonymous"
        for index in range(api.read.vehicle.total_vehicles()):
            yield api.read.vehicle.driver_name(index)
