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
Vehicles module
"""

from __future__ import annotations

from .. import calculation as calc
from ..api_control import api
from ..const_common import MAX_METERS, MAX_SECONDS, MAX_VEHICLES
from ..module_info import VehiclesInfo, minfo
from ._base import DataModule

ALL_INDEXES = list(range(MAX_VEHICLES))


class Realtime(DataModule):
    """Vehicles info"""

    __slots__ = ()

    def __init__(self, config, module_name):
        super().__init__(config, module_name)

    def update_data(self):
        """Update module data"""
        _event_wait = self._event.wait
        reset = False
        update_interval = self.active_interval

        output = minfo.vehicles
        max_lap_diff_ahead = self.mcfg["lap_difference_ahead_threshold"]
        max_lap_diff_behind = self.mcfg["lap_difference_behind_threshold"]

        while not _event_wait(update_interval):
            if self.state.active:

                if not reset:
                    reset = True
                    update_interval = self.active_interval
                    output.dataSetVersion = -1

                self.__update_vehicle_data(
                    output,
                    minfo.relative.classes,
                    minfo.relative.qualifications,
                    max_lap_diff_ahead,
                    max_lap_diff_behind
                )

            else:
                if reset:
                    reset = False
                    update_interval = self.idle_interval

    def __update_vehicle_data(
        self,
        output: VehiclesInfo,
        class_pos_list: list,
        qual_pos_list: list[tuple[int, int]],
        max_lap_diff_ahead: float,
        max_lap_diff_behind: float,
    ):
        """Update vehicle data"""
        veh_total = output.total = api.read.vehicle.total_vehicles()
        if veh_total < 1:
            return

        # General data
        track_length = api.read.lap.track_length()
        in_race = api.read.session.in_race()
        draw_order = ALL_INDEXES[:veh_total]
        laptime_best_leader = 0.0

        # Local player data
        plr_laps_done = api.read.lap.completed_laps()
        plr_lap_distance = api.read.lap.distance()
        plr_lap_progress = calc.lap_progress_distance(plr_lap_distance, track_length)
        plr_laptime_est = api.read.timing.estimated_laptime()
        plr_timeinto_est = api.read.timing.estimated_time_into()
        nearest_line = MAX_METERS
        nearest_time_behind = -MAX_SECONDS
        nearest_yellow = MAX_METERS

        # Sorting reference index
        leader_index = 0
        player_index = -1  # local player may not exist, init with -1
        inpit_index = 0

        # Update dataset from all vehicles in current session
        for index, data, class_pos, qual_pos in zip(range(veh_total), output.dataSet, class_pos_list, qual_pos_list):
            # Vehicle class var
            opt_index_ahead = class_pos[4]
            data.positionInClass = class_pos[1]
            data.classBestLapTime = class_pos[3]
            data.isClassFastestLastLap = class_pos[6]
            data.qualifyOverall = qual_pos[0]
            data.qualifyInClass = qual_pos[1]

            # Temp var only
            lap_etime = api.read.timing.elapsed(index)
            speed = api.read.vehicle.speed(index)
            laps_done = api.read.lap.completed_laps(index)
            lap_distance = api.read.lap.distance(index)
            num_penalties = api.read.vehicle.number_penalties(index)

            # Temp & output var
            is_player = data.isPlayer = api.read.vehicle.is_player(index)
            class_name = data.vehicleClass = api.read.vehicle.class_name(index)
            position_overall = data.positionOverall = api.read.vehicle.place(index)
            in_pit = data.inPit = 2 if api.read.vehicle.in_garage(
                index) else api.read.vehicle.in_pits(index) # 0 not in pit, 1 in pit, 2 in garage
            is_yellow = data.isYellow = speed < 8
            lap_progress = data.lapProgress = calc.lap_progress_distance(lap_distance, track_length)
            laptime_last = data.lastLapTime = api.read.timing.last_laptime(index)

            # Output var only
            data.driverName = api.read.vehicle.driver_name(index)
            data.vehicleName = api.read.vehicle.vehicle_name(index)
            data.gapBehindNext = calc_gap_behind_next(index)
            data.gapBehindLeader = calc_gap_behind_leader(index)
            data.bestLapTime = api.read.timing.best_laptime(index)
            data.numPitStops = -num_penalties if num_penalties else api.read.vehicle.number_pitstops(index)
            data.pitState = api.read.vehicle.pit_request(index)
            data.tireCompoundFront = f"{class_name} - {api.read.tyre.compound_name_front(index)}"
            data.tireCompoundRear = f"{class_name} - {api.read.tyre.compound_name_rear(index)}"
            data.gapBehindNextInClass = calc_gap_behind_next_in_class(
                opt_index_ahead, index, track_length, laps_done, lap_progress)
            data.pitTimer.update(in_pit, lap_etime)
            data.update_lap_history(api.read.timing.start(index), lap_etime, laptime_last)

            # Position & relative data
            opt_pos_x = data.worldPositionX = api.read.vehicle.position_longitudinal(index)
            opt_pos_y = data.worldPositionY = api.read.vehicle.position_lateral(index)
            if is_player:
                if is_yellow:
                    nearest_yellow = 0.0
            else:
                # Relative position & orientation
                plr_pos_x = api.read.vehicle.position_longitudinal()
                plr_pos_y = api.read.vehicle.position_lateral()
                plr_ori_yaw = api.read.vehicle.orientation_yaw_radians()
                opt_ori_yaw = api.read.vehicle.orientation_yaw_radians(index)

                data.relativeOrientationRadians = opt_ori_yaw - plr_ori_yaw
                data.relativeRotatedPositionX, data.relativeRotatedPositionY = calc.rotate_coordinate(
                    plr_ori_yaw - 3.14159265,  # plr_ori_rad, rotate view
                    opt_pos_x - plr_pos_x,     # x position related to player
                    opt_pos_y - plr_pos_y)     # y position related to player

                # Relative distance & time gap
                relative_straight_distance = data.relativeStraightDistance = calc.distance(
                    (plr_pos_x, plr_pos_y), (opt_pos_x, opt_pos_y))
                data.isLapped = calc.lap_difference(
                    laps_done + lap_progress, plr_laps_done + plr_lap_progress,
                    max_lap_diff_ahead, max_lap_diff_behind
                ) if in_race else 0

                # Nearest straight line distance (non local players)
                if nearest_line > relative_straight_distance:
                    nearest_line = relative_straight_distance
                # Nearest traffic time gap (opponents behind local players)
                if not in_pit:
                    opt_time_behind = calc.circular_relative_distance(
                        plr_laptime_est, plr_timeinto_est, api.read.timing.estimated_time_into(index))
                    if 0 > opt_time_behind > nearest_time_behind:
                        nearest_time_behind = opt_time_behind
                # Nearest yellow flag distance
                if is_yellow and nearest_yellow > 0:
                    opt_rel_distance = abs(calc.circular_relative_distance(
                        track_length, plr_lap_distance, lap_distance))
                    if nearest_yellow > opt_rel_distance:
                        nearest_yellow = opt_rel_distance

            # Sort draw order list in loop ->
            if position_overall == 1:  # save leader index
                leader_index = index
                laptime_best_leader = data.bestLapTime
                if is_player:  # player can be leader at the same time
                    player_index = index
            elif is_player:  # save local player index
                player_index = index
            elif in_pit:  # swap opponent in pit/garage to start
                draw_order[index], draw_order[inpit_index] = draw_order[inpit_index], draw_order[index]
                inpit_index += 1

        # Finalize draw order list ->
        # Move leader to end of draw order
        if leader_index != draw_order[-1]:
            leader_pos = draw_order.index(leader_index)
            draw_order[leader_pos], draw_order[-1] = draw_order[-1], draw_order[leader_pos]
        # Move local player to 2nd end of draw order if exists and not leader
        if -1 != player_index != leader_index:
            player_pos = draw_order.index(player_index)
            draw_order[player_pos], draw_order[-2] = draw_order[-2], draw_order[player_pos]
        # <- End draw order list

        # Output extra info
        output.leaderIndex = leader_index
        output.playerIndex = player_index
        output.nearestLine = nearest_line
        output.nearestTraffic = -nearest_time_behind
        output.nearestYellow = nearest_yellow
        output.leaderBestLapTime = laptime_best_leader
        output.drawOrder = draw_order
        output.dataSetVersion += 1


def calc_gap_behind_next_in_class(
    opt_index: int, index: int, track_length: float, laps_done: float, lap_progress: float):
    """Calculate interval behind next in class"""
    if opt_index < 0:
        return 0.0
    opt_laps_done = api.read.lap.completed_laps(opt_index)
    opt_lap_distance = api.read.lap.distance(opt_index)
    opt_lap_progress = calc.lap_progress_distance(opt_lap_distance, track_length)
    lap_diff = abs(opt_laps_done + opt_lap_progress - laps_done - lap_progress)
    if lap_diff > 1:
        return int(lap_diff)
    return abs(calc.circular_relative_distance(
        api.read.timing.estimated_laptime(index),
        api.read.timing.estimated_time_into(index),
        api.read.timing.estimated_time_into(opt_index),
    ))


def calc_gap_behind_next(index: int):
    """Calculate interval behind next"""
    laps_behind_next = api.read.lap.behind_next(index)
    if laps_behind_next > 0:
        return laps_behind_next
    return api.read.timing.behind_next(index)


def calc_gap_behind_leader(index: int):
    """Calculate interval behind leader"""
    laps_behind_leader = api.read.lap.behind_leader(index)
    if laps_behind_leader > 0:
        return laps_behind_leader
    return api.read.timing.behind_leader(index)
