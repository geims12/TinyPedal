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
Virtual energy Widget
"""

from .. import calculation as calc
from ..api_control import api
from ..module_info import minfo
from ._base import Overlay
from ._common import WarningFlash
from ._painter import FuelLevelBar


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
                self.wcfg["caption_text_pits"],
                self.wcfg["caption_text_remain"],
                (
                    self.wcfg["caption_text_absolute_refill"]
                    if self.wcfg["show_absolute_refilling"]
                    else self.wcfg["caption_text_refill"]
                ),
                self.wcfg["caption_text_used"],
                self.wcfg["caption_text_delta"],
                self.wcfg["caption_text_ratio"],
            )
            caption_lower = (
                self.wcfg["caption_text_early"],
                self.wcfg["caption_text_laps"],
                self.wcfg["caption_text_minutes"],
                self.wcfg["caption_text_save"],
                self.wcfg["caption_text_end"],
                self.wcfg["caption_text_bias"],
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

        # Estimated end remaining
        bar_style_end = self.set_qss(
            fg_color=self.wcfg["font_color_end"],
            bg_color=self.wcfg["bkg_color_end"]
        )
        self.bar_end = self.set_qlabel(
            text=text_def,
            style=bar_style_end,
            fixed_width=style_width,
        )
        self.bar_end.decimals = max(self.wcfg["decimal_places_end"], 0)

        # Remaining
        self.bar_style_curr = (
            self.set_qss(
                fg_color=self.wcfg["font_color_remain"],
                bg_color=self.wcfg["bkg_color_remain"]),
            self.set_qss(
                fg_color=self.wcfg["font_color_remain"],
                bg_color=self.wcfg["warning_color_low_energy"])
        )
        self.bar_curr = self.set_qlabel(
            text=text_def,
            style=self.bar_style_curr[0],
            fixed_width=style_width,
        )
        self.bar_curr.decimals = max(self.wcfg["decimal_places_remain"], 0)

        # Total needed
        self.bar_style_need = (
            self.set_qss(
                fg_color=self.wcfg["font_color_refill"],
                bg_color=self.wcfg["bkg_color_refill"]),
            self.set_qss(
                fg_color=self.wcfg["font_color_refill"],
                bg_color=self.wcfg["warning_color_low_energy"])
        )
        self.bar_need = self.set_qlabel(
            text=text_def,
            style=self.bar_style_need[0],
            fixed_width=style_width,
        )
        self.bar_need.decimals = max(self.wcfg["decimal_places_refill"], 0)

        # Estimated consumption
        bar_style_used = self.set_qss(
            fg_color=self.wcfg["font_color_used"],
            bg_color=self.wcfg["bkg_color_used"]
        )
        self.bar_used = self.set_qlabel(
            text=text_def,
            style=bar_style_used,
            fixed_width=style_width,
        )
        self.bar_used.decimals = max(self.wcfg["decimal_places_used"], 0)

        # Delta consumption
        bar_style_delta = self.set_qss(
            fg_color=self.wcfg["font_color_delta"],
            bg_color=self.wcfg["bkg_color_delta"]
        )
        self.bar_delta = self.set_qlabel(
            text=text_def,
            style=bar_style_delta,
            fixed_width=style_width,
        )
        self.bar_delta.decimals = max(self.wcfg["decimal_places_delta"], 0)

        # Fuel ratio consumption
        bar_style_ratio = self.set_qss(
            fg_color=self.wcfg["font_color_ratio"],
            bg_color=self.wcfg["bkg_color_ratio"]
        )
        self.bar_ratio = self.set_qlabel(
            text=text_def,
            style=bar_style_ratio,
            fixed_width=style_width,
        )
        self.bar_ratio.decimals = max(self.wcfg["decimal_places_ratio"], 0)

        # Estimate pit stop counts when pitting at end of current lap
        bar_style_early = self.set_qss(
            fg_color=self.wcfg["font_color_early"],
            bg_color=self.wcfg["bkg_color_early"]
        )
        self.bar_early = self.set_qlabel(
            text=text_def,
            style=bar_style_early,
            fixed_width=style_width,
        )
        self.bar_early.decimals = max(self.wcfg["decimal_places_early"], 0)

        # Estimated laps can last
        bar_style_laps = self.set_qss(
            fg_color=self.wcfg["font_color_laps"],
            bg_color=self.wcfg["bkg_color_laps"]
        )
        self.bar_laps = self.set_qlabel(
            text=text_def,
            style=bar_style_laps,
            fixed_width=style_width,
        )
        self.bar_laps.decimals = max(self.wcfg["decimal_places_laps"], 0)

        # Estimated minutes can last
        bar_style_mins = self.set_qss(
            fg_color=self.wcfg["font_color_minutes"],
            bg_color=self.wcfg["bkg_color_minutes"]
        )
        self.bar_mins = self.set_qlabel(
            text=text_def,
            style=bar_style_mins,
            fixed_width=style_width,
        )
        self.bar_mins.decimals = max(self.wcfg["decimal_places_minutes"], 0)

        # Estimated one less pit consumption
        bar_style_save = self.set_qss(
            fg_color=self.wcfg["font_color_save"],
            bg_color=self.wcfg["bkg_color_save"]
        )
        self.bar_save = self.set_qlabel(
            text=text_def,
            style=bar_style_save,
            fixed_width=style_width,
        )
        self.bar_save.decimals = max(self.wcfg["decimal_places_save"], 0)

        # Estimate pit stop counts when pitting at end of current stint
        bar_style_pits = self.set_qss(
            fg_color=self.wcfg["font_color_pits"],
            bg_color=self.wcfg["bkg_color_pits"]
        )
        self.bar_pits = self.set_qlabel(
            text=text_def,
            style=bar_style_pits,
            fixed_width=style_width,
        )
        self.bar_pits.decimals = max(self.wcfg["decimal_places_pits"], 0)

        # Fuel bias
        bar_style_bias = self.set_qss(
            fg_color=self.wcfg["font_color_bias"],
            bg_color=self.wcfg["bkg_color_bias"]
        )
        self.bar_bias = self.set_qlabel(
            text=text_def,
            style=bar_style_bias,
            fixed_width=style_width,
        )
        self.bar_bias.decimals = max(self.wcfg["decimal_places_bias"], 0)

        # Energy level bar
        if self.wcfg["show_energy_level_bar"]:
            self.bar_level = FuelLevelBar(
                self,
                width=(font_m.width * self.bar_width + bar_padx) * 6,
                height=max(self.wcfg["energy_level_bar_height"], 1),
                start_mark_width=max(self.wcfg["starting_energy_level_mark_width"], 1),
                refill_mark_width=max(self.wcfg["refilling_level_mark_width"], 1),
                input_color=self.wcfg["highlight_color_energy_level"],
                bg_color=self.wcfg["bkg_color_energy_level"],
                start_mark_color=self.wcfg["starting_energy_level_mark_color"],
                refill_mark_color=self.wcfg["refilling_level_mark_color"],
                show_start_mark=self.wcfg["show_starting_energy_level_mark"],
                show_refill_mark=self.wcfg["show_refilling_level_mark"],
            )
            layout.addWidget(self.bar_level, self.wcfg["column_index_middle"], 0)

        # Set layout
        layout_upper.addWidget(self.bar_pits, 1, 0)
        layout_upper.addWidget(self.bar_curr, 1, 1)
        layout_upper.addWidget(self.bar_need, 1, 2)
        layout_upper.addWidget(self.bar_used, 1, 3)
        layout_upper.addWidget(self.bar_delta, 1, 4)
        layout_upper.addWidget(self.bar_ratio, 1, 5)
        layout_lower.addWidget(self.bar_early, 1, 0)
        layout_lower.addWidget(self.bar_laps, 1, 1)
        layout_lower.addWidget(self.bar_mins, 1, 2)
        layout_lower.addWidget(self.bar_save, 1, 3)
        layout_lower.addWidget(self.bar_end, 1, 4)
        layout_lower.addWidget(self.bar_bias, 1, 5)

        # Last data
        self.warn_flash = WarningFlash(
            self.wcfg["warning_flash_highlight_duration"],
            self.wcfg["warning_flash_interval"],
            self.wcfg["number_of_warning_flashes"],
        )

    def timerEvent(self, event):
        """Update when vehicle on track"""
        is_low_energy = minfo.energy.estimatedLaps <= self.wcfg["low_energy_lap_threshold"]
        if self.wcfg["show_low_energy_warning_flash"] and minfo.energy.estimatedValidConsumption:
            is_low_energy = self.warn_flash.state(api.read.timing.elapsed(), is_low_energy)
            if is_low_energy:
                padding = 0.00000001  # add padding for switching state
            else:
                padding = 0
        else:
            padding = 0

        # Estimated end remaining
        amount_end = minfo.energy.amountEndStint
        self.update_energy(self.bar_end, amount_end)

        # Remaining
        amount_curr = minfo.energy.amountCurrent
        self.update_energy(self.bar_curr, amount_curr + padding, self.bar_style_curr[is_low_energy])

        # Total needed
        if self.wcfg["show_absolute_refilling"]:
            amount_need = calc.sym_max(minfo.energy.neededAbsolute, 9999)
            self.update_energy(self.bar_need, amount_need + padding, self.bar_style_need[is_low_energy])
        else:
            amount_need = calc.sym_max(minfo.energy.neededRelative, 9999)
            self.update_energy(self.bar_need, amount_need + padding, self.bar_style_need[is_low_energy], "+")

        # Estimated consumption
        used_last = minfo.energy.estimatedConsumption
        self.update_energy(self.bar_used, used_last)

        # Delta consumption
        delta_energy = minfo.energy.deltaConsumption
        self.update_energy(self.bar_delta, delta_energy, None, "+")

        # Fuel ratio
        fuel_ratio = minfo.hybrid.fuelEnergyRatio
        self.update_energy(self.bar_ratio, fuel_ratio)

        # Estimate pit stop counts when pitting at end of current lap
        est_pits_early = calc.zero_max(minfo.energy.estimatedNumPitStopsEarly, 99.99)
        self.update_energy(self.bar_early, est_pits_early)

        # Estimated laps can last
        est_runlaps = min(minfo.energy.estimatedLaps, 9999)
        self.update_energy(self.bar_laps, est_runlaps)

        # Estimated minutes can last
        est_runmins = min(minfo.energy.estimatedMinutes, 9999)
        self.update_energy(self.bar_mins, est_runmins)

        # Estimated one less pit consumption
        energy_save = calc.zero_max(minfo.energy.oneLessPitConsumption, 99.99)
        self.update_energy(self.bar_save, energy_save)

        # Estimate pit stop counts when pitting at end of current stint
        est_pits_end = calc.zero_max(minfo.energy.estimatedNumPitStopsEnd, 99.99)
        self.update_energy(self.bar_pits, est_pits_end)

        # Fuel bias
        fuel_bias = minfo.hybrid.fuelEnergyBias
        self.update_energy(self.bar_bias, fuel_bias, None, "+")

        # Energy level bar
        if self.wcfg["show_energy_level_bar"]:
            level_capacity = minfo.energy.capacity
            level_curr = minfo.energy.amountCurrent
            level_start = minfo.energy.amountStart
            level_refill = level_curr + minfo.energy.neededRelative
            level_state = round(level_curr + level_start + level_refill, 3)
            if level_capacity and self.bar_level.last != level_state:
                self.bar_level.last = level_state
                self.bar_level.update_input(
                    level_curr / level_capacity,
                    level_start / level_capacity,
                    level_refill / level_capacity,
                )

    # GUI update methods
    def update_energy(self, target, data, color=None, sign=""):
        """Update energy data"""
        if target.last != data:
            target.last = data
            text = f"{data:{sign}.{target.decimals}f}"[:self.bar_width].strip(".")
            target.setText(text)
            if color:  # low energy warning
                target.updateStyle(color)
