"""
Session Browser Widget (WebSocket-based)
"""

from typing import Callable
from PySide6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QPushButton,
    QLabel,
    QWidget,
)

from ..setting import cfg
from ..api_control import api
from ._common import UIScaler



class SessionBrowser(QWidget):
    """Widget for browsing and joining active telemetry sessions (via WebSocket)"""

    def __init__(self, parent, notify_toggle: Callable = lambda _: None):
        super().__init__(parent)
        self.notify_toggle = notify_toggle

        # Label
        self.label_status = QLabel("")

        # Session list
        self.listbox_sessions = QListWidget(self)
        self.listbox_sessions.setAlternatingRowColors(True)
        self.listbox_sessions.itemDoubleClicked.connect(self.join_selected)

        # Buttons
        self.button_join = QPushButton("Join")
        self.button_join.clicked.connect(self.join_selected)

        self.button_refresh = QPushButton("Refresh")
        self.button_refresh.clicked.connect(self.refresh_sessions)

        self.button_toggle = QPushButton("")
        self.button_toggle.setCheckable(True)
        self.button_toggle.clicked.connect(self.toggle_remote_connection)
        self.update_toggle_button_text()

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_join)
        layout_buttons.addWidget(self.button_refresh)
        layout_buttons.addWidget(self.button_toggle)
        layout_buttons.addStretch(1)

        layout_main = QVBoxLayout()
        layout_main.addWidget(self.label_status)
        layout_main.addWidget(self.listbox_sessions)
        layout_main.addLayout(layout_buttons)

        margin = UIScaler.pixel(6)
        layout_main.setContentsMargins(margin, margin, margin, margin)
        self.setLayout(layout_main)

        self.refresh_sessions()

    def refresh_sessions(self):
        """Send session list request over WebSocket"""
        try:
            info = api._api.info
            print("info:", info)
            print("has _ws_client:", hasattr(info, "_ws_client"))
            client = getattr(info, "_ws_client", None)
            print("client:", client)
            if client and hasattr(client, "request_session_list"):
                client.request_session_list(self.update_sessions)
                self.label_status.setText("Requesting session list...")
            else:
                self.label_status.setText("WebSocket client not available.")
        except Exception as e:
            self.label_status.setText(f"Error: {e}")

    def update_sessions(self, data: dict):
        """Update session list in UI from full JSON dict"""
        sessions = data.get("sessions", [])
        self.listbox_sessions.clear()
        for sess in sessions:
            name = sess.get("name", "<unknown>")
            sender = sess.get("sender") or "No sender"
            viewers = sess.get("receivers", 0)
            label = f"{name} — {sender}, {viewers} viewers"
            self.listbox_sessions.addItem(label)
            # Use role 256 as user data to store session name
            self.listbox_sessions.item(self.listbox_sessions.count() - 1).setData(256, name)

        self.label_status.setText(f"Found {len(sessions)} active session(s)")

    def join_selected(self):
        """Join selected session"""
        selected_item = self.listbox_sessions.currentItem()
        if not selected_item:
            return

        session_name = selected_item.data(256)
        if not session_name:
            return

        cfg.shared_memory_api["websocket_session"] = session_name
        cfg.save()
        api.restart()
        

        self.label_status.setText(f"Joined session: <b>{session_name}</b>")

    def toggle_remote_connection(self):
        """Toggle remote connection on/off"""
        current = cfg.shared_memory_api.get("connect_to_remote", False)
        cfg.shared_memory_api["connect_to_remote"] = not current
        cfg.save()
        api.restart()
        self.update_toggle_button_text()
        self.refresh_sessions()

    def update_toggle_button_text(self):
        connected = cfg.shared_memory_api.get("connect_to_remote", False)
        self.button_toggle.setChecked(connected)
        self.button_toggle.setText("Connected" if connected else "Disconnected")

    def refresh(self):
        self.refresh_sessions()