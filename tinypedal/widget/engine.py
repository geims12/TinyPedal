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
Engine Widget
"""

from .. import calculation as calc
from ..api_control import api
from ..units import (
    set_symbol_power,
    set_symbol_pressure,
    set_unit_power,
    set_unit_pressure,
    set_unit_temperature,
)
from ._base import Overlay


class Realtime(Overlay):
    """Draw widget"""

    def __init__(self, config, widget_name):
        # Assign base setting
        super().__init__(config, widget_name)
        layout = self.set_grid_layout(gap=self.wcfg["bar_gap"])
        self.set_primary_layout(layout=layout)

        # Config font
        font_m = self.get_font_metrics(
            self.config_font(self.wcfg["font_name"], self.wcfg["font_size"]))

        # Config variable
        bar_padx = self.set_padding(self.wcfg["font_size"], self.wcfg["bar_padding"])
        bar_width = font_m.width * 8 + bar_padx

        # Config units
        self.unit_temp = set_unit_temperature(self.cfg.units["temperature_unit"])
        self.unit_power = set_unit_power(self.cfg.units["power_unit"])
        self.symbol_power = set_symbol_power(self.cfg.units["power_unit"])
        self.unit_pres = set_unit_pressure(self.cfg.units["turbo_pressure_unit"])
        self.symbol_pres = set_symbol_pressure(self.cfg.units["turbo_pressure_unit"])

        # Base style
        self.set_base_style(self.set_qss(
            font_family=self.wcfg["font_name"],
            font_size=self.wcfg["font_size"],
            font_weight=self.wcfg["font_weight"])
        )

        # Oil temperature
        if self.wcfg["show_oil_temperature"]:
            self.bar_style_oil = (
                self.set_qss(
                    fg_color=self.wcfg["font_color_oil"],
                    bg_color=self.wcfg["bkg_color_oil"]),
                self.set_qss(
                    fg_color=self.wcfg["font_color_oil"],
                    bg_color=self.wcfg["warning_color_overheat"])
            )
            self.bar_oil = self.set_qlabel(
                text="Oil T",
                style=self.bar_style_oil[0],
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_oil,
                column=self.wcfg["column_index_oil"],
            )

        # Water temperature
        if self.wcfg["show_water_temperature"]:
            self.bar_style_water = (
                self.set_qss(
                    fg_color=self.wcfg["font_color_water"],
                    bg_color=self.wcfg["bkg_color_water"]),
                self.set_qss(
                    fg_color=self.wcfg["font_color_water"],
                    bg_color=self.wcfg["warning_color_overheat"])
            )
            self.bar_water = self.set_qlabel(
                text="Water T",
                style=self.bar_style_water[0],
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_water,
                column=self.wcfg["column_index_water"],
            )

        # Turbo pressure
        if self.wcfg["show_turbo_pressure"]:
            bar_style_turbo = self.set_qss(
                fg_color=self.wcfg["font_color_turbo"],
                bg_color=self.wcfg["bkg_color_turbo"]
            )
            self.bar_turbo = self.set_qlabel(
                text="Turbo",
                style=bar_style_turbo,
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_turbo,
                column=self.wcfg["column_index_turbo"],
            )

        # Engine RPM
        if self.wcfg["show_rpm"]:
            bar_style_rpm = self.set_qss(
                fg_color=self.wcfg["font_color_rpm"],
                bg_color=self.wcfg["bkg_color_rpm"]
            )
            self.bar_rpm = self.set_qlabel(
                text="RPM",
                style=bar_style_rpm,
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_rpm,
                column=self.wcfg["column_index_rpm"],
            )

        # Engine RPM maximum
        if self.wcfg["show_rpm_maximum"]:
            bar_style_rpm_max = self.set_qss(
                fg_color=self.wcfg["font_color_rpm_maximum"],
                bg_color=self.wcfg["bkg_color_rpm_maximum"]
            )
            self.bar_rpm_max = self.set_qlabel(
                text="MAX RPM",
                style=bar_style_rpm_max,
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_rpm_max,
                column=self.wcfg["column_index_rpm_maximum"],
            )

        # Engine torque
        if self.wcfg["show_torque"]:
            bar_style_torque = self.set_qss(
                fg_color=self.wcfg["font_color_torque"],
                bg_color=self.wcfg["bkg_color_torque"]
            )
            self.bar_torque = self.set_qlabel(
                text="TORQUE",
                style=bar_style_torque,
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_torque,
                column=self.wcfg["column_index_torque"],
            )

        # Engine power
        if self.wcfg["show_power"]:
            bar_style_power = self.set_qss(
                fg_color=self.wcfg["font_color_power"],
                bg_color=self.wcfg["bkg_color_power"]
            )
            self.bar_power = self.set_qlabel(
                text="POWER",
                style=bar_style_power,
                width=bar_width,
            )
            self.set_primary_orient(
                target=self.bar_power,
                column=self.wcfg["column_index_power"],
            )

    def timerEvent(self, event):
        """Update when vehicle on track"""
        # Oil temperature
        if self.wcfg["show_oil_temperature"]:
            temp_oil = round(api.read.engine.oil_temperature(), 2)
            self.update_oil(self.bar_oil, temp_oil)

        # Water temperature
        if self.wcfg["show_water_temperature"]:
            temp_water = round(api.read.engine.water_temperature(), 2)
            self.update_water(self.bar_water, temp_water)

        # Turbo pressure
        if self.wcfg["show_turbo_pressure"]:
            turbo = int(api.read.engine.turbo())
            self.update_turbo(self.bar_turbo, turbo)

        # Engine RPM
        if self.wcfg["show_rpm"]:
            rpm = int(api.read.engine.rpm())
            self.update_rpm(self.bar_rpm, rpm)

        # Engine RPM maximum
        if self.wcfg["show_rpm_maximum"]:
            rpm_max = int(api.read.engine.rpm_max())
            self.update_rpm_max(self.bar_rpm_max, rpm_max)

        # Engine torque
        if self.wcfg["show_torque"]:
            torque = round(api.read.engine.torque(), 2)
            self.update_torque(self.bar_torque, torque)

        # Engine power
        if self.wcfg["show_power"]:
            power = round(calc.engine_power(
                api.read.engine.torque(), api.read.engine.rpm()), 2)
            self.update_power(self.bar_power, power)

    # GUI update methods
    def update_oil(self, target, data):
        """Oil temperature"""
        if target.last != data:
            target.last = data
            target.setText(f"O{self.unit_temp(data): >6.1f}°")
            target.updateStyle(self.bar_style_oil[data >= self.wcfg["overheat_threshold_oil"]])

    def update_water(self, target, data):
        """Water temperature"""
        if target.last != data:
            target.last = data
            target.setText(f"W{self.unit_temp(data): >6.1f}°")
            target.updateStyle(self.bar_style_water[data >= self.wcfg["overheat_threshold_water"]])

    def update_turbo(self, target, data):
        """Turbo pressure"""
        if target.last != data:
            target.last = data
            text = f"{self.unit_pres(data * 0.001):03.3f}"[:5]
            target.setText(f"{text}{self.symbol_pres}")

    def update_rpm(self, target, data):
        """Engine RPM"""
        if target.last != data:
            target.last = data
            target.setText(f"{data: >5}rpm")

    def update_rpm_max(self, target, data):
        """Engine RPM maximum"""
        if target.last != data:
            target.last = data
            target.setText(f"{data: >5}max")

    def update_torque(self, target, data):
        """Engine torque"""
        if target.last != data:
            target.last = data
            text = f"{data: >6.2f}"[:6]
            target.setText(f"{text}Nm")

    def update_power(self, target, data):
        """Engine power"""
        if target.last != data:
            target.last = data
            text = f"{self.unit_power(data): >6.2f}"[:6]
            target.setText(f"{text}{self.symbol_power}")
