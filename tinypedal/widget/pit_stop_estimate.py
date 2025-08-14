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
Pit stop estimate Widget
"""

from .. import calculation as calc
from ..api_control import api
from ..module_info import minfo
from ..units import set_unit_fuel
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
        text_def = "-.--"
        bar_padx = self.set_padding(self.wcfg["font_size"], self.wcfg["bar_padding"])
        self.bar_width = max(self.wcfg["bar_width"], 3)
        style_width = font_m.width * self.bar_width + bar_padx
        self.extra_time = max(self.wcfg["additional_pitstop_time"], 0)

        # Config units
        self.unit_fuel = set_unit_fuel(self.cfg.units["fuel_unit"])

        # Base style
        self.set_base_style(self.set_qss(
            font_family=self.wcfg["font_name"],
            font_size=self.wcfg["font_size"],
            font_weight=self.wcfg["font_weight"])
        )

        # Create layout
        layout_upper = self.set_grid_layout()
        layout_lower = self.set_grid_layout()
        layout.addLayout(layout_upper, self.wcfg["column_index_upper"], 0)
        layout.addLayout(layout_lower, self.wcfg["column_index_lower"], 0)

        # Caption
        if self.wcfg["show_caption"]:
            bar_style_desc = self.set_qss(
                fg_color=self.wcfg["font_color_caption"],
                bg_color=self.wcfg["bkg_color_caption"],
                font_size=int(self.wcfg['font_size'] * 0.8)
            )
            caption_upper = (
                self.wcfg["caption_text_pass_duration"],
                self.wcfg["caption_text_stop_duration"],
                self.wcfg["caption_text_maximum_delay"],
                self.wcfg["caption_text_actual_relative_refill"],
            )
            caption_lower = (
                self.wcfg["caption_text_pit_timer"],
                self.wcfg["caption_text_minimum_total_duration"],
                self.wcfg["caption_text_maximum_total_duration"],
                self.wcfg["caption_text_total_relative_refill"],
            )

            row_idx_upper = 2 * self.wcfg["swap_upper_caption"]
            for index, text_caption in enumerate(caption_upper):
                cap_temp = self.set_qlabel(
                    text=text_caption,
                    style=bar_style_desc,
                    fixed_width=style_width,
                )
                layout_upper.addWidget(cap_temp, row_idx_upper, index)

            row_idx_lower = 2 - 2 * self.wcfg["swap_lower_caption"]
            for index, text_caption in enumerate(caption_lower):
                cap_temp = self.set_qlabel(
                    text=text_caption,
                    style=bar_style_desc,
                    fixed_width=style_width,
                )
                layout_lower.addWidget(cap_temp, row_idx_lower, index)

        # Estimated pit pass through time
        bar_style_pass = self.set_qss(
            fg_color=self.wcfg["font_color_pass_duration"],
            bg_color=self.wcfg["bkg_color_pass_duration"]
        )
        self.bar_pass = self.set_qlabel(
            text=text_def,
            style=bar_style_pass,
            fixed_width=style_width,
        )
        self.bar_pass.decimals = max(self.wcfg["decimal_places_pass_duration"], 0)

        # Estimated pit stop time
        bar_style_stop = self.set_qss(
            fg_color=self.wcfg["font_color_stop_duration"],
            bg_color=self.wcfg["bkg_color_stop_duration"]
        )
        self.bar_stop = self.set_qlabel(
            text=text_def,
            style=bar_style_stop,
            fixed_width=style_width,
        )
        self.bar_stop.decimals = max(self.wcfg["decimal_places_stop_duration"], 0)

        # Maximum pit stop delay time
        bar_style_delay = self.set_qss(
            fg_color=self.wcfg["font_color_maximum_delay"],
            bg_color=self.wcfg["bkg_color_maximum_delay"]
        )
        self.bar_delay = self.set_qlabel(
            text=text_def,
            style=bar_style_delay,
            fixed_width=style_width,
        )
        self.bar_delay.decimals = max(self.wcfg["decimal_places_maximum_delay"], 0)

        # Relative refilling
        bar_style_refill = self.set_qss(
            fg_color=self.wcfg["font_color_actual_relative_refill"],
            bg_color=self.wcfg["bkg_color_actual_relative_refill"]
        )
        self.bar_refill = self.set_qlabel(
            text=text_def,
            style=bar_style_refill,
            fixed_width=style_width,
        )
        self.bar_refill.decimals = max(self.wcfg["decimal_places_actual_relative_refill"], 0)

        # Pit timer
        bar_style_timer = self.set_qss(
            fg_color=self.wcfg["font_color_pit_timer"],
            bg_color=self.wcfg["bkg_color_pit_timer"]
        )
        self.bar_timer = self.set_qlabel(
            text=text_def,
            style=bar_style_timer,
            fixed_width=style_width,
        )
        self.bar_timer.decimals = max(self.wcfg["decimal_places_pit_timer"], 0)

        # Estimated min total pit time
        bar_style_minpit = self.set_qss(
            fg_color=self.wcfg["font_color_minimum_total_duration"],
            bg_color=self.wcfg["bkg_color_minimum_total_duration"]
        )
        self.bar_minpit = self.set_qlabel(
            text=text_def,
            style=bar_style_minpit,
            fixed_width=style_width,
            last=-1,
        )
        self.bar_minpit.decimals = max(self.wcfg["decimal_places_minimum_total_duration"], 0)

        # Estimated max total pit time
        bar_style_maxpit = self.set_qss(
            fg_color=self.wcfg["font_color_maximum_total_duration"],
            bg_color=self.wcfg["bkg_color_maximum_total_duration"]
        )
        self.bar_maxpit = self.set_qlabel(
            text=text_def,
            style=bar_style_maxpit,
            fixed_width=style_width,
        )
        self.bar_maxpit.decimals = max(self.wcfg["decimal_places_maximum_total_duration"], 0)

        # Estimated total needed refill
        bar_style_needed = self.set_qss(
            fg_color=self.wcfg["font_color_total_relative_refill"],
            bg_color=self.wcfg["bkg_color_total_relative_refill"]
        )
        self.bar_needed = self.set_qlabel(
            text=text_def,
            style=bar_style_needed,
            fixed_width=style_width,
        )
        self.bar_needed.decimals = max(self.wcfg["decimal_places_total_relative_refill"], 0)

        # Set layout
        layout_upper.addWidget(self.bar_pass, 1, 0)
        layout_upper.addWidget(self.bar_stop, 1, 1)
        layout_upper.addWidget(self.bar_delay, 1, 2)
        layout_upper.addWidget(self.bar_refill, 1, 3)
        layout_lower.addWidget(self.bar_timer, 1, 0)
        layout_lower.addWidget(self.bar_minpit, 1, 1)
        layout_lower.addWidget(self.bar_maxpit, 1, 2)
        layout_lower.addWidget(self.bar_needed, 1, 3)

    def timerEvent(self, event):
        """Update when vehicle on track"""
        pitlane_length = minfo.mapping.pitLaneLength
        speed_limit = minfo.mapping.pitSpeedLimit
        min_pitstop_time, max_pitstop_time, refill_fuel, refill_energy, state_stopgo = minfo.restapi.pitStopEstimate
        pass_time = pitlane_length / speed_limit if speed_limit else 0
        delay_time = max_pitstop_time - min_pitstop_time
        pit_timer = minfo.vehicles.dataSet[minfo.vehicles.playerIndex].pitTimer.elapsed

        if state_stopgo:
            stopgo_time = minfo.restapi.penaltyTime
            if stopgo_time <= 0:  # fallback if not available from API
                stopgo_time = self.wcfg["stop_go_penalty_time"]

            if state_stopgo == 1:  # stopgo only
                min_pitstop_time = max_pitstop_time = stopgo_time
                refill_fuel = refill_energy = 0
            else:  # add stopgo time to service time (simultaneous)
                min_pitstop_time += stopgo_time
                max_pitstop_time += stopgo_time

        if minfo.restapi.maxVirtualEnergy:
            actual_refill = refill_energy
            total_refill = calc.sym_max(minfo.energy.neededRelative, 9999)
        else:
            actual_refill = self.unit_fuel(refill_fuel)
            total_refill = calc.sym_max(self.unit_fuel(minfo.fuel.neededRelative), 9999)

        # Estimated pit pass through time
        self.update_estimate(self.bar_pass, pass_time)

        # Estimated pit stop time
        self.update_estimate(self.bar_stop, min_pitstop_time)

        # Maximum pit stop delay time
        self.update_estimate(self.bar_delay, delay_time, "+")

        # Pit timer
        self.update_estimate(self.bar_timer, pit_timer)

        # Relative refilling
        self.update_estimate(self.bar_refill, max(actual_refill, 0), "+")

        # Estimated total needed refill
        self.update_estimate(self.bar_needed, total_refill, "+")

        # Estimated min, max total pit time, update while not in pit
        if not api.read.vehicle.in_pits() or self.bar_minpit.last < pass_time:
            if min_pitstop_time:
                min_total = min_pitstop_time + pass_time + self.extra_time
                max_total = max_pitstop_time + pass_time + self.extra_time
            else:
                min_total = max_total = 0
            self.update_estimate(self.bar_minpit, min_total)
            self.update_estimate(self.bar_maxpit, max_total)

    # GUI update methods
    def update_estimate(self, target, data, sign=""):
        """Update estimate pit data"""
        if target.last != data:
            target.last = data
            text = f"{data:{sign}.{target.decimals}f}"[:self.bar_width].strip(".")
            target.setText(text)
