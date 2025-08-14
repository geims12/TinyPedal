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
Track info editor
"""

import logging
import time

from PySide6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from ..api_control import api
from ..const_file import ConfigType
from ..setting import cfg, copy_setting
from ..template.setting_tracks import TRACKINFO_DEFAULT
from ._common import (
    BaseEditor,
    CompactButton,
    FloatTableItem,
    UIScaler,
)

HEADER_TRACKS = "Track name","Pit entry (m)","Pit exit (m)","Pit speed (m/s)"

logger = logging.getLogger(__name__)


class TrackInfoEditor(BaseEditor):
    """Track info editor"""

    def __init__(self, parent):
        super().__init__(parent)
        self.set_utility_title("Track Info Editor")
        self.setMinimumSize(UIScaler.size(45), UIScaler.size(38))

        self.tracks_temp = copy_setting(cfg.user.tracks)

        # Set table
        self.table_tracks = QTableWidget(self)
        self.table_tracks.setColumnCount(len(HEADER_TRACKS))
        self.table_tracks.setHorizontalHeaderLabels(HEADER_TRACKS)
        self.table_tracks.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table_tracks.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for idx in range(1, len(HEADER_TRACKS)):
            self.table_tracks.horizontalHeader().setSectionResizeMode(idx, QHeaderView.Fixed)
            self.table_tracks.setColumnWidth(idx, UIScaler.size(8))
        self.table_tracks.cellChanged.connect(self.verify_input)
        self.refresh_table()
        self.set_unmodified()

        # Set button
        layout_button = self.set_layout_button()

        # Set layout
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.table_tracks)
        layout_main.addLayout(layout_button)
        layout_main.setContentsMargins(self.MARGIN, self.MARGIN, self.MARGIN, self.MARGIN)
        self.setLayout(layout_main)

    def set_layout_button(self):
        """Set button layout"""
        button_add = CompactButton("Add")
        button_add.clicked.connect(self.add_track)

        button_sort = CompactButton("Sort")
        button_sort.clicked.connect(self.sort_track)

        button_delete = CompactButton("Delete")
        button_delete.clicked.connect(self.delete_track)

        button_reset = CompactButton("Reset")
        button_reset.clicked.connect(self.reset_setting)

        button_apply = CompactButton("Apply")
        button_apply.clicked.connect(self.applying)

        button_save = CompactButton("Save")
        button_save.clicked.connect(self.saving)

        button_close = CompactButton("Close")
        button_close.clicked.connect(self.close)

        # Set layout
        layout_button = QHBoxLayout()
        layout_button.addWidget(button_add)
        layout_button.addWidget(button_sort)
        layout_button.addWidget(button_delete)
        layout_button.addWidget(button_reset)
        layout_button.addStretch(1)
        layout_button.addWidget(button_apply)
        layout_button.addWidget(button_save)
        layout_button.addWidget(button_close)
        return layout_button

    def refresh_table(self):
        """Refresh tracks list"""
        self.table_tracks.setRowCount(0)
        row_index = 0
        for track_name, track_data in self.tracks_temp.items():
            self.add_track_entry(row_index, track_name, track_data)
            row_index += 1

    def add_track(self):
        """Add new track"""
        start_index = row_index = self.table_tracks.rowCount()
        # Add missing track name from active session
        track_name = api.read.session.track_name()
        if track_name and not self.is_value_in_table(track_name, self.table_tracks):
            self.add_track_entry(row_index, track_name, TRACKINFO_DEFAULT)
            row_index += 1
        # Add new name entry
        if start_index == row_index:
            new_track_name = self.new_name_increment("New Track Name", self.table_tracks)
            self.add_track_entry(row_index, new_track_name, TRACKINFO_DEFAULT)
            self.table_tracks.setCurrentCell(row_index, 0)

    def add_track_entry(self, row_index: int, track_name: str, track_data: dict):
        """Add new track entry to table"""
        self.table_tracks.insertRow(row_index)
        self.table_tracks.setItem(row_index, 0, QTableWidgetItem(track_name))
        column_index = 1
        for key, value in TRACKINFO_DEFAULT.items():
            self.table_tracks.setItem(
                row_index,
                column_index,
                FloatTableItem(track_data.get(key, value)),
            )
            column_index += 1

    def sort_track(self):
        """Sort tracks in ascending order"""
        if self.table_tracks.rowCount() > 1:
            self.table_tracks.sortItems(0)
            self.set_modified()

    def delete_track(self):
        """Delete track entry"""
        selected_rows = set(data.row() for data in self.table_tracks.selectedIndexes())
        if not selected_rows:
            QMessageBox.warning(self, "Error", "No data selected.")
            return

        if not self.confirm_operation(message="<b>Delete selected rows?</b>"):
            return

        for row_index in sorted(selected_rows, reverse=True):
            self.table_tracks.removeRow(row_index)
        self.set_modified()

    def reset_setting(self):
        """Reset setting"""
        msg_text = (
            "Reset <b>tracks preset</b> to default?<br><br>"
            "Changes are only saved after clicking Apply or Save Button."
        )
        if self.confirm_operation(message=msg_text):
            self.tracks_temp = copy_setting(cfg.default.tracks)
            self.set_modified()
            self.refresh_table()

    def applying(self):
        """Save & apply"""
        self.save_setting()

    def saving(self):
        """Save & close"""
        self.save_setting()
        self.accept()  # close

    def verify_input(self, row_index: int, column_index: int):
        """Verify input value"""
        self.set_modified()
        item = self.table_tracks.item(row_index, column_index)
        if column_index >= 1:
            item.validate()

    def update_tracks_temp(self):
        """Update temporary changes to tracks temp first"""
        self.tracks_temp.clear()
        for row_index in range(self.table_tracks.rowCount()):
            track_name = self.table_tracks.item(row_index, 0).text()
            self.tracks_temp[track_name] = {
                key: self.table_tracks.item(row_index, column_index).value()
                for column_index, key in enumerate(TRACKINFO_DEFAULT, start=1)
            }

    def save_setting(self):
        """Save setting"""
        self.update_tracks_temp()
        cfg.user.tracks = copy_setting(self.tracks_temp)
        cfg.save(0, cfg_type=ConfigType.TRACKS)
        while cfg.is_saving:  # wait saving finish
            time.sleep(0.01)
        self.reloading()
        self.set_unmodified()
