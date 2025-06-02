**Note: following guide is updated to match latest released version.**

TinyPedal offers a wide range of customization options for `widget` and `module` controls, which can be accessed from corresponding tabs in main window.

# Global user configuration
TinyPedal stores global user configuration in `config.json` file, which is used for none-preset specific options.

* For Windows, `config.json` is stored under `username\AppData\Roaming\TinyPedal` folder.
* For Linux, `config.json` is stored under `home/username/.config/TinyPedal` folder.

Available settings:

* `Application`, can be accessed from `Config` menu in main window, see [Application](#application) section for details.
* `Compatibility`, can be accessed from `Config` menu in main window, see [Compatibility](#compatibility) section for details.
* `User path`, can be accessed from `Config` menu in main window, see [User Path](#user-path) section for details.
* `Auto load preset`, can be accessed from `Preset` tab in main window, see [Preset Management](#preset-management) section for details.

Reload or Restart:

* To reload all presets, select `Reload` from `Overlay` menu in main window.
* To restart game API, select `Restart API` from `Overlay` menu in main window.
* To restart TinyPedal, select `Restart TinyPedal` from `Window` menu in main window.

[**`Back to Top`**](#)


# Preset management
TinyPedal stores all customization options in `JSON` format preset files, and can be managed from `Preset` tab in main window.

All user preset files, by default, are located in `TinyPedal\settings` folder. Those `JSON` files can also be manually edited with text editor.

`Right-Click` on a preset name in `Preset` tab opens up a context menu that provides additional preset file management options:

* Lock Preset  
    Lock selected preset, which prevents any changes that made through TinyPedal from saving to locked preset file. APP `version` tag will be attached to the preset that is locked with.

    Note, this feature does not prevent user from modifying or deleting locked preset file by other means. Locked preset file info is stored in `config.lock` file in [Global User Configuration](#global-user-configuration) folder.

* Unlock Preset  
    Unlock selected preset.

* Set primary for *  
    Add `primary sim` tag to selected preset, which will be auto loaded by `Auto load preset` system. Note, a single preset can have tags from multiple games.

* Clear primary tag  
    Clear all tags from selected preset.

* Duplicate  
    Duplicate selected preset with a new name.

* Rename  
    Rename selected preset with a new name. This option is not available for locked preset.

* Delete  
    Delete selected preset with confirmation. This option is not available for locked preset.

[**`Back to Top`**](#)


## Saving JSON file
TinyPedal automatically saves setting when user makes changes to widget position, or has toggled widget visibility, auto-hide, overlay-lock, etc. Changes will only take effect after `Reload` preset, or clicked `Save` or `Apply` button in `Config` dialog, or `Restart` APP.

[**`Back to Top`**](#)


## Backup JSON file
TinyPedal will automatically create backup file with time stamp suffix if old setting file fails to load, and new default `JSON` with same filename will be generated.

A newer released version will auto-update old setting and add new setting after loading. It may still be a good idea to manually backup files before upgrading to newer version.

[**`Back to Top`**](#)


## Editing JSON file
Customization can be done through various configuration dialogs and menus from main window. Manual editing `JSON` file is not recommended.

[**`Back to Top`**](#)


## Brands preset
**Brands preset is used for customizing brand name that matches specific vehicle name.**

Brands preset can be customized by accessing `Vehicle brand editor` from `Tools` menu in main window. See [Vehicle Brand Editor](#vehicle-brand-editor) section for complete editing guide.

`brands.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


## Classes preset
**Classes preset is used for customizing class name and color that matches specific vehicle class.**

Classes preset can be customized by accessing `Vehicle class editor` from `Tools` menu in main window. See [Vehicle Class Editor](#vehicle-class-editor) section for complete editing guide.

`classes.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


## Brakes preset
**Brakes preset is used for customizing brake failure thickness and heatmap style that matches specific vehicle class.**

Brakes preset can be customized by accessing `Brake editor` from `Tools` menu in main window. See [Brake Editor](#brake-editor) section for complete editing guide.

`brakes.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


## Compounds preset
**Compounds preset is used for customizing tyre compound symbol and heatmap style that matches specific tyre compound.**

Compounds preset can be customized by accessing `Tyre compound editor` from `Tools` menu in main window. See [Tyre Compound Editor](#tyre-compound-editor) section for complete editing guide.

`compounds.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


## Heatmap preset
**Heatmap preset is used for customizing heatmap color that matches specific value range of telemetry data, such as brake and tyre temperature.**

Heatmap preset can be customized by accessing `Heatmap editor` from `Tools` menu in main window. See [Heatmap Editor](#heatmap-editor) section for complete editing guide.

`heatmap.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


## Tracks preset
**Tracks preset is used for storing and customizing track info for various track-related calculation.**

Tracks preset can be customized by accessing `Track info editor` from `Tools` menu in main window. See [Track Info Editor](#track-info-editor) section for complete editing guide.

Track info recording is handled by [Mapping Module](#mapping-module).

`tracks.json` preset will be generated and saved in `TinyPedal\settings` folder after first time launch of the APP.

[**`Back to Top`**](#)


# User files
TinyPedal generates and saves user session data in specific folders defined in `User path`. Session data can be reset by accessing `Reset data` menu from `Overlay` menu in main window; or, delete data file from corresponding folder.

[**`Back to Top`**](#)


## Driver stats
Driver stats data is stored as `JSON` format (.stats extension) under [Global User Configuration](#global-user-configuration) folder. Driver stats can be viewed with [Driver Stats Viewer](#driver-stats-viewer) from `Tools` menu in main window.

Data recording is handled by [Stats Module](#stats-module).

[**`Back to Top`**](#)


## Delta best
Delta best data is stored as `CSV` format (.csv extension) under `TinyPedal\deltabest` folder (default). Those files can be opened in spreadsheet or notepad programs.

Data recording is handled by [Delta Module](#delta-module).

[**`Back to Top`**](#)


## Energy delta
Energy delta data is stored as `CSV` format (.energy extension) under `TinyPedal\deltabest` folder (default). Those files can be opened in spreadsheet or notepad programs.

Data recording is handled by [Energy Module](#energy-module).

[**`Back to Top`**](#)


## Fuel delta
Fuel delta data is stored as `CSV` format (.fuel extension) under `TinyPedal\deltabest` folder (default). Those files can be opened in spreadsheet or notepad programs.

Data recording is handled by [Fuel Module](#fuel-module).

[**`Back to Top`**](#)


## Consumption history
Consumption history data is stored as `CSV` format (.consumption extension) under `TinyPedal\deltabest` folder (default). Those files can be opened in spreadsheet or notepad programs.

Consumption history data stores lap time and fuel consumption data per `track and vehicle class`, which can be loaded in [Fuel Calculator](#fuel-calculator). Up to 100 most recent lap entries are saved per `track and vehicle class`. Data recording is handled by [Fuel Module](#fuel-module).

[**`Back to Top`**](#)


## Sector best
Sector best data is stored as `CSV` format (.sector extension) under `TinyPedal\deltabest` folder (default). Those files can be opened in spreadsheet or notepad programs.

Data recording is handled by [Sectors Module](#sectors-module).

[**`Back to Top`**](#)


## Track map
Track map is stored as `SVG` vector image format (.svg extension) under `TinyPedal\trackmap` folder (default). Track map can be viewed with [Track Map Viewer](#track-map-viewer) from `Tools` menu in main window.

Data recording is handled by [Mapping Module](#mapping-module).

The SVG vector map data contains two coordinate paths:
* First is global x,y position path, used for drawing track map.
* Second is corresponding track distance and elevation path, used for drawing elevation plot.

Each sector position index is also stored in SVG file for finding sector coordinates.

[**`Back to Top`**](#)


## Pace notes
`TinyPedal Pace Notes` data is stored as `TPPN` format (.tppn extension) under `TinyPedal\pacenotes` folder (default). Pace notes can be created or edited with [Track Notes Editor](#track-notes-editor) from `Tools` menu in main window.

Pace notes data is mainly used for [Pace Notes Playback](#pace-notes-playback) for specific tracks.

To allow `auto notes loading` function to work, pace notes file name must match same track map file name.

[**`Back to Top`**](#)


## Track notes
`TinyPedal Track Notes` data is stored as `TPTN` format (.tptn extension) under `TinyPedal\tracknotes` folder (default). Track notes can be created or edited with [Track Notes Editor](#track-notes-editor) from `Tools` menu in main window.

Track notes data is mainly used for displaying corner and section names for specific tracks, or providing additional info at specific track location while driving.

To allow `auto notes loading` function to work, track notes file name must match same track map file name.

[**`Back to Top`**](#)


## Brand logo
TinyPedal supports user-defined brand logo image in `PNG` format (.png extension) which is placed under `TinyPedal\brandlogo` folder (default).

Note: TinyPedal does not provide brand logo image assets, it is up to user to prepare images. Maximum `PNG` file size is limited to `1MB`.

How to prepare brand logo image:  
1. Brand logo image should have all transparent borders cropped. For example, in `GIMP` this can be done by selecting `Image` > `Crop to Content`.
2. Make sure image dimension is not too big, usually around 100 pixel width or height is good enough. Bigger dimension may consume more RAM or exceed maximum supported file size.
3. Save image to `TinyPedal\brandlogo` folder, image filename must match corresponding `brand name` that defined in [Vehicle Brand Editor](#vehicle-brand-editor). For cross-platform compatibility, filename matching is set to be case-sensitive, make sure filename has the same upper or lower case as set in `brand name`.
4. `Reload` preset to load newly added brand logo images for displaying in overlay.

[**`Back to Top`**](#)


# Command line arguments
**Command line arguments can be passed to script or executable to enable additional features.**

    -h, --help
List all available command line arguments.

Usage: `python .\run.py -h` or `.\tinypedal.exe --help`

    -l, --log-level
Set logging output level. Supported values are:
  * `--log-level 0` outputs only warning or error log to `console`.
  * `--log-level 1` outputs all log to `console`.
  * `--log-level 2` outputs all log to both `console` and `tinypedal.log` file.

Log location:
  * On windows, `tinypedal.log` is located under `username\AppData\Roaming\TinyPedal` folder.
  * On Linux, `tinypedal.log` is located under `home/username/.config/TinyPedal` folder.

Default logging output level is set on `1` if argument is not set.

Usage: `python .\run.py -l 2` or `.\tinypedal.exe --log-level 2`

    -s, --single-instance
Set running mode. `0` allows running multiple instances (copies) of TinyPedal. `1` allows only single instance (default).

To run multiple copies of TinyPedal at same time: `python .\run.py -s 0` or `.\tinypedal.exe --single-instance 0`

Single instance mode saves `pid.log` file in the same folder as `tinypedal.log`, which is used for instance identification.

    -p, --pyside
Set PySide (Qt for Python) module version. Set `2` for PySide2 (default). Set `6` for PySide6. Currently, this option is only available while `running from source`, and mainly for testing purpose or used on platform where PySide2 is no longer available.

[**`Back to Top`**](#)


# General options
**General options can be accessed from main window menu.**

[**`Back to Top`**](#)


## Common terms and keywords
**These are the commonly used setting terms and keywords.**

    enable
Check whether a widget or module will be loaded at startup.

    update_interval
Set refresh rate for widget or module in milliseconds. A value of `20` means refreshing every 20ms, which equals 50fps. Since most data from sharedmemory plugin is capped at 50fps, and most operation system has a roughly 15ms minimum sleep time, setting value less than `10` has no benefit, and extreme low value may result significant increase of CPU usage.

    idle_update_interval
Set refresh rate for module while idling for conserving resources.

    position_x, position_y
Define widget position on screen in pixels. Those values will be auto updated and saved.

    opacity
Set opacity for entire widget. By default, all widgets have a 90% opacity setting, which equals value `0.9`. Lower value adds more transparency to widget. Acceptable value range in `0.0` to `1.0`. Note, opacity can also be set by adjusting alpha value in `color` options for individual elements.

    bar_gap, inner_gap
Set gap (screen pixel) between elements in a widget, only accept integer, `1` = 1 pixel.

    font_name
Mono type font is highly recommended. To set custom font, write `full font name` inside quotation marks. If a font name is invalid, a default fallback font will be used by program.

    font_size
Set font size in pixel, increase or decrease font size will also apply to widget size.

    font_weight
Acceptable value: `normal` or `bold`.

    enable_auto_font_offset
Automatically adjust font vertical offset based on font geometry for better vertical alignment, and should give good result in most case. This option is enabled by default, and only available to certain widgets. Set `false` to disable.

    font_offset_vertical
Manually set font vertical offset. Default is `0`. Negative value will offset font upward, and position value for downward. This option only takes effect when `enable_auto_font_offset` is set to `false`.

    *_offset_x, *_offset_y
Set text offset position (percentage), value range in `0.0` to `1.0`.

    bar_padding
Set widget edge padding value that multiplies and scales with `font_size`. Default is `0.2` for most widgets. Increase padding value will further increase each element width in widget.

    color
Set color in hexadecimal color codes with alpha value (opacity). The color code format starts with `#`, then follows by two-digit hexadecimal numbers for each channel in the order of `alpha`, `red`, `green`, `blue`. Note, `alpha` is optional and can be omitted. User can select a new color without manual editing, by double-clicking on color entry box in `Config` dialog.

    text_alignment
Set text alignment. Acceptable value: `Left`, `Center`, `Right`.

    prefix
Set prefix text that displayed beside corresponding data. Set to `""` to hide prefix text.

    show_caption
Show short caption description on widget.

    column_index
Set order of each info column(or row). Must keep index number unique to each column, otherwise columns may overlap.

    decimal_places
Set amount decimal places to keep.

[**`Back to Top`**](#)


## Application
**Application options can be accessed from `Config` and `Window` menu in main window.**

    show_at_startup
Show main window at startup, otherwise hides to tray icon.

    minimize_to_tray
Minimize to tray when user clicks `X` close button.

    remember_position
Remember main window last position.

    remember_size
Remember main window last size.

    enable_high_dpi_scaling
Enable window dialog and overlay widget auto-scaling under high DPI screen resolution. This option requires restarting TinyPedal to take effect. This option is disabled by default.

High DPI scaling mode can be quickly toggled via `Scale` button on main window status bar.

On Windows, scaling is determined by percentage value set in `Display` > `Scale and Layout` setting. For example, `200%` scale in windows setting will double the size of main window dialog and also every widget.

On Linux, DPI scaling may already be forced `ON` in some system, which this option may not have effect.

    enable_auto_load_preset
Enable `Auto load preset` system to allow auto loading user-defined game-specific preset depends on active game (currently supports `RF2` and `LMU`).

Auto loading preset is triggered when a new or different game is started and active. Auto loading will only trigger once per game change. A preset must be tagged as `primary` for specific game before it can be auto loaded. See [Preset Management](#preset-management) section for details.

This option is disabled by default.

    show_confirmation_for_batch_toggle
Show confirmation dialog for enabling or disabling all widgets or modules. This option is enabled by default.

    grid_move_size
Set grid size for grid move, value in pixel. Default is `8` pixel. Minimum value is limited to `1`.

    minimum_update_interval
Set minimum refresh rate limit for widget and module in milliseconds. This option is used for preventing extremely low refresh rate that may cause performance issues in case user incorrectly sets `update_interval` and `idle_update_interval` values. Default value is `10`, and should not be modified.

    maximum_saving_attempts
Set maximum retry attempts for preset saving. Default value is `10`. Minimum value is limited to `3` maximum attempts. Note, each attempt has a roughly 50ms delay. If all saving attempts failed, saving will be aborted, and old preset file will be restored to avoid preset file corruption.

    position_x, position_y
Define main window position on screen in pixels. Those values will be auto updated and saved while `remember_position` option is enabled.

    window_width, window_height
Define main window size on screen in pixels. Those values will be auto updated and saved while `remember_size` option is enabled.

    window_color_theme
Set color theme for main window and dialog. Default theme is `Dark`. This option does not affect overlay widget.

Color theme can be quickly toggled via `UI` button on main window status bar.

[**`Back to Top`**](#)


## Compatibility
**Compatibility options can be accessed from `Config` menu in main window.**

    enable_bypass_window_manager
Set `true` to bypass window manager on Linux. This option does not affect windows system. This option is enabled by default on Linux. Note, while this option is enabled, OBS may not be able to capture overlay widgets in streaming on Linux.

    enable_translucent_background
Set `false` to disable translucent background.

    enable_window_position_correction
Set `true` to enable main application window position correction, which is used to correct window-off-screen issue with multi-screen. This option is enabled by default.

    enable_x11_platform_plugin_override
Set Qt platform plugin type to `X11` via environment variable on Linux. This option may help work around some issues with overlay dragging and position on `Wayland`. This option requires restarting TinyPedal to take effect. This option is enabled by default on Linux.

    global_bkg_color
Sets global background color for all widgets.

Note, global background color will only be visible when `enable_translucent_background` option is disabled or translucent background is not supported. Some widgets with own background setting may override this option.

    multimedia_plugin_on_windows
Set multimedia plugin for playing sound file on windows. Default is using `WMF` plugin.

Note, if the option is set on `DirectShow`, additional audio decoder software may be required to play certain sound formats, such as `MP3`. This option requires restarting TinyPedal to take effect.

[**`Back to Top`**](#)


## User path
**User path options can be accessed from `Config` menu in main window.**

User path dialog allows customization to global user path for storing different user data.

To change user path, double-clicking on edit box to open `Select folder` dialog; or manually editing path text. Folder will be automatically created if does not exist.

Click `Apply` or `Save` button to verify and apply new paths. Invalid path will not be applied.

**Notes to relative and absolute path**

User path that sets inside TinyPedal root folder will be automatically converted to relative path. Relative path is not considered global path, and does not share data between multiple copies of TinyPedal. This is done to retain portability and compatibility with old version.

To share user path across multiple copies of TinyPedal, user must set path to place outside TinyPedal APP root folder.

**Default user path**

* On windows, all user paths are set inside TinyPedal root folder as relative paths:

        brandlogo/
        deltabest/
        settings/
        trackmap/
        pacenotes/
        tracknotes/

* On Linux, all user paths are set outside TinyPedal root folder as absolute paths:

        home/username/.config/TinyPedal/brandlogo/
        home/username/.config/TinyPedal/settings/
        home/username/.config/TinyPedal/pacenotes/
        home/username/.config/TinyPedal/tracknotes/
        home/username/.local/share/TinyPedal/deltabest/
        home/username/.local/share/TinyPedal/trackmap/

[**`Back to Top`**](#)


## Overlay
**Overlay options can be accessed from `Overlay` menu in main window, or from tray icon menu.**

    fixed_position
Check whether widget is locked at startup. This setting can be toggled from tray icon menu.

    auto_hide
Check whether auto hide is enabled. This setting can be toggled from tray icon menu.

    enable_grid_move
Enable grid-snap effect while moving widget for easy alignment and repositioning.

    vr_compatibility
Enable widget visibility as windows on taskbar in order to be used in VR via APPs such as `OpenKneeboard`. Non-VR user should not enable this option.

Note, you will still need a third party program (such as `OpenKneeboard`) to project overlay windows (widgets) into VR.

[**`Back to Top`**](#)


## Shared memory API
**Shared Memory API options can be accessed from `Config` menu in main window. Some options may only be relevant to certain API.**

    api_name
Set API name for accessing data from supported API.

| API name | Requirement |
|:-:|---|
| rFactor 2 | Requires `rF2 Shared Memory Map Plugin` to work. |
| Le Mans Ultimate | Currently a placehoder, the underlying code uses the same RF2 API which requires `rF2 Shared Memory Map Plugin` to work. |

    access_mode
Set access mode for API. Mode value `0` uses copy access and additional data check to avoid data desynchronized or interruption issues. Mode value `1` uses direct access, which may result data desynchronized or interruption issues. Default mode is copy access.

    process_id
Set process ID string for accessing API from server. Currently this option is only relevant to `RF2`.

    enable_active_state_override
Set `true` to enable `active state` manual override. While enabled, `overriding` notification will be shown on API status bar from main window.

    active_state
This option overrides local player on-track status check, and updates or stops overlay and data processing accordingly. Set `true` to activate state. Set `false` to deactivate state. This option works only when `enable_active_state_override` enabled.

    enable_player_index_override
Set `true` to enable `player index` manual override.

    player_index
Set `player index` override for displaying data from specific player. Valid player index range starts from `0` to max number players minus one, and must not exceed `127`. Set value to `-1` for unspecified player, which can be useful for display general standings and trackmap data (ex. broadcasting). This option works only when `enable_player_index_override` enabled.

    character_encoding
Set character encoding for displaying text in correct encoding. Available encoding: `UTF-8`, `ISO-8859-1`. Default encoding is `UTF-8`, which works best in `LMU` game. Note, `UTF-8` may not work well for some Latin characters in `RF2`, try use `ISO-8859-1` instead.

[**`Back to Top`**](#)


## Units
**Units options can be accessed from `Config` menu in main window.**

    distance_unit
2 unit types are available: `Meter`, `Feet`.

    fuel_unit
2 unit types are available: `Liter`, `Gallon`.

    odometer_unit
3 unit types are available: `Kilometer`, `Mile`, `Meter`.

    power_unit
3 unit types are available: `Kilowatt`, `Horsepower`, `Metric Horsepower`.

    speed_unit
3 unit types are available: `KPH`, `MPH`, `m/s`.

    temperature_unit
2 unit types are available: `Celsius`, `Fahrenheit`.

    turbo_pressure_unit
3 unit types are available: `bar`, `psi`, `kPa`.

    tyre_pressure_unit
3 unit types are available: `kPa`, `psi`, `bar`.

[**`Back to Top`**](#)


## Global font override
**Global font override options can be accessed from `Config` menu in main window, which allow changing font setting globally for all widgets.**

    Font Name
Select a font name to replace `font_name` setting of all widgets. Default selection is `no change`, which no changes will be applied.

    Font Size Addend
Set a value that will be added (or subtracted if negative) to `font_size` value of all widgets. Default is `0`, which no changes will be applied.

    Font Weight
Set font weight to replace `font_weight` setting of all widgets. Default selection is `no change`, which no changes will be applied.

[**`Back to Top`**](#)


## Spectate mode
**Spectate mode can be accessed from `Spectate` tab in main window.**

Click `Enabled` or `Disabled` button to toggle spectate mode on and off. Note, spectate mode can also be enabled by setting `enable_player_index_override` option to `true` in [Shared Memory API](#shared-memory-api) config.

While Spectate mode is enabled, `double-click` on a player name in the list to access telemetry data and overlay readings from selected player; alternatively, select a player name and click `Spectate` button. Current spectating player name is displayed on top of player name list.

Select `Anonymous` for unspecified player, which is equivalent to player index `-1` in JSON file.

Click `Refresh` button to manually refresh player name list.

[**`Back to Top`**](#)


## Pace notes playback
**Pace notes playback control panel can be accessed from `Pace Notes` tab in main window.**

Note, [Notes Module](#notes-module) must be enabled to allow pace notes playback.

Click `Playback Enabled` or `Playback Disabled` button to quickly enable or disable pace notes playback. Disabling this option does not affect `Notes Module` or `Pace notes Widget`.

Enable `Manually Select Pace Notes File` check box to disable auto-file-name matching, and manually select a pace notes file that can be played on any track. By default, pace notes file is automatically loaded from `pace_notes_path` if a file that matches current track name is found. This option takes immediate effect when changed.

`Sound file path` sets path for loading pace notes sound files that matches name value (exclude file extension) from `pace note` column found in pace notes file. If no sound file found, sound won't be played. This option takes immediate effect when changed.

`Sound format` sets sound format for loading sound file, which should match sound file extension. This option only takes effect after clicked `Apply` button.

`Global offset` adds global position offset (in meters) to current vehicle position on track, which affects when next pace note line will be played. This option only takes effect after clicked `Apply` button.

`Max duration` sets maximum playback duration for each sound file, which can be used to limit sound file maximum playing duration. Default duration is `10` seconds. This option only takes effect after clicked `Apply` button.

`Max Queue` sets maximum number of sound files in playback queues. Default is `5` sound files. This option only takes effect after clicked `Apply` button.

`Playback volume` sets output volume for sound file. This option takes immediate effect when adjusted.

[**`Back to Top`**](#)


# Tools
**Tools can be accessed from main window menu.**

[**`Back to Top`**](#)


## Fuel calculator
**Fuel calculator can be accessed from `Tools` menu in main window.**

On the left side is calculation panel, which handles `fuel` and `virtual energy` usage calculation and results display.

Fuel value and unit symbol depend on `Fuel Unit` setting from [Units](#units) config dialog, `L` = liter, `gal` = gallon. Virtual energy unit is `%` = percentage. Note, after changed `Fuel Unit` setting, it is required to close and reopen `Fuel calculator` in order to update units info for calculation.

On the right side is fuel consumption history table, which lists `lap number`, `lap time`, `fuel consumption`, `virtual energy consumption`, `battery drain`, `battery regen`, `tank capacity` data from [Consumption History](#consumption-history) data.
Invalid lap time or consumption data is highlighted in red.

Click `Load Live` button to load or update consumption history from live session to history table and automatically fill in latest data to calculator.

Click `Load File` button to load data from specific consumption history file to history table and automatically fill in latest data to calculator.

Loaded data source and track and class name will be displayed on status bar.

Select one or more `Time`, `Fuel`, `Energy`, `Tank` values from history table and click `Add selected data` button to send value to calculator.

Select multiple values from history table and click `Add selected data` button to calculate average reading of selected values and send to calculator.

    Lap time
Set lap time in `minutes` : `seconds` : `milliseconds` format. Values are automatically carried over between spin boxes when exceeded min or max value range. This value can be retrieved from `Time` column.

    Tank capacity
Set vehicle fuel tank capacity. This value can be retrieved from `Tank` column.

    Fuel consumption
Set fuel consumption per lap. This value can be retrieved from `Fuel` column.

    Energy consumption
Set virtual energy consumption per lap. This value can be retrieved from `Energy` column.

    Fuel ratio
Show fuel ratio between fuel and virtual energy consumption.

    Race minutes
Set race length in minutes for time-based race. Note, option is disabled if `Race laps` is set.

    Race laps
Set race length in laps for lap-based race. Note, option is disabled if `Race minutes` is set.

    Formation/Rolling
Set number of formation or rolling start laps.

    Average pit seconds
Set average pit stop time in seconds.

    Total race fuel, Total race energy
Show total required fuel or energy to finish race. First value is raw reading with decimal places, second value behind `≈` sign is rounded up integer reading.

    End stint fuel, End stint energy
Show remaining fuel or energy at the end of stint or race.

    Total Pit stops
Show total number of pit stops required to finish race. First value is raw reading with decimal places, second value behind `≈` sign is rounded up integer reading. Note, sometimes when `Average pit seconds` is set to longer duration, ceiling integer reading may be rounded up `2` units higher than raw reading, this is not an error. For example, it may show `5.978 ≈ 7` instead of `5.978 ≈ 6`, this is because when calculating from `6` pit stops, due to less amount time spent in pit stop compare to `7`, more fuel is required per pit stop which would exceed tank capacity, hence calculator adds 1 more pit stop.

    One less pit stop
Show theoretical fuel or energy consumption in order to make one less pit stop.

    Total laps
Show total laps can run based on `Total race fuel` or `Total race energy` value.

    Total minutes
Show total minutes can run based on `Total race fuel` or `Total race energy` value.

    Starting fuel, Starting energy
Set starting fuel or energy. This value is only used for calculating `Average refueling` or `Average replenishing` per pit stop. Maximum value cannot exceed `Tank capacity` for fuel, or `100%` for energy. If value is set to `0`, `Tank capacity` value will be used as starting fuel for `Average refueling` calculation.

    Average refueling, Average replenishing
Show average refueling or replenishing per pit stop, and display warning color if value exceeds `Tank capacity` (fuel) or `100%` (energy).

[**`Back to Top`**](#)


## Driver stats viewer
**Driver stats viewer can be accessed from `Tools` menu in main window.**

Driver stats viewer is used for viewing [Driver Stats](#driver-stats). Note, the viewer only allows limited reset or removal, stat value cannot be edited by design. Any changes will take immediate effect after confirmation, changes cannot be undone.

Driver stats are grouped under specific track name, which can be switched from track name selector on the top.

To sort by specific stat, click on corresponding column name. Stats are sorted by `personal best lap time` by default.

To view corresponding track map, click `View Map` button.

To reload stats data, click `Reload` button.

To delete all stats from a specific track, click `Delete` button.

To remove all stats from a specific vehicle, right-click on vehicle name and select `Remove Vehicle`.

To reset personal best lap time to default, right-click on personal best lap time and select `Reset Lap Time`.

`Vehicle` column is vehicle classification info, which is determined by `vehicle_classification` option in [Stats Module](#stats-module).

`PB` column is personal best lap time. This value can be reset via right-click menu.

`Km` column is total driven distance in kilometers. Note, `odometer_unit` setting from [Units](#units) affects how this column is displayed.

`Hours` column is total time spent in driving (only counts when vehicle speed higher than 1 m/s).

`Liter` column is total fuel consumed. Note, `fuel_unit` setting from [Units](#units) affects how this column is displayed.

`Valid` column is total valid laps completed.

`Invalid` column is total invalid laps completed.

`Penalties` column is total penalties received in race. Non-race penalties are not recorded.

`Races` column is total races completed.

`Wins` column is total races won.

`Podiums` column is total podiums from race.

Note, race completion and final standings stats are retrieved at the moment when local driver crossed finish line on final lap, it does not concern any post-race penalties or finish state from team mate.

[**`Back to Top`**](#)


## Vehicle brand editor
**Vehicle brand editor can be accessed from `Tools` menu in main window.**

Vehicle brand editor is used for editing [Brands Preset](#brands-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

For brand logo image preparation, see [Brand Logo](#brand-logo) section.

`Vehicle name` is full vehicle name that must match in-game vehicle name.

`Brand name` is custom brand name.

To import vehicle brand data from `Rest API`, click `Import from` menu, and select either `RF2 Rest API` or `LMU Rest API`. Note, game updates may introduce new vehicles, it is recommended to re-import after each game update to keep brand info updated.

**Important notes**

Game must be running in order to import from `Rest API`. Newly imported data will be appended on top of existing data, existing data will not be changed.

If importing fails while game is running, check if `URL Port` option in `RestAPI` module that matches `WebUI port` value that sets in `LMU` (UserData\player\Settings.JSON) or `RF2` (UserData\player\player.JSON) setting file. See [RestAPI Module](#restapi-module) section for details.

Alternatively, to import vehicle brand data from vehicle `JSON` file, click `Import from` menu, and select `JSON file`.

    How to manually export vehicle brand data from RF2 Rest API:
    1. Start RF2, then open following link in web browser:
    localhost:5397/rest/race/car
    2. Click "Save" button which saves vehicle data to JSON file.

    How to manually export vehicle brand data from LMU Rest API:
    1. Start LMU, then open following link in web browser:
    localhost:6397/rest/sessions/getAllVehicles
    2. Click "Save" button which saves vehicle data to JSON file.

    Note: importing feature is experimental. Maximum acceptable JSON file size is limited to "5MB".

To add new brand name, click `Add` button. Note, the editor can auto-detect and fill-in missing vehicle names found from current active session, existing data will not be changed.

To sort brand name in orders, click `Sort` button.

To remove a brand name, select a vehicle name and click `Delete` button.

To batch replace name, click `Replace` button.

To reset all brands setting to default, click `Reset` button; or manually delete `brands.json` preset.

[**`Back to Top`**](#)


## Vehicle class editor
**Vehicle class editor can be accessed from `Tools` menu in main window.**

Vehicle class editor is used for editing [Classes Preset](#classes-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

`Class name` column is full vehicle class name that must match in-game vehicle.

`Alias name` column is alternative name that replaces class name for displaying.

`Color` column is class color style (HEX code). Double-click on color to open color dialog.

To add new class, click `Add` button. Note, the editor can auto-detect and fill-in missing vehicle classes found from current active session, existing data will not be changed.

To sort class name in orders, click `Sort` button.

To remove class, select one or more rows and click `Delete`.

To reset all classes setting to default, click `Reset` button; or manually delete `classes.json` preset.

[**`Back to Top`**](#)


## Brake editor
**Brake editor can be accessed from `Tools` menu in main window.**

Brake editor is used for editing [Brakes Preset](#brakes-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

`Brake name` column is full vehicle class name plus brake name that must match in-game vehicle.

`Failure (mm)` column is millimeter thickness threshold at brake failure and affects brake wear calculation. See [Brake Wear](#brake-wear) widget for details.

`Heatmap name` column is heatmap style name selector. Click on heatmap selector to open drop down list and select a heatmap style.

To add new brake, click `Add` button. Note, the editor can auto-detect and fill-in missing brakes found from running vehicles in current active session, existing data will not be changed.

To sort brake name in orders, click `Sort` button.

To remove brake, select one or more rows and click `Delete`.

To reset all brakes setting to default, click `Reset` button; or manually delete `brakes.json` preset.

[**`Back to Top`**](#)


## Track info editor
**Track info editor can be accessed from `Tools` menu in main window.**

Track info editor is used for editing [Tracks Preset](#tracks-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

`Track name` column is full track name that must match in-game track.

`Pit entry (m)` column is pit entry position (in meters) relative to track length. This value is automatically recorded or updated by [Mapping Module](#mapping-module).

`Pit exit (m)` column is pit exit position (in meters) relative to track length. This value is automatically recorded or updated by [Mapping Module](#mapping-module).

`Pit speed (m/s)` column is pit lane speed limit (in meters per second). This value is automatically recorded or updated by [Mapping Module](#mapping-module). Note, vehicle pit limiter must be activated while in pit lane to allow recording speed limit.

To add new track, click `Add` button. Note, the editor can auto-detect and fill-in missing track found from current active session, existing data will not be changed.

To sort track name in orders, click `Sort` button.

To remove track, select one or more rows and click `Delete`.

To reset all tracks setting to default, click `Reset` button; or manually delete `tracks.json` preset.

[**`Back to Top`**](#)


## Tyre compound editor
**Tyre compound editor can be accessed from `Tools` menu in main window.**

Tyre compound editor is used for editing [Compounds Preset](#compounds-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

`Compound name` column is full vehicle class name plus full tyre compound name that must match in-game vehicle.

`Symbol` column is alternative symbol character that replaces full tyre compound name for displaying.

`Heatmap name` column is heatmap style name selector. Click on heatmap selector to open drop down list and select a heatmap style.

To add new tyre compound, click `Add` button. Note, the editor can auto-detect and fill-in missing tyre compounds found from running vehicles in current active session, existing data will not be changed.

To sort tyre compound name in orders, click `Sort` button.

To remove tyre compound, select one or more rows and click `Delete`.

To batch replace name, click `Replace` button.

To reset all tyre compounds setting to default, click `Reset` button; or manually delete `compounds.json` preset.

[**`Back to Top`**](#)


## Heatmap editor
**Heatmap editor can be accessed from `Tools` menu in main window.**

Heatmap editor is used for editing [Heatmap Preset](#heatmap-preset). Note, any changes will only be saved and take effect after clicking `Apply` or `Save` Button.

Each row represents a target temperature and corresponding color. First column is temperature degree value in `Celsius`, and up to one decimal place is kept. Second column is corresponding color (HEX code). Double-click on color to open color dialog.

To add temperature, click `Add` button.

To sort temperature list in orders, click `Sort` button.

To batch offset temperature values, select one or more temperature from `temperature` column, then click `Offset` button. Click `Scale Mode` check box to scale temperature values. Note, offset option will be reset to `0` each time after applying. Last applied offset value is displayed on top of dialog.

To remove a temperature, select one or more temperature and click `Remove` button.

To select a different heatmap preset, click `drop-down list` at top, and select a preset name. Note: by selecting a different preset, any changes to previously selected heatmap will be saved in cache, and only be saved to file after clicking `Apply` or `Save` Button.

To create a new heatmap preset, click `New` button. Note: only alphabetic characters, numbers, underscores are accepted in preset name, and renaming preset is not supported.

To duplicate a heatmap preset, click `Copy` button.

To delete selected heatmap preset, click `Delete` button. Note: built-in presets cannot be deleted.

To reset selected heatmap preset, click `Reset` button. Note: only built-in presets can be reset.

To assign a heatmap preset to specific widget, select corresponding `heatmap name` in widget config dialog.

In case of errors found in `heatmap.json` preset, the APP will automatically fall back to built-in default heatmap preset.

To restore all heatmap settings back to default, just delete `heatmap.json` preset.

[**`Back to Top`**](#)


## Track map viewer
**Track map viewer can be accessed from `Tools` menu in main window.**

To load a track map, click `Load Map` button. Map file name will be displayed alongside if file is successfully loaded. Note, only track map files (.svg extension) that generated from TinyPedal [Mapping Module](#mapping-module) are supported.

To customize map display, click `Config` button. Note, some display options may require reload track map file to be updated.

To zoom map in or out, scroll mouse wheel in map display area; or adjust `Zoom` spin box value.

To move current position on map, use position slider at bottom of map display; or adjust `Position` spin box value.

To increase or decrease current nodes selection, adjust `Nodes` spin box value. Note, minimum nodes selection is limited to `3` nodes, maximum nodes selection cannot exceed total map nodes.

To toggle on or off specific map display, `Right-Click` on map display area to open context menu, includes:
* Map info - Show map length, total map nodes.
* Position info - Show current node position and global XYZ coordinates (Z is elevation).
* Curve info - Show curve section length, grade, radius, angle, curvature.
* Slope info - Show slope grade, percent, angle, height delta.
* Center mark - Mark current node position.
* Distance circle - Show reference distance circles.
* Osculating circle - Show osculating circle that calculated from curve section.
* Curve section - Show curve section from current nodes selection.
* Marked coordinates - Show marked coordinates if available.
* Highlighted coordinates - Show highlighted coordinates if available.
* Dark background - Show dark background color.

---

    inner_margin
Set inner margin for info display.

    position_increment_step
Set single increment step for position slider and spin box. Default is `5` meters.

    curve_grade_*
Set corner curve classification by radius (meters). Set value to `-1` to exclude from grade selection.

    length_grade_*
Set corner length classification by meters.

    slope_grade_*
Set road slope classification by slope percent.

[**`Back to Top`**](#)


## Track notes editor
**Track notes editor allows for creating and editing track or pace notes, which can be accessed from `Tools` menu in main window.**

Note, by default the editor starts in `Pace Notes` edit mode as displayed in status bar.

**Important note, the editor does not provide `undo` function, it is recommended to save file before doing heavy modification.**

The editor consists of two panel views:  
* Left panel is the `Track Map Viewer`, which can be used to visualize track map and providing analytic info for assisting notes creation. See [Track Map Viewer](#track-map-viewer) section for details.
* Right panel is the track and pace notes editor, which allows to create, open, and save track or pace notes file.

The table view consists of multiple columns: 
* `distance` column defines track position (in meters) of a note line.
* `pace note` column (in Pace Notes edit mode) defines `pace note` name that is used to match pace note sound file name. Because windows system excludes some special characters from used in file name, the `pace note` column will automatically strip off invalid characters. Note, DO NOT write file extension (format) in `pace note` column. File extension should be set in `Pace Notes` control panel tab from main window.
* `track note` column (in Track Notes edit mode) defines track `corner name` or `section name` or any thing user wish to note.
* `comment` column defines optional extra info for `pace note` or `track note` column for user. Note, a comment can be broken into multiple lines by adding `\n` to any part of the comment.

To create or open pace notes, click `File` and select `New Pace Notes` or `Open Pace Notes`.

To create or open track notes, click `File` and select `New Track Notes` or `Open Track Notes`.

To save notes file, click `Save`. Note, notes file name should exactly match with track name from track map file name for `auto notes loading` function to work. The editor will try to retrieve track name automatically in an active session, or from an opened track map in `Track Map Viewer`.

To save notes file to other formats for used in other games, select a file format name from `save type` in save dialog, such as `GPL Pace Notes (*.ini)` which saves pace notes in GPL pace notes file format. Note, only `TinyPedal` notes file formats are supported for used in TinyPedal.

To hide map viewer, click `Hide Map`. To show map viewer, click `Show Map`.

To edit metadata info, click `Info`. Metadata info provides optional info to notes:  
* `Title` of notes.
* `Author` of notes.
* `Date` when notes created or modified.
* `Description` about notes.

To set `distance` (position) value, first select one cell from `distance` column, then click `Set Pos` and click either `From Map` or `From Telemetry`. Note, `From Map` retrieves `distance` data from track map that opened in `Track Map Viewer`; `From Telemetry` retrieves `distance` data from current on-track vehicle position.

To add a note line, click `Add`, which adds a new note line at the end of notes table.

To insert a note line, first select a note line from notes table, then click `Insert` to insert a new note line `above` selected note line. To insert below selected note line, right-click on selected note line and click `Insert Row Below` from context menu.

To sort notes table, click `Sort`.

To delete notes, first select one or multiple note lines from notes table, then click `Delete`.

To replace words, click `Replace` and select a column, then use `Find` and `Replace` to find and replace words.

To batch offset `distance` (position) values, first select one or multiple note lines from `distance` column, then click `Offset` button. Click `Scale Mode` check box to scale distance values. Note, offset option will be reset to `0` each time after applying. Last applied offset value is displayed on top of dialog.

To highlight a `distance` value on `Track Map Viewer`, right-click on a note line and click `Highlight on Map`.

[**`Back to Top`**](#)


# Modules
Modules provide important data that updated in real-time for other widgets. Widgets may stop updating or receiving readings if corresponding modules were turned off. Each module can be configured by accessing `Config` button from `Module` tab in main window.

[**`Back to Top`**](#)


## Delta module
**This module provides deltabest and timing data.**

    module_delta
Enable delta module.

    minimum_delta_distance
Set minimum recording distance (in meters) between each delta sample. Default value is `5` meters. Lower value may result more samples recorded and bigger file size; higher value may result less samples recorded and inaccuracy. Recommended value range in `5` to `10` meters.

    delta_smoothing_samples
Set number of samples for delta data smoothing calculation using exponential moving average (EMA) method. Value range in `1` to `100`. Higher value results more smoothness, but may lose accuracy. Default is `30` samples. Set to `1` to disable smoothing.

    laptime_pace_samples
Set number of samples for average laptime pace calculation (EMA). Value range in `1` to `20`. Default is `6` samples. Set `1` to disable averaging. Note, initial laptime pace is always based on player's all time personal best laptime if available. If a new laptime is faster than current laptime pace, it will replace current laptime pace without calculating average. Invalid lap, pit-in/out laps are always excluded from laptime pace calculation.

    laptime_pace_margin
Set additional margin for laptime pace that cannot exceed the sum of previous `laptime pace` and `margin`. This option is used to minimize the impact of unusually slow laptime. Default value is `5` seconds. Minimum value is limited to `0.1`.

[**`Back to Top`**](#)


## Energy module
**This module provides vehicle virtual energy usage data.**

    module_energy
Enable energy module.

    minimum_delta_distance
Set minimum recording distance (in meters) between each delta sample. Default value is `5` meters. Lower value may result more samples recorded and bigger file size; higher value may result less samples recorded and inaccuracy. Recommended value range in `5` to `10` meters.

[**`Back to Top`**](#)


## Force module
**This module provides vehicle g force, downforce, braking rate data.**

    module_force
Enable force module.

    gravitational_acceleration
Set gravitational acceleration value on earth.

    max_g_force_reset_delay
Set time delay in seconds for resetting max g force reading.

    max_average_g_force_samples
Set amount samples for calculating max average g force. Minimum value is limited to `3`.

    max_average_g_force_difference
Set max average g force difference threshold which compares with the standard deviation calculated from max average g force samples. Default is `0.2` g.

    max_average_g_force_reset_delay
Set time delay in seconds for resetting max average g force. Default is `30` seconds.

    max_braking_rate_reset_delay
Set time delay in seconds for resetting max braking rate. Default is `60` seconds.

[**`Back to Top`**](#)


## Fuel module
**This module provides vehicle fuel usage data.**

    module_fuel
Enable fuel module.

    minimum_delta_distance
Set minimum recording distance (in meters) between each delta sample. Default value is `5` meters. Lower value may result more samples recorded and bigger file size; higher value may result less samples recorded and inaccuracy. Recommended value range in `5` to `10` meters.

[**`Back to Top`**](#)


## Hybrid module
**This module provides vehicle battery usage and electric motor data.**

    module_hybrid
Enable hybrid module.

    minimum_delta_distance
Set minimum recording distance (in meters) between each delta sample. Default value is `5` meters. Lower value may result more samples recorded and bigger file size; higher value may result less samples recorded and inaccuracy. Recommended value range in `5` to `10` meters.

[**`Back to Top`**](#)


## Mapping module
**This module records and processes track map data.**

    module_mapping
Enable mapping module.

[**`Back to Top`**](#)


## Notes module
**This module processes track and pace notes data.**

    module_notes
Enable notes module.

[**`Back to Top`**](#)


## Relative module
**This module provides vehicle relative and standings data.**

    module_relative
Enable relative module.

[**`Back to Top`**](#)


## RestAPI module
**This module connects to game's Rest API for accessing additional data that is not available through Sharedmemory API.**

    module_restapi
Enable RestAPI module.

    url_host*
Set `RF2` or `LMU` Rest API host address. Default is `localhost`.

    url_port*
Set port for host address. Port value must match `WebUI port` value that sets in `LMU` (UserData\player\Settings.JSON) or `RF2` (UserData\player\player.JSON) setting file in order to successfully connect to Rest API and receive data. The default port value for `RF2` is `5397`, and `6397` for `LMU`.

Note, `WebUI port` value from game setting file may change in some situations, and would require manual correction to match `WebUI port` value.

    connection_timeout
Set connection timeout duration in seconds. Value range in `0.5` to `10`. Default is `1` second.

    connection_retry
Set number of attempts to retry connection. Value range in `0` to `10`. Default is `3` retries.

    connection_retry_delay
Set time delay in seconds to retry connection. Value range in `0` to `60`. Default is `1` second.

    enable_pit_strategy_access
Set `false` to turn off "pit strategy" data accessing completely. Note, [Pit stop estimate](#pit-stop-estimate) Widget will not be able to display pit data if this option is turned off.

[**`Back to Top`**](#)


## Sectors module
**This module provides sectors timing data.**

    module_sectors
Enable sectors module.

    enable_all_time_best_sectors
Calculate sectors timing based on all time best sectors and affects [Sectors](#sectors) widget display. This option is enabled by default. Set `false` to calculate sectors timing from current session only. Note, both session best and all time best sectors data are saved no matter the setting.

[**`Back to Top`**](#)


## Stats module
**This module records driver stats data.**

Note, while `enable_player_index_override` or `enable_active_state_override` option is enabled in [Shared Memory API](#shared-memory-api), driver stats will not be recorded. Stats are only saved when driver returned to garage.

    module_stats
Enable stats module.

    vehicle_classification
Set one of the three vehicle classifications where stats will be saved.

`Class - Brand` saves corresponding stats under class and brand name. Make sure to use [Vehicle Brand Editor](#vehicle-brand-editor) to import brand name. If brand name does not exist, only class name will be used instead.

`Class` saves corresponding stats under class name only.

`Vehicle` saves corresponding stats under vehicle name only. Saving stats under vehicle name is not recommended, because each single vehicle in `RF2` or `LMU` uses unique vehicle name, which will result multiple records of the same vehicle.

    enable_podium_by_class
Enable to count race finish position by class instead of overall position.

[**`Back to Top`**](#)


## Vehicles module
**This module provides additional processed vehicles data.**

    module_vehicles
Enable vehicles module.

    lap_difference_ahead_threshold
Lap difference (percentage) threshold for tagging opponents as ahead. Default is `0.9` lap.

    lap_difference_behind_threshold
Lap difference (percentage) threshold for tagging opponents as behind. Default is `0.9` lap.

[**`Back to Top`**](#)


## Wheels module
**This module provides wheel radius and slip ratio data.**

    minimum_axle_rotation
Set minimum axle rotation (radians per second) for calculating wheel radius and differential locking percent. Default value is `4`.

    maximum_rotation_difference_front, maximum_rotation_difference_rear
Set maximum rotation difference between left or right wheel rotation and same axle rotation for limiting wheel radius calculation. Default value is `0.002` (0.2%). Setting higher difference value may result inaccurate wheel radius reading.

    cornering_radius_sampling_interval
Set position sampling interval for cornering radius calculation. Value range in `5` to `100`. Default sampling interval is `10`, which is roughly 200ms interval between each recorded position. Higher value may result inaccuracy. Note, this option does not affect position recording interval.

[**`Back to Top`**](#)


# Widgets
Each widget can be configured by accessing `Config` button from `Widget` tab in main window.

[**`Back to Top`**](#)


## Battery
**This widget displays battery usage info.**

Note, there are some electric vehicles in `RF2` that are not based on the new electric motor and battery charge system, which there is no battery usage info available.

    show_battery_charge
Show percentage available battery charge.

    show_battery_drain
Show percentage battery charge drained in current lap.

    show_battery_regen
Show percentage battery charge regenerated in current lap.

    show_estimated_net_change
Show estimated battery charge net change from current lap. Positive value indicates net gain (regen higher than drain); negative indicates net loss (drain higher than regen).

Total net change reading is more accurate for vehicles that constantly consume battery charge, such as `FE` or `Hypercar` class. It is less useful for vehicles that only utilize electric motor for a short duration, such as `P2P`.

Note, at least one full lap (excludes pit-out or first lap) is required to generate estimated net change data.

    show_activation_timer
Show electric boost motor activation timer.

    low_battery_threshold
Set percentage threshold for low battery charge warning indicator.

    freeze_duration
Set freeze duration (seconds) for displaying previous lap total drained/regenerated battery charge after crossing finish line. Value range in `0` to `30` seconds. Default is `10` seconds.

[**`Back to Top`**](#)


## Brake bias
**This widget displays brake bias info.**

    show_front_and_rear
Show both front and rear bias. Default is `false`.

    show_percentage_sign
Set `true` to show percentage sign for brake bias value.

    show_baseline_bias_delta
Show delta between current and baseline brake bias, which can be useful for keeping track of brake bias changes easier during a long race. Baseline brake bias is automatically set (and reset) while vehicle is stationary in pit lane.

    show_brake_migration
Show real-time brake migration change, as commonly seen in LMH and LMDh classes.

Note, brake migration is calculated based on brake input and brake pressure telemetry data, and is affected by pedal force setting from car setup and electric braking allocation of specific vehicle.

To get accurate brake migration reading, it is necessary for brake pedal to reach fully pressed state for at least once while entering track to recalibrate brake pressure scaling for brake migration calculation. It is normally not required to do manually, as game's auto-hold brake assist is on by default. However if auto-hold brake assist is off, or the APP was reloaded while player was already on track, then it is required to do a full braking for at least once to get accurate brake migration reading.

    electric_braking_allocation
Set allocation for calculating brake migration under different electric braking allocation from specific vehicle. Note, vehicle that has not electric braking, or has disabled regeneration, is not affected by this option. Incorrect allocation value will result wrong brake migration reading from vehicle that has electric braking activated.

Set value to `-1` to enable auto-detection, which automatically checks whether electric braking is activated on either axles while braking, and sets allocation accordingly. This is enabled by default. Note, it may take a few brakes to detect correct allocation.

Set value to `0` to manual override and use front allocation, which is commonly seen in LMH class.

Set value to `1` to manual override and use rear allocation, which is commonly seen in LMDh class.

[**`Back to Top`**](#)


## Brake performance
**This widget displays brake performance info.**

    show_transient_max_braking_rate
Show transient max braking rate (g) from last braking input, and resets after 3 seconds.

    show_max_braking_rate
Show max braking rate (g), and resets after a set period of time that defined by `max_braking_rate_reset_delay` value in Force Module.

    show_delta_braking_rate
Show max braking rate difference (g) against transient max braking rate, and resets on the next braking.

    show_delta_braking_rate_in_percentage
Show max braking rate difference (g) in percentage (%) instead.

    show_front_wheel_lock_duration, show_rear_wheel_lock_duration
Show front and rear wheel lock duration (seconds) per lap under braking. Duration increases when tyre slip ratio has exceeded `wheel_lock_threshold` value, and resets on first braking input of a new lap.

    wheel_lock_threshold
Set percentage threshold for counting wheel lock duration under braking. `0.3` means 30% of tyre slip ratio.

[**`Back to Top`**](#)


## Brake pressure
**This widget displays visualized percentage brake pressure info.**

[**`Back to Top`**](#)


## Brake temperature
**This widget displays brake temperature info.**

Note, if temperature drops below `-100` degrees Celsius, temperature readings will be replaced by unavailable sign as `-`. This usually indicates brake failure, or brake is not available on one of the wheels.

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    enable_heatmap_auto_matching
Enable automatically heatmap style matching for specific brakes defined in `brakes.json` preset. This option applies matching heatmap style to front and rear brakes separately.

    heatmap_name
Set heatmap preset name that is defined in `heatmap.json` preset. Note, this option has no effect while `enable_heatmap_auto_matching` is enabled.

    swap_style
Swap heatmap color between font and background color.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_average
Show average brake temperature calculated from a full lap.

    highlight_duration
Set duration (seconds) for highlighting average brake temperature from previous lap after crossing finish line. Default is `5` seconds.

[**`Back to Top`**](#)


## Brake wear
**This widget displays brake wear info.**

Important note: Brake wear data is currently only available on `LMU`. `RF2` currently doesn't provide brake wear data. Depends on vehicle, brake may or may not have noticeable wear.

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_thickness
Show brake thickness (millimeter) instead of percentage, which also affects wear difference readings.

Note, brake maximum thickness (for percentage wear calculation) is retrieved at the moment when car leaves garage or has brake repaired or changed. Reloading a preset or restarting APP in the middle of a running stint could result wrong maximum thickness and percentage wear calculation, which should be avoided.

**Notes to brake failure thickness:**

Brake failure thickness is millimeter thickness threshold at brake failure, which affects brake wear calculation accuracy, and can be customized for specific vehicle class in [Brake Editor](#brake-editor).

For example, if `brake thickness` is `40`mm, and `failure thickness` is `25`mm, then `effective thickness` is `40 - 25 = 15mm`.

Since brake failure thickness threshold data is not available from game API, it may require testing to find out, and may vary from vehicle to vehicle. Front brake failure thickness threshold can be different from rear brake. Thickness threshold value should not exceed brake maximum thickness, otherwise brake wear readings will not be displayed correctly.

Some reference brake failure thickness threshold:
`Hypercar` and `P2` classes in `LMU` usually have `25`mm brake failure threshold.
`GTE` and `LMGT3` class in `LMU` usually has `30`mm brake failure threshold.

    show_remaining
Show total remaining brake in percentage that changes color according to wear.

    show_wear_difference
Show total brake wear difference of previous lap.

    show_live_wear_difference
Show brake wear difference of current lap that constantly updated.

    freeze_duration
Set freeze duration (seconds) for displaying previous lap brake wear if `show_live_wear_difference` is enabled. Value range in `0` to `30` seconds. Default is `10` seconds.

    show_lifespan_laps
Show estimated brake lifespan in laps.

    show_lifespan_minutes
Show estimated brake lifespan in minutes.

    warning_threshold_remaining
Set warning threshold for total remaining brake in percentage. Default is `30` percent.

    warning_threshold_wear
Set warning threshold for total amount brake wear of last lap in percentage. Default is `1` percent.

    warning_threshold_laps
Set warning threshold for estimated brake lifespan in laps. Default is `5` laps.

    warning_threshold_minutes
Set warning threshold for estimated brake lifespan in minutes. Default is `5` laps.

[**`Back to Top`**](#)


## Cruise
**This widget displays track clock, compass, elevation, odometer info.**

    show_track_clock
Show current in-game clock time of the circuit.

    enable_track_clock_synchronization
Enable auto track clock and time scale synchronization. RestAPI module must be enabled to synchronize track clock from Rest API.

Note, for `RF2`, synchronization only works in singleplayer; for `LMU`, synchronization works in both singleplayer and multiplayer.

    track_clock_time_scale
Manually set time multiplier for time-scaled session. Default is `1`, which matches `Time Scale: Normal` setting in-game. Note, this option will only be used if `enable_track_clock_synchronization` option is disabled.

    track_clock_format
Set track clock format string. To show seconds, add `%S`, such as `%H:%M:%S %p`. See [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for full list of format codes.

    show_time_scale
Show current session track clock time scale multiplier.

    show_compass
Show compass directions with three-figure bearings that matches game's cardinal directions.

    show_elevation
Show elevation difference in game's coordinate system.

    show_odometer
Show odometer that displays total driven distance of local player. 

    odometer_maximum_digits
Set maximum number of display digits.

    show_distance_into_lap
Show distance into current lap.

    show_cornering_radius
Show cornering radius calculated in real-time.

[**`Back to Top`**](#)


## Damage
**This widget displays visualized vehicle damage info.**

**Wheel (suspension) damage levels**

1. No damage to suspension or wheel (default color: green).
2. Light suspension damage (default damage range: 2% - 15%, default color: yellow).
3. Medium suspension damage (default damage range: 15% - 40%, default color: orange).
4. Heavy suspension damage (default damage range: 40% - 80%, default color: purple).
5. Totaled suspension (default damage range: 80% - 100%, default color: blue).
6. Wheel detached (default color: black).

Note, body aero integrity and suspension damage display is only available for `LMU`.

    display_margin
Set display margin in pixels.

    inner_gap
Set body parts inner gap in pixels.

    part_width
Set body parts width in pixels. Minimum value is limited to `1`.

    parts_max_width, parts_max_height
Set maximum body parts width, height in pixels. Minimum value is limited to `4`.

    wheel_width, wheel_height
Set wheel width, height in pixels. Minimum value is limited to `1`.

    show_background
Show widget background.

    suspension_damage_*_threshold
Set suspension damage level percentage threshold for suspension damage color indication, which better reflects severity of suspension damage that would affect handling.

    show_last_impact_cone
Show cone indicator towards last known impact (collision) position.

    last_impact_cone_angle
Set cone angle (size) in degree. Value range in `2` to `90`. Default is `15`.

    last_impact_cone_duration
Set cone indicator display duration (seconds) for last known impact. Default is `15` seconds.

    show_integrity_reading
Show vehicle bodywork integrity reading in percentage. Note, bodywork damage may not necessarily affect aero or handling.

    show_aero_integrity_if_available
Show vehicle body aero integrity reading in percentage if available, which better reflects severity of bodywork damage that would affect performance.

    show_inverted_integrity
Invert integrity reading.

[**`Back to Top`**](#)


## Deltabest
**This widget displays deltabest info.**

    layout
2 layouts are available: `0` = delta bar above deltabest text, `1` = delta bar below deltabest text.

    swap_style
Swap time gain and loss color between font and background color.

    deltabest_source
Set lap time source for deltabest display. Available values are: `Best` = all time best lap time, `Session` = session best lap time, `Stint` = stint best lap time, `Last` = last lap time.

    show_delta_bar
Show visualized delta bar.

    bar_length, bar_height
Set delta bar length and height in pixels.

    bar_display_range
Set max display range (gain or loss) in seconds for delta bar, accepts decimal place. Default is `2` seconds.

    delta_display_range
Set max display range (gain or loss) in seconds for delta reading, accepts decimal place. Default is `99.999` seconds.

    freeze_duration
Set freeze duration (seconds) for displaying previous lap time difference against best lap time source after crossing finish line. Value range in `0` to `30` seconds. Default is `3` seconds. Set to `0` to disable.

    show_animated_deltabest
Deltabest display follows delta bar progress.

[**`Back to Top`**](#)


## Deltabest extended
**This widget displays deltabest info against multiple lap time sources.**

    show_all_time_deltabest
Show deltabest against personal all time best lap time.

    show_session_deltabest
Show deltabest against current personal session best lap time. Note: session deltabest will be reset upon changing session, or reload preset/restart APP.

    show_stint_deltabest
Show deltabest against current personal stint best lap time. Note: stint deltabest will be reset if vehicle stops in pit lane.

    show_deltalast
Show delta against personal last lap time (deltalast). Note: deltalast will be reset upon ESC.

[**`Back to Top`**](#)


## Differential
**This widget displays wheel differential locking info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_inverted_locking
Invert minimum differential locking percent reading.

    show_power_locking_*, show_coast_locking_*
Show minimum differential locking percent between left and right wheels on the same axle under power (on throttle) or coasting (off throttle).

A `100%` reading indicates two wheels on the same axle are rotating at same speed; while `0%` indicates that one of the wheels is completely spinning or locked.

    off_throttle_threshold
Set percentage threshold which counts as off throttle if throttle position is lower, value range in `0.0` to `1.0`. Default is `0.01` (1%).

    on_throttle_threshold
Set percentage threshold which counts as on throttle if throttle position is higher, value range in `0.0` to `1.0`. Default is `0.01` (1%).

    power_locking_reset_cooldown, coast_locking_reset_cooldown
Set cooldown duration (seconds) before resetting minimum power or coast locking percent value if value hasn't changed during cooldown period. Default is `5` seconds.

[**`Back to Top`**](#)


## DRS
**This widget displays DRS(rear flap) usage info.**

    drs_text
Set custom DRS text.

    font_color_activated, bkg_color_activated
Set color when DRS is activated by player.

    font_color_allowed, bkg_color_allowed
Set color when DRS is allowed but not yet activated by player.

    font_color_available, bkg_color_available
Set color when DRS is available but current disallowed to use.

    font_color_not_available, bkg_color_not_available
Set color when DRS is unavailable for current track or car.

[**`Back to Top`**](#)


## Electric motor
**This widget displays electric motor usage info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_motor_temperature
Show electric motor temperature.

    show_water_temperature
Show electric motor cooler water temperature.

    overheat_threshold_motor, overheat_threshold_water
Set temperature threshold for electric motor and water overheat color indicator, unit in Celsius.

    show_rpm
Show electric motor RPM.

    show_torque
Show electric motor torque.

    show_power
Show electric motor power.

[**`Back to Top`**](#)


## Elevation
**This widget displays elevation plot. Note: elevation plot data is recorded together with track map. At least one complete and valid lap is required to generate elevation plot.**

    display_detail_level
Sets detail level for track map. Default value is `1`, which auto adjusts map detail according to display size. Higher value reduces map detail and RAM usage, and may also help reduce rough edges from large map. Set to `0` for full detail.

    display_width
Set widget display width in pixels. Minimum width is limited to `20`.

    display_height
Set widget display height in pixels. Minimum height is limited to `10`.

    display_margin_*
Set widget display margin in pixels. Maximum margin is limited to half of `display_height` value.

    show_elevation_reading
Show elevation difference in game's coordinate system.

    show_elevation_scale
Show elevation plot scale reading, which is ratio between screen pixel and real world elevation. A `1:10.5` reading means 1 pixel equals 10.5 meters (or feet, depends on distance unit setting).

    show_background
Show widget background.

    show_elevation_background
Show background of elevation plot.

    show_elevation_progress
Show elevation progress bar according player's current position.

    show_elevation_progress_line
Show elevation progress line according player's current position.

    show_elevation_line
Show elevation reference line.

    show_zero_elevation_line
Show zero elevation reference line in game's coordinate system.

    show_start_line
Show start line mark.

    show_sector_line
Show sector line mark.

    show_position_mark
Show player's current position line mark.

[**`Back to Top`**](#)


## Engine
**This widget displays engine usage info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_temperature
Show oil and water temperature.

    overheat_threshold_oil, overheat_threshold_water
Set temperature threshold for oil and water overheat color indicator, unit in Celsius.

    show_turbo_pressure
Show turbo pressure.

    show_rpm
Show engine RPM.

    show_rpm_maximum
Show maximum engine RPM (rev limit).

    show_torque
Show engine torque.

    show_power
Show engine power.

[**`Back to Top`**](#)


## Flag
**This widget displays flags, pit state, warnings, start lights info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_pit_timer
Show pit timer, and total amount time spent in pit after exit pit.

    pit_time_highlight_duration
Set highlight duration for total amount time spent in pit after exit pit.

    pit_closed_text
Set custom pit closed text.

    font_color_pit_closed, bkg_color_pit_closed
Set color indicator on pit timer when pit lane is closed.

    show_low_fuel
Show low fuel (or low virtual energy if available) indicator when below certain amount value. Only one indicator will be displayed for low fuel (LF) or low virtual energy (LE), depends on which one would deplete sooner.

    show_low_fuel_for_race_only
Only show low fuel indicator during race session.

    low_fuel_volume_threshold
Set fuel volume threshold (in Liter) to show low fuel indicator when total amount of remaining fuel is equal or less than this value. This setting is used to limit low fuel warning when racing on lengthy tracks, where fuel tank may only hold for a lap or two. Default is `20` Liter.

    low_fuel_lap_threshold
Set amount lap threshold to show low fuel indicator when total completable laps of remaining fuel is equal or less than this value. Default is `2` laps before running out of fuel.

    show_speed_limiter
Show speed limiter indicator.

    speed_limiter_text
Set custom pit speed limiter text which shows when speed limiter is engaged.

    show_yellow_flag
Show yellow flag indicator and distance display which shows nearest yellow flag vehicle distance.

    show_yellow_flag_for_race_only
Only show yellow flag indicator during race session.

    yellow_flag_maximum_range
Only show yellow flag indicator when there is yellow flag within the maximum range (track distance in meters).

    show_blue_flag
Show blue flag indicator with timer.

    show_blue_flag_for_race_only
Only show blue flag indicator during race session.

    show_startlights
Show race start lights indicator with light frame number for standing-type start.

    green_flag_duration
Set display duration(seconds) for green flag text before it disappears. Default is `3`.

    red_lights_text
Set custom text for red lights.

    green_flag_text
Set custom text for green flag.

    show_traffic
Show nearest incoming on-track traffic indicator (time gap) while in pit lane or after pit-out.

    traffic_maximum_time_gap
Set maximum time gap (seconds) of incoming on-track traffic.

    traffic_pitout_duration
Set traffic indicator extended duration (seconds) after pit-out.

    traffic_low_speed_threshold
Set low speed threshold for showing nearest incoming traffic indicator. Default is `8` m/s (roughly 28kph). Set to `0` to disable. This option can be useful to quickly determine nearby traffic situation after a spin or crash.

    show_pit_request
Show pit request indicator and `pit-in laps countdown` alongside `estimated remaining laps` reading that current fuel or energy can run. Note, `pit-in laps countdown` value is always calculated towards the finish line of current stint's final lap, and thus is always less than or equal to `estimated remaining laps` reading. If countdown drops below 1.0 (laps), it indicates the final lap of current stint, and driver should pit in before the end of current lap to refuel. If countdown reaches zero or negative, there may still be some fuel or energy left in tank, however it will not be enough to complete another full lap.

    show_finish_state
Show finish or disqualify state.

[**`Back to Top`**](#)


## Force
**This widget displays g force and downforce info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_g_force
Show longitudinal and lateral g force with direction indicator.

    show_downforce_ratio
Show front vs rear downforce ratio. 50% means equal downforce; higher than 50% means front has more downforce.

    show_front_downforce, show_rear_downforce
Show front and rear downforce reading in Newtons.

    warning_color_liftforce
Set lift force indicator color.

[**`Back to Top`**](#)


## Friction circle
**This widget displays g force in circle diagram.**

    display_size
Set widget size in pixels.

    display_radius_g
Set viewable g force range by radius(g).

    show_inverted_orientation
Set `true` to invert display orientation for longitudinal and lateral g force axis. Default is `false`, which shows brake at top, acceleration at bottom, right-turn at left, left-turn at right.

    show_readings
Show values from g force reading. Value at top is current longitudinal g force, and value at bottom is max longitudinal g force. Value at left is max lateral g force, and value at right is current lateral g force.

    show_background
Show background color that covers entire widget.

    show_circle_background
Show circle background color.

    show_fade_out
Fade out circle background edge.

    fade_in_radius, fade_out_radius
Set fade in/out radius, value range in `0.0` to `1.0`.

    show_max_average_lateral_g_circle
Show max average lateral g force reference circle.

    max_average_lateral_g_circle_style
Set circle line style. `0` for dashed line, `1` for solid line.

    max_average_lateral_g_circle_width
Set circle line width in pixels.

    show_dot
Show g force dot.

    dot_size
Set g force dot size in pixels.

    show_trace
Show g force trace.

    trace_max_samples
Set max amount g force trace samples.

    trace_style
Set g force trace style. `0` for line style. `1` for point style.

    trace_width
Set g force trace width in pixels.

    show_trace_fade_out
Show trace fade out effect.

    trace_fade_out_step
Set trace fade out speed. Value range in `0.1` to `0.9`, higher value increases trace fade out speed. Default value is `0.2`.

    show_center_mark
Show center mark.

    center_mark_radius_g
Set center mark size by radius(g).

    center_mark_style
Set center mark line style. `0` for dashed line, `1` for solid line.

    center_mark_width
Set center mark line width in pixels.

    show_reference_circle
Show reference circle.

    reference_circle_*_radius_g
Set reference circle size by radius(g). Circle will not be displayed if radius is bigger than `display_radius_g`.

    reference_circle_*_style
Set reference circle line style. `0` for dashed line, `1` for solid line.

    reference_circle_*_width
Set reference circle line width in pixels.

[**`Back to Top`**](#)


## Fuel
**This widget displays fuel usage info.**

Note, for non-hybrid pure electric vehicle, this widget will show `battery charge` usage (in percentage) info instead. Since multiple different electric systems exist in `RF2`, there is no reliable way to distinguish pure electric vehicles from fuel or hybrid vehicles, it is important to make sure `fuel_unit` option in [Units](#units) setting is set to `Liter` in order to correctly display battery charge usage in `percentage` for pure electric vehicles.

---

Differences between `relative` and `absolute` refueling:

* Relative refueling value shows total amount `additional` fuel required to finish the remaining race length, which matches `relative refueling` mechanism (amount to add on top of remaining fuel in tank) in `RF2`.

* Absolute refueling value shows absolute total amount fuel required to finish the remaining race length, which matches `absolute refueling` mechanism (amount total fuel to fill tank up to) in `LMU`.

Also see `estimated laps` display option in [Session](#session) widget that can be used for `absolute refueling`.

---

    show_absolute_refueling
Show absolute refueling value instead of relative refueling when enabled. Note, `+` or `-` sign is not displayed with absolute refueling.

    *remain
Remaining fuel in tank.

    *refuel
Estimated refueling reading, which is the total amount additional fuel required to finish race.

Note, for `relative refueling` (`show_absolute_refueling` disabled), positive value indicates additional refueling and pit-stop would be required, while negative value indicates total remaining fuel at the end of race, and no extra pit-stop required. For example, a `-1.5` value indicates `1.5` remaining fuel after crossed finish line.

For `absolute refueling` (`show_absolute_refueling` enabled), total remaining fuel at the end of race can be found by subtracting `refuel` value from `remain` value. For example, `6` (remain column) - `4.5` (refuel column) = `1.5` remaining fuel after crossed finish line.

    *used
Estimated fuel consumption reading, which is calculated from last-valid-lap fuel consumption and delta fuel consumption. Note, when vehicle is in garage stall, this reading only shows last-valid-lap fuel consumption without delta calculation.

    *delta
Estimated delta fuel consumption reading. Positive value indicates an increase in consumption, while negative indicates a decrease in consumption.

    *pits
Estimate number of pit stop counts when making a pit stop at end of current stint. Any non-zero decimal places would be considered for an additional pit stop.

    *early
Estimate number of pit stop counts when making an early pit stop at end of current lap. This value can be used to determine whether an early pit stop is worth performing comparing to `pits` value.

Example 1: When this value is just below `1.0` (such as `0.97`), it indicates an early pit stop can be made right at the end of current lap with enough empty capacity to refuel according to `refuel` reading which would last to the end of race.

Example 2: When this value is just below `2.0` (such as `1.96`), and `pits` value is also in `1.x` range (such as `1.32`),  it indicates 2 required pit stops, and an early pit stop can be made right at the end of current lap with tank fully refueled according to `refuel` reading. After refueling, `pits` reading would show an approximately `0.96` value which indicates one more required pit stop.

Example 3: If this value is one or more integers higher than `pits` value, then additional pit stops would be required after making a pit stop at the end of current lap.

    *laps
Estimated laps reading that current fuel can last.

    *minutes
Estimated minutes reading that current fuel can last.

    *save
Estimated fuel consumption reading for one less pit stop.

    *end
Estimated remaining fuel reading at the end of current stint before next pit stop, which reflects fuel usage efficiency.

Note, this value does not count towards the end of race; instead, this value always counts towards the end of last completeable lap. To find out total remaining fuel at the end of race, see `refuel` column and explanation.

    bar_width
Set each column width, value in chars, such as 10 = 10 chars. Default is `5`. Minimum width is limited to `3`.

    low_fuel_lap_threshold
Set amount lap threshold to show low fuel indicator when total completable laps of remaining fuel is equal or less than this value. Default is `2` laps before running out of fuel.

    warning_color_low_fuel
Set low fuel color indicator, which changes widget background color when there is just 2 laps of fuel left.

    show_fuel_level_bar
Show visualized horizontal fuel level bar.

    fuel_level_bar_height
Set fuel level bar height in pixels.

    show_starting_fuel_level_mark
Show starting fuel level mark of current stint. Default mark color is red.

    show_refueling_level_mark
Show estimated fuel level mark after refueling. If the mark is not visible on fuel level bar, it indicates total refueling has exceeded fuel tank capacity. Default mark color is green.

    starting_fuel_level_mark_width, refueling_level_mark_width
Set fuel level mark width in pixels.

    caption_text
Set custom caption text.

    swap_upper_caption, swap_lower_caption
Swap caption row position.

[**`Back to Top`**](#)


## Fuel energy saver
**This widget displays fuel or virtual energy saving info.**

Show current stint estimated total completable laps and completed laps based on current consumption.

Show estimated target lap consumption to save (extend) one or more total stint laps.

Show delta consumption against target lap consumption, which allows fuel or energy saving to be visualized and easily controlled in real-time.

Show consumption type in `FUEL` or `NRG` (if virtual energy available).

Show last lap consumption.

    minimum_reserve
Set minimum amount fuel or virtual energy in tank that is excluded from saving calculation and reserved for the end of stint. Default is `0.2` Liter for fuel (or % for virtual energy).

    number_of_more_laps
Set number of target slots for more completable laps. Default is `3`. Range in `1` to `10`.

    number_of_less_laps
Set number of target slots for less completable laps. Default is `0`. Range in `0` to `5`.

[**`Back to Top`**](#)


## Gear
**This widget displays gear, RPM, speed, battery info.**

    inner_gap
Set inner gap between gear and speed readings. Negative value reduces gap, while positive value increases gap. Default is `0`.

    show_speed
Show speed reading.

    show_speed_below_gear
Show speed reading below gear.

    font_scale_speed
Set font scale for speed reading. This option only takes effect when `show_speed_below_gear` is enabled. Default is `0.5`.

    show_speed_limiter
Show pit speed limiter indicator.

    speed_limiter_text
Set custom pit speed limiter text which shows when speed limiter is engaged.

    show_battery_bar
Show battery bar, which is only visible if electric motor available.

    show_inverted_battery
Invert battery bar progression.

    battery_bar_height
Set battery bar height in pixels.

    show_battery_reading
Show battery charge (in percentage) reading text on battery bar.

    show_rpm_bar
Show a RPM bar at bottom of gear widget, which moves when RPM reaches range between safe and max RPM.

    show_inverted_rpm
Invert RPM bar progression.

    rpm_bar_height
RPM bar height, in pixel.

    show_rpm_reading
Show RPM reading text on RPM bar.

    rpm_multiplier_safe
This value multiplies max RPM value, which sets relative safe RPM range for RPM color indicator (changes gear widget background color upon reaching this RPM value).

    rpm_multiplier_redline
This value multiplies max RPM value, which sets relative near-max RPM range for RPM color indicator.

    rpm_multiplier_critical
This value multiplies max RPM value, which sets critical RPM range for RPM color indicator.

    show_rpm_flickering_above_critical
Show flickering effects when RPM is above critical range and gear is lower than max gear.

    neutral_warning_speed_threshold, neutral_warning_time_threshold
Set speed/time threshold value for neutral gear color warning, which activates color warning when speed and time-in-neutral is higher than threshold. Speed unit in meters per second, Default is `28`. Time unit in seconds, Default is `0.3` seconds.

[**`Back to Top`**](#)


## Heading
**This widget displays vehicle yaw angle, slip angle, heading info.**

    display_size
Set widget size in pixels.

    show_yaw_angle_reading
Show yaw angle reading in degree.

    show_slip_angle_reading
Show slip angle reading in degree.

    show_degree_sign
Set `true` to show degree sign for yaw angle reading.

    show_background
Show background color that covers entire widget.

    show_circle_background
Show circle background color.

    show_yaw_line
Show yaw line (vehicle heading).

    show_direction_line
Show vehicle's direction of travel line.

    show_slip_angle_line
Show slip angle (average of the front tyres) line.

    *_line_head_scale
Set line length scale from center to head, value range in `0.0` to `1.0`.

    *_line_tail_scale
Set line length scale from center to tail, value range in `0.0` to `1.0`.

    *_line_width
Set line width in pixels.

    show_dot
Show center dot.

    show_center_mark
Show center mark.

    center_mark_length_scale
Set center mark length scale, value range in `0.0` to `1.0`.

    center_mark_style
Set center mark line style. `0` for dashed line, `1` for solid line.

    center_mark_width
Set center mark line width in pixels.

[**`Back to Top`**](#)


## Instrument
**This widget displays vehicle instruments info.**

    icon_size
Set size of instrument icon in pixel. Minimum value is limited to `16`.

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_headlights
Show headlights state.

    show_ignition
Show engine ignition, starter, stalling state.

    stalling_rpm_threshold
Set RPM threshold for triggering engine stalling warning. Default is `100` RPM.

    show_clutch
Show auto-clutch and clutch state.

    show_wheel_lock
Show wheel lock state.

    show_wheel_slip
Show wheel slip state.

    wheel_lock_threshold
Set percentage threshold for triggering wheel lock warning under braking. `0.3` means 30% of tyre slip ratio.

    wheel_slip_threshold
Set percentage threshold for triggering wheel slip warning under acceleration. `0.1` means 10% of tyre slip ratio.

[**`Back to Top`**](#)


## Lap time history
**This widget displays lap time history info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = reversed vertical layout.

    lap_time_history_count
Set the number of lap time history display. Default is to show `10` most recent lap times.

    show_virtual_energy_if_available
Show virtual energy consumption instead of fuel consumption if available. This option is enabled by default.

    show_empty_history
Show empty lap time history. Default is `false`, which hides empty rows.

[**`Back to Top`**](#)


## Laps and position
**This widget displays lap number, driver overall position, position in class info.**

    show_lap_number
Show your current lap number (lap progression) and max laps if available.

    bkg_color_maxlap_warn
Set warning color that shows 1 lap before exceeding max-lap in qualify (or indicates the last lap of a lap-type race).

    show_position_overall
Show your current overall position against all drivers in a session.

    show_position_in_class
Show your current position in class against all drivers from the same class.

[**`Back to Top`**](#)


## Navigation
**This widget displays a zoomed navigation map that centered on player's vehicle. Note: at least one complete and valid lap is required to generate map.**

    display_size
Set widget size in pixels.

    view_radius
Set viewable area by radius(unit meter). Default is `500` meters. Minimum value is limited to `5`.

    show_background
Show background color that covers entire widget.

    show_circle_background
Show circle background color.

    circle_outline_width
Set circle background outline width. Set value to `0` to hide outline.

    show_fade_out
Fade out view edge.

    fade_in_radius, fade_out_radius
Set fade in/out radius, value range in `0.0` to `1.0`.

    map_width
Set navigation map line width.

    map_outline_width
Set navigation map outline width.

    show_start_line
Show start line mark.

    show_sector_line
Show sector line mark.

    show_vehicle_standings
Show vehicle standings info on navigation map.

    show_circle_vehicle_shape
Set `True` to show vehicle in circle shape, set `False` for arrow shape.

    vehicle_size
Set vehicle size in pixels.

    vehicle_offset
Set vehicle vertical position offset (percentage) relative to display size, value range in `0.0` to `1.0`.

    vehicle_outline_width
Set vehicle outline width.

[**`Back to Top`**](#)


## P2P
**This widget displays push to pass usage info.**

    show_battery_charge
Show percentage available battery charge.

    show_activation_timer
Show electric boost motor activation timer.

    activation_threshold_gear
Set minimum gear threshold for P2P ready indicator.

    activation_threshold_speed
Set minimum speed threshold for P2P ready indicator, unit in KPH.

    activation_threshold_throttle
Set minimum throttle input percentage threshold for P2P ready indicator, value range in `0.0` to `1.0`. Default is `0.6` (60%).

    minimum_activation_time_delay
Set minimum time delay between each P2P activation, unit in seconds.

    maximum_activation_time_per_lap
Set maximum P2P activation time per lap, unit in seconds.

[**`Back to Top`**](#)


## Pace notes
**This widget displays pace notes, comments, debugging info.**

    show_background
Show background color. Turn off to show text only.

    show_pace_notes
Show nearest pace notes info behind current vehicle position.

    show_comments
Show nearest pace notes comments info behind current vehicle position.

    enable_comments_line_break
Enable line break for displaying multi-line comments. To break a line into multiple lines, add `\n` to any part of the comment.

    show_debugging
Show nearest pace notes index number behind current vehicle position, and distance value (meters) behind current position to next index position.

    pace_notes_width, comments_width, debugging_width
Set maximum display width, value in chars, such as 10 = 10 chars.

    auto_hide_if_not_available
Auto hide this widget if pace notes data is not available for current track.

    maximum_display_duration
Set maximum display duration (seconds) of each note. Set to `-1` to always display notes. Default is `-1`.

[**`Back to Top`**](#)


## Pedal
**This widget displays pedal input and force feedback info.**

    show_readings
Show pedal input and force feedback readings. Note, while `show_*_filtered` option is enabled, only the highest reading between filtered and raw input is displayed.

    readings_offset
Set reading text offset position (percentage), value range in `0.0` to `1.0`.

    enable_horizontal_style
Show pedal bar in horizontal style.

    bar_length, bar_width_unfiltered, bar_width_filtered
Set pedal bar length and width in pixels.

    inner_gap
Set gap between pedal and max indicator.

    max_indicator_height
This is the indicator height when pedal reaches 100% travel, value in pixel.

    show_brake_pressure
Show brake pressure changes applied on all wheels, which auto scales with max brake pressure and indicates amount brake released by ABS on all wheels. This option is enabled by default, which replaces game's filtered brake input that cannot show ABS.

    show_throttle
Show throttle bar.

    show_brake
Show brake bar.

    show_clutch
Show clutch bar.

    show_ffb_meter
Show Force Feedback meter.

    show_*_filtered
Show filtered pedal input if available. Note, some vehicles may not provide filtered pedal input value, which the value will be zero. Disable this option to show raw input only.

[**`Back to Top`**](#)


## Pit stop estimate
**This widget displays estimated pit stop duration and refilling info.**

Note, this widget is designed for `LMU`. Most readings are not available for `RF2` due to lack of API data.

    pass_duration
Show estimated pit-lane pass through (drive-through) time, calculated from pit-entry to pit-exit line. Average accuracy is within `0.5` seconds. Note, for any new tracks, at least one pit-lane pass through is required to record data for pass through time calculation.

    stop_duration
Show estimated pit stop time while making a service stop or serving a penalty, calculated according to each setting from MFD `Pitstop` page and underlying service timing and concurrency differences. Average accuracy is within `1` seconds.

Note, for unscheduled pit stop (without requesting pit), game sometimes will add random amount extra delay (as part of pit crew preparation time) on top of pit stop time. To avoid this, always requests pit before entering pit.

    maximum_delay
Show maximum total random delay which game may add on top of pit stop time. For example, if estimated pit stop time is `12.0`s, and maximum delay is `+3.0`s, then final pit stop time will be between `12.0`s and `15.0`s.

    stop_go_penalty_time
Set stop go penalty time in seconds. Default value is `10` seconds.

    additional_pitstop_time
Set additional pit stop time that is not part of `pass_duration` or `stop_duration`. Default value is `2` seconds, which is the average time it takes to decelerate and accelerate towards and away from pit spot.

    minimum_total_duration
Show estimated minimum total pit time, which is the sum of `pass_duration`, `stop_duration`, and `additional_pitstop_time`. Note, this reading is recalculated only while not in pit lane.

    maximum_total_duration
Show estimated maximum total pit time, which is the sum of `minimum_total_duration` and `maximum_delay`. Note, this reading is recalculated only while not in pit lane.

    pit_timer
Show pit timer, useful for comparing against other pit time readings.

    actual_relative_refill
Show actual relative refilling, as the total additional fuel or virtual energy that will be added in next pit stop according to remaining fuel or virtual energy and user refill setting from MFD `Pitstop` page.

    total_relative_refill
Show total relative refilling, as the total additional fuel or virtual energy that is required to finish the race. This is the same value as seen from `refill` column of Fuel Widget or Virtual energy Widget.

With both `actual` and `total` relative refilling readings, users can determine precisely how much fuel or virtual energy that will be added in next pit stop, and whether the refilling will be enough or more pit stops are required.

[**`Back to Top`**](#)


## Radar
**This widget displays vehicle radar info.**

    global_scale
Sets global scale of radar display. Default is `6`, which is 6 times of original size.

    radar_radius
Set the radar display area by radius(unit meter). Default is `30` meters. Minimum value is limited to `5`.

    vehicle_length, vehicle_width
Set vehicle overall size (length and width), value in meters.

    vehicle_border_radius
Set vehicle round border radius.

    vehicle_outline_width
Set vehicle outline width.

    enable_radar_fade
Enable radar gradually fade in/out effect.

    radar_fade_out_radius
Set radar fade out radius relative to radar radius. Value range in `0.5` to `1.0`. Default value is `0.98`.

    radar_fade_in_radius
Set radar fade in radius relative to radar radius. Minimum value is limited to `0.1`, maximum value cannot exceed `radar_fade_out_radius`. Default value is `0.8`.

    show_background
Show background color that covers entire widget.

    show_circle_background
Show circle background color.

    show_edge_fade_out
Fade out radar edge.

    edge_fade_in_radius, edge_fade_out_radius
Set fade in/out radius relative to radar radius, value range in `0.0` to `1.0`.

    show_overlap_indicator
Show overlap indicator when there are nearby side by side vehicles. This option shows `boundary style` indicator if `show_overlap_indicator_in_cone_style` option is disabled.

    show_overlap_indicator_in_cone_style
Show overlap indicator in `cone style` instead of `boundary style`.

    overlap_cone_angle
Set cone display angle in degrees. This option does not affect overlap detection range. Default is `120` degrees.

    overlap_nearby_range_multiplier
Set nearby vehicle overlap detection range multiplier that scales with vehicle width. A value of `5` would result a 5-vehicle-wide detection range. Default is `5` vehicle-wide.

    overlap_critical_range_multiplier
Set nearby vehicle critical overlap detection range multiplier that scales with vehicle width. Default is `1` vehicle-wide.

    indicator_size_multiplier
Set indicator size multiplier that scales with vehicle width.

    show_center_mark
Show center mark on radar.

    center_mark_style
Set center mark line style. `0` for dashed line, `1` for solid line.

    center_mark_radius
Set center mark size by radius(unit meter).

    center_mark_width
Set center mark line width in pixels.

    show_angle_mark
Show angle mark (fixed 45 degrees) on radar.

    show_distance_circle
Show distance circle line on radar for distance reference.

    distance_circle_*_style
Set distance circle line style. `0` for dashed line, `1` for solid line.

    distance_circle_*_radius
Set distance circle size by radius(unit meter). Circle will not be displayed if radius is bigger than `radar_radius`.

    distance_circle_*_width
Set distance circle line width in pixels.

    auto_hide
Auto hides radar display when no nearby vehicles.

    auto_hide_in_private_qualifying
Auto hides radar in private qualifying session, requires both `auto_hide` and [RestAPI Module](#restapi-module) enabled.

    auto_hide_time_threshold
Set amount time(unit second) before triggering auto hide. Default is `1` second. Note, this option has no effect while `enable_radar_fade` is enabled.

    auto_hide_minimum_distance_ahead, behind, side
The three values define an invisible rectangle area(unit meter) that auto hides radar if no vehicle is within the rectangle area. Default value is `-1`, which auto scales with `radar_radius` value. Set to any positive value to customize radar auto-hide range. Note, each value is measured from center of player's vehicle position.

    vehicle_maximum_visible_distance_ahead, behind, side
The three values define an invisible rectangle area(unit meter) that hides any vehicle outside the rectangle area. Default value is `-1`, which auto scales with `radar_radius` value. Set to any positive value to customize vehicle visible range. Note, each value is measured from center of player's vehicle position.

[**`Back to Top`**](#)


## Rake angle
**This widget displays vehicle rake info.**

    wheelbase
Set wheelbase in millimeters, for used in rake angle calculation.

    show_degree_sign
Set `true` to show degree sign for rake angle value.

    show_ride_height_difference
Show average front and rear ride height difference in millimeters.

[**`Back to Top`**](#)


## Relative
**This widget displays relative standings info.**

    show_player_highlighted
Highlight player row with customizable specific color.

    show_lap_difference
Show different font color based on lap difference between player and opponents. Note, this option will override `font_color` setting from `position`, `driver name`, `vehicle name`.

    font_color_same_lap, font_color_laps_ahead, font_color_laps_behind
Set font color for lap difference. Note, `font_color_laps_ahead` and `font_color_laps_behind` applies to race session only.

    show_position
Show overall position standings.

    show_position_change
Show overall driver position change relative to overall qualification position.

    show_position_change_in_class
Show driver position change in class instead of overall. This option is enabled by default.

    show_driver_name
Show driver name.

    driver_name_shorten
Shorten driver's first name to a single letter with a period separating driver's last name, and any middle names will not be displayed. Note, if a driver is using nickname that consists only a single word, the name will not be shortened.

    driver_name_uppercase
Set driver name to uppercase.

    driver_name_width
Set drive name display width, value in chars, such as 10 = 10 chars.

    driver_name_align_center
Align driver name in the center when enabled. Default is left alignment when disabled.

    show_vehicle_name
Show vehicle name. Note, game API outputs `skin livery name` as `vehicle name`, which means actual displayed name depends on what skin livery name is called. For example, some vehicles may add `team name` and/or `class name` in `skin livery name`, some may not.

    show_vehicle_brand_as_name
Show vehicle brand name instead of vehicle name. If brand name does not exist, vehicle name will be displayed instead.

    vehicle_name_uppercase
Set vehicle name to uppercase.

    vehicle_name_width
Set vehicle name display width, value in chars, such as 10 = 10 chars.

    vehicle_name_align_center
Align vehicle name in the center when enabled. Default is left alignment when disabled.

    show_brand_logo
Show user-defined brand logo if available.

    brand_logo_width
Set maximum brand logo display width in pixels. Note, maximum brand logo display height is automatically adapted to `font_size`.

    show_time_gap
Show relative time gap between player and opponents.

    show_time_gap_sign
Show plus or minus sign for time gap. `-` sign indicates opponent's relative position is in front of player, `+` sign indicates the opposite.

    time_gap_width
Set time gap display width, value is in chars, 5 = 5 chars wide.

    time_gap_align_center
Align time gap in the center when enabled. Default is right alignment when disabled.

    show_highlighted_nearest_time_gap
Show highlighted color on opponents within nearest time gap threshold.

    nearest_time_gap_threshold_front, nearest_time_gap_threshold_behind
Set nearest time gap threshold (in seconds) for opponent who is in front of or behind player. Default is `1` second for front, and `2` seconds for behind.

    show_laptime
Show driver's last lap time and pit timer if available.

    show_highlighted_fastest_last_laptime
Highlight the fastest last lap time within the same class if available.

    show_position_in_class
Show driver's position standing in class.

    show_class
Show vehicle class categories. Class name and color are fully customizable, see [Vehicle Class Editor](#vehicle-class-editor) section for details.

    show_random_color_for_unknown_class
Show random color for unknown class name that is not defined in `classes.json` preset.

    class_width
Set class name display width, value is in chars, 4 = 4 chars wide.

    show_pit_status
Show indicator whether driver is currently in pit or garage.

    pit_status_text
Set custom pit status text which shows when driver is in pit.

    garage_status_text
Set custom garage status text which shows when driver is in garage.

    show_tyre_compound
Show tyre compound symbols (front and rear) that matches specific tyre compounds defined in `compounds.json` preset.

    show_pitstop_count
Show each driver's pit stop count and penalty count if available. Note, when a driver accumulates one or more penalties, this column will show the number of penalties in negative value with purple (default) background to distinguish from number of pit stops.

    show_pit_request
Show pit request color indicator on pit stop count column.

    show_vehicle_in_garage
Show vehicles parked in garage stall. Default is `false`. Note, local player is always displayed.

    additional_players_front, additional_players_behind
Set additional players shown on relative list. Each value is limited to a maximum of 60 additional players (for a total of 120 additional players). Default is `0`.

[**`Back to Top`**](#)


## Relative finish order
**This widget displays estimated relative finish order between leader and local player with corresponding refilling estimate in a table view.**

**Overview**

This widget predicts `relative final lap progress` (percent into lap) at the moment when session timer ended in time-type race, or leader crossed finish line in laps-type race, which can be used to determine whether extra laps are required to finish race.

Simple example: in time-type race, at the moment when session timer ended, assume race leader's vehicle is in `Sector 1` (or 20% into lap), and local player is in `Sector 3` (or 80% into lap) which is ahead of leader in terms of `relative lap progress` (0% from start line to 100% at finish line). When local player finishes his current lap, the race does not end for him because leader is behind local player and has not yet crossed finish line. This means local player has to complete another lap in order to finish the race, and needs an extra lap of fuel.

---

The table consists of 5 fixed rows, 1 optional row, 3 fixed columns, and 10 optional predication columns that can be customized. Example:

| TIME |   0s  |  30s  |  40s  |  50s  |  60s  |  54s  |
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|  LDR |  0.49 |  0.20 |  0.11 |  0.02 |  0.92 |  0.98 |
| 0.04 |  0.91 |  0.64 |  0.55 |  0.46 |  0.37 |  0.51 |
| DIFF |   0s  |  30s  |  40s  |  50s  |  60s  |  43s  |
|  NRG | +18.1 | +18.1 | +18.1 | +18.1 | +18.1 | +18.1 |
| EX+1 | +20.3 | +20.3 | +20.3 | +20.3 | +20.3 | +20.3 |

First and fourth rows, starting from second cell, show estimated `leader's pit time` and `local player's pit time`, where first row first cell shows current session type in `TIME` or `LAPS`. Last cell shows last recorded total time that leader and local player had spent in pit. Note, last recorded total pit time counts from pit entry to pit exit point, it doesn't include the extra few seconds that spent while approaching or exiting from pit.

Second and third rows, starting from second cell, show estimated `leader's final lap progress` (fraction of lap) and `local player's final lap progress` that depend on current session type:
* For `TIME` type race, it shows final lap progress at the moment when session timer ended.
* For `LAPS` type race, it shows relative final total lap difference between leader and local player.  
Leader's value from second row second cell always shows `integer value`, because laps-type race has no timer, and the end of race is determined at the moment when leader crossed finish line, which can only be full laps.  
Local player's value from third row second cell always shows final lap progress relative to leader's value from second row second cell.  
Both leader's and local player's `final lap progress` values starting from third cell are offset from second cell of same row.

Third row, first cell shows `relative lap difference` between leader and local player that is calculated from lap time pace difference of both players, which can be used to determine whether leader has the chance to overtake local player on final lap. For example:
* If relative lap difference value shows 0.25, that means for every full lap, leader is faster than local player by 0.25 lap. If leader is at start line and player is just within 0.25 lap distance from leader, that means leader can catch up and overtake player before the end of lap.
* If relative lap difference value shows 0.25 and leader is at middle of current lap (0.5 lap), that means leader now only has roughly half of the lap distance (0.12 lap) to make successful overtake before the end of lap. If player is not within this 0.12 lap distance, then leader may not be able to overtake.

Fifth row, first cell shows refilling type in `FUEL` or `NRG` (if virtual energy available). Starting from second cell, shows estimated `local player's refilling` that depends on current session type:
* For `TIME` type race, refilling value from each column is calculated based on local player's current `laptime pace`, `consumption`, and `local player's final lap progress` from third row of same column. Note, each refilling value has no relation to `leader's final lap progress` value from same column. Refilling value from `0s` column gives same reading as seen from `Fuel` or `Virtual Energy` Widget in time-type race.
* For `LAPS` type race, only refilling value from `0s` column is calculated and displayed according to leader's `leader's final lap progress` value.  
Other column values are not displayed, this is done to avoid confusion. Because unlike `TIME` type race where all `final lap progress` values are within `0.0` to `1.0` range, in `LAPS` type race values can exceed `1.0` or below `0.0` (negative), which the number of possible lap differences would increase exponentially and not possible to list all of them in the widget.

Sixth row (optional), first cell shows `number of extra laps` for extra refilling display. Starting from second cell, shows estimated `extra refilling` value that depends on `local player's refilling` value and `number of extra laps` setting. Each extra refilling value equals `extra laps of consumption` plus `local player's refilling` value of same column. Those values save the trouble from manual calculation in case there will be extra laps.

See `TIME` or `LAPS` type race example usages below for details.

---

**Important notes**

* Predication accuracy depends on many variables and is meant for final stint estimate. Such as laptime pace, pit time, penalties, weather condition, safety car, yellow flag, can all affect predication accuracy. It requires at least 2-3 laps to get sensible readings, and more laps to have better accuracy.

* `Final lap progress` values will not be displayed if no corresponding valid lap time pace data found, which requires at least 1 or 2 laps to record. If local player is the leader, then all values from leader's row will not be displayed. Refilling values will not be displayed during formation lap for the reasons mentioned in first note.

* Refilling estimate calculation is different between `TIME` and `LAPS` type races, make sure to look at the correct value, check out `example usage` below for details.

* `LMU` currently uses `absolute refueling` mechanism (amount `total` fuel to fill tank up to), as opposite to relative fuel (amount to `add` on top of remaining fuel in tank). User can enabled `show_absolute_refilling` option to display total amount fuel/energy required (including fuel/energy in tank) to finish race.

---

**Time-type race example usage**

| TIME | 0s   | 30s  | 40s  | 50s  | 60s  | 0s   |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| LDR  | 0.38 | 0.10 | 0.01 | 0.91 | 0.82 | 0.38 |
| 0.11 | 0.72 | 0.47 | 0.39 | 0.31 | 0.22 | 0.37 |
| DIFF | 0s   | 30s  | 40s  | 50s  | 60s  | 43s  |
| FUEL | +7.4 | +7.4 | +7.4 | +7.4 | +7.4 | +7.4 |
| EX+1 | +11.2 | +11.2 | +11.2 | +11.2 | +11.2 | +11.2 |

1. Determine leader's next pit time and select `leader's final lap progress` (second row) value from corresponding pit time (first row) column. `0s` column means no pit stop.

2. Determine local player's next pit time and select `local player's final lap progress` (third row) value from corresponding pit time (fourth row) column.

3. Compare the two `final lap progress` values from leader and local player, assume fuel per lap is `3.8`:

    * If leader's `final lap progress` value is greater than local player, such as leader's 0.91 (50s column) vs player's 0.47 (30s column), it indicates that leader will be ahead of local player when timer ended, and there will be no extra final lap. So `local player's refilling` value from corresponding `30s` column can be used, in this case, it's `+7.4` fuel to add.  
    However, if leader is closer to finish line (as show in orange color indicator), there is a chance that leader may be fast enough to cross finish line before the end of timer, which would result an extra final lap for local player, and requires adding an extra lap of fuel (`3.8`) on top of `+7.4` fuel. In this case it would be `+11.2` refuel, or you can simply look at the refuel value from `extra refilling row` of same column.

    * If local player's `final lap progress` value is greater than leader, such as leader's 0.10 (30s column) vs player's 0.39 (40s column), it indicates that local player will be ahead of leader when timer ended, and there will be an extra final lap for local player, and here again requires adding an extra lap of fuel (`3.8`) on top of `+7.4` fuel from `40s` column, which is `+11.2` refuel.  
    However, if the difference between the two `final lap progress` values is smaller than `relative lap difference` (from third row first cell) value, it may indicate that leader could overtake local player on final lap, which would result no extra final lap.

4. To sum up, if comparison shows no extra final lap, then just refill according to `local player's refilling` (fifth row) value from the same column of `local player's final lap progress` (third row). If comparison shows an extra final lap, then just add an extra lap of fuel on top of `local player's refilling` value; or, just look at the refuel value from `extra refilling row` of same column.


**Laps-type race example usage**

Note, there is generally no reason to use this widget in `LAPS` type race unless you are doing multi-class laps-type race which is very rarely seen.

| LAPS | 0s    | 30s  | 40s   | 50s   | 60s   | 0s   |
|:----:|:-----:|:----:|:-----:|:-----:|:-----:|:----:|
| LDR  | 2.00  | 1.57 | 1.43  | 1.28  | 1.14  | 2.00 |
| 0.11 | 0.40  | 0.02 | -0.11 | -0.24 | -0.37 | 0.40 |
| DIFF | 0s    | 30s  | 40s   | 50s   | 60s   | 43s  |
| FUEL | +12.8 | -    | -     | -     | -     | -    |
| EX+1 | +15.0 | -    | -     | -     | -     | -    |

1. Determine leader's next pit time and select `leader's final lap progress` (second row) value from corresponding pit time (first row) column. `0s` means no pit stop.

2. Determine local player's next pit time and select `local player's final lap progress` (third row) value from corresponding pit time (fourth row) column.

3. Subtract `local player's final lap progress` value from `leader's final lap progress`, then round down value:

    * If leader's `final lap progress` value is 2.00 (0s column), and local player's `final lap progress` value is 0.40 (0s column), then after subtracting (2 - 0.4 = 1.6) and rounding down, the final value is `1` lap difference, which means local player will do `one less lap` than leader.  
    As mentioned earlier, for laps-type race, refilling value from `0s column` is calculated according to leader's `leader's final lap progress` value, which any lap difference is already included in the result from `local player's refilling` value (fifth row second cell), in this case, it's `+12.8` fuel to add.  

    * If leader's `final lap progress` value is 1.43 (40s column), and local player's `final lap progress` value is -0.24 (50s column), then after subtracting (1.43 - -0.24 = 1.67) and rounding down, the final value is also `1` lap difference, which means local player will do the same `one less lap` than leader. So in this case, it's still `+12.8` fuel to add.  

    * If leader's `final lap progress` value is 2.00 (0s column), and local player's `final lap progress` value is -0.11 (40s column), then after subtracting (2 - -0.11 = 2.11) and rounding down, the final value is `2` lap difference, which means local player will do `two less laps` than leader. So an extra lap of fuel may be removed from `local player's refilling` value from fifth row second cell, in this case, it's `12.8` minus one lap of fuel `2.2`, equals `+10.6` fuel to add. Alternatively, it can be calculated from full lap refuel (as show in Fuel Widget), which will be `15.0` minus two lap of fuel `4.4`, and equals `+10.6` fuel to add.  
    Be aware that carrying less fuel is risky in laps-type race due to reasons below.

4. Last note, since the end of laps-type race is determined by the moment that leader completed all race laps, leader can greatly affect final predication outcome. To give an extreme example, if leader is ahead of everyone by a few laps, and decides to wait a few minutes on his final lap before finish line, then everyone else will be catching up and do a few `extra laps` which would require more fuel. Thus it is always risky to carry less fuel in laps-type race.

---

    layout
2 layouts are available: `0` = show columns from left to right, `1` = show columns from right to left.

    near_start_range
Set detection range (in seconds) near (after) start/finish line to show color indicator when vehicle is within the range (or less). Default is `20` seconds. Default color is green.

    near_finish_range
Set detection range (in seconds) near (before) start/finish line to show color indicator when vehicle is within the range (or less). Default is `20` seconds. Default color is orange.

    leader_laptime_pace_samples
Set number of samples for average laptime pace calculation (EMA). Value range in `1` to `20`. Default is `6` samples. Set `1` to disable averaging.

Note, initial laptime pace is always based on leader's session personal best laptime if available. If a new laptime is faster than current laptime pace, it will replace current laptime pace without calculating average. Invalid lap, pit-in/out laps are always excluded from laptime pace calculation.

    leader_laptime_pace_margin
Set additional margin for laptime pace that cannot exceed the sum of previous `laptime pace` and `margin`. This option is used to minimize the impact of unusually slow laptime. Default value is `5` seconds. Minimum value is limited to `0.1`.

    show_absolute_refilling
Show absolute refilling value instead of relative refilling when enabled. Note, `+` or `-` sign is not displayed with absolute refilling.

    show_extra_refilling
Show readings of extra refilling row below `local player's refilling` row. Each extra refilling value equals `extra laps of consumption` plus `local player's refilling` value of same column. Those values save the trouble from manual calculation in case there will be extra laps.

The first column of extra refilling row shows number of extra laps depends on `number of extra laps` setting, such as `EX+1` for 1 extra lap, or `EX+3` for 3 extra laps.

    number_of_extra_laps
Set number of extra laps for extra refilling calculation. Default is `1` extra lap.

    number_of_predication
Set number of optional predication columns with customizable pit time. Value range in `0` to `10`. Default is `4` extra customizable columns.

    predication_*_leader_pit_time, predication_*_player_pit_time
Set predication pit time for leader or local player.

[**`Back to Top`**](#)


## Ride height
**This widget displays visualized ride height info.**

    ride_height_max_range
Set visualized maximum ride height display range (millimeter).

    rideheight_offset*
Set ride height offset for bottoming indicator. Value in millimeters, but without decimal place.

[**`Back to Top`**](#)


## Rivals
**This widget displays standings info from opponent ahead and behind local player from same vehicle class.**

Note, most options are inherited from [Relative](#relative) and [Standings](#standings) widgets, with some additions noted below.

    time_interval_align_center
Align time interval in the center when enabled. Default is right alignment when disabled.

    *_color_time_interval_ahead, *_color_time_interval_behind
Set custom time interval color of opponent ahead and behind.

[**`Back to Top`**](#)


## Sectors
**This widget displays sectors timing info.**

    layout
2 layouts are available: `0` = target and current sectors above deltabest sectors, `1` = deltabest sectors above target and current sectors.

    target_laptime
Set target laptime for display target reference lap and sector time. Set `Theoretical` to show theoretical best sector time. Set `Personal` to show sector time from personal best lap time. Note, if `enable_all_time_best_sectors` option is enabled in `Sectors Module`, all time best sectors data will be displayed instead, otherwise only current session best sectors data will be displayed.

    freeze_duration
Set freeze duration (seconds) for displaying previous sector time. Default is `5` seconds.

[**`Back to Top`**](#)


## Session
**This widget displays system clock, session name, timing, lap number, overall position info.**

    show_session_name
Show current session name that includes testday, practice, qualify, warmup, race.

    session_text_*
Set custom session name text.

    show_system_clock
Show current system clock time.

    system_clock_format
Set clock format string. To show seconds, add `%S`, such as `%H:%M:%S %p`. See [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for full list of format codes.

    show_session_time
Show total remaining session time.

    show_estimated_laps
Show estimated total remaining laps (from current lap position towards finish line) based on total remaining session time and local player's lap time pace. This value can be used for adjusting absolute refueling.

Note, this is the same value that used for calculating estimated refueling value in Fuel Module. As with estimation, there may be a margin of error of one lap, and may be affected by other variables such as those mentioned in [Relative Finish Order](#relative-finish-order) widget.

[**`Back to Top`**](#)


## Slip ratio
**This widget displays visualized slip ratio info.**

    slip_ratio_optimal_range
Set optimal slip ratio range (percentage) for optimal and critical slip ratio color indication, value range in `0` to `100`. Default is `30` percent.

    slip_ratio_max_range
Set visualized maximum slip ratio display range (percentage), value range in `10` to `100`. Default is `50` percent.

[**`Back to Top`**](#)


## Speedometer
**This widget displays conditional speed info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_speed
Show current vehicle speed.

    show_speed_minimum
Show minimum speed that is updated while off throttle.

    show_speed_maximum
Show maximum speed that is updated while on throttle.

    show_speed_fastest
Show fastest recorded speed. To reset current record, shift gear into reverse, or reload preset.

    off_throttle_threshold
Set throttle threshold which counts as off throttle if throttle position is lower, value range in `0.0` to `1.0`. Default is `0.5`.

    on_throttle_threshold
Set throttle threshold which counts as on throttle if throttle position is higher, value range in `0.0` to `1.0`. Default is `0.01`.

    speed_minimum_reset_cooldown, speed_maximum_reset_cooldown
Set cooldown duration (seconds) before resetting minimum or maximum speed value.

[**`Back to Top`**](#)


## Standings
**This widget displays standings info.**

Note, most options are inherited from [Relative](#relative) widget, with some additions noted below.

    max_vehicles_combined_mode
Set maximum amount vehicles to display, which takes effect when `enable_multi_class_split_mode` is not enabled. When total vehicle number is lower than this value, extra rows will auto-hide. When total vehicle number is above this value, the top 3 vehicles will always show, and rest of the vehicles will be selected from the nearest front and behind places related to player.

    max_vehicles_split_mode
Set maximum amount vehicles to display, which takes effect when in multi-class session and `enable_multi_class_split_mode` is enabled. If total vehicle number is above this value, any extra vehicles will not be shown. Default is `50`, which is sufficient in most case.

    min_top_vehicles
Set minimum amount top place vehicles to display. This value has higher priority than other `max_vehicles` settings. Default is `3`, which always shows top 3 vehicles if present.

    enable_multi_class_split_mode
Enable multi-class split mode, which splits and displays each vehicle class in separated groups. This mode will only take effect when there is more than one vehicle class present in a session, otherwise it will automatically fall back to normal single class mode.

    max_vehicles_per_split_player
Set maximum amount vehicles to display for class where player is in. Default is `7`. Note that, if player is not in first place, then at least one opponent ahead of player will always be displayed, even if this value sets lower.

    max_vehicles_per_split_others
Set maximum amount vehicles to display for classes where player is not in. Default is `3`.

    split_gap
Set split gap between each class.

    show_time_gap
For race session, this option shows time gap between leader and all other drivers. For other none race sessions, this option shows the time gap between session's best lap time and all other drivers.

    show_time_gap_from_class_best
Show time gap from none race session's best lap time of the same vehicle class.

    time_gap_leader_text
Set text indicator for race leader in time gap column.

    show_time_interval
Show time interval between each closest driver in order.

    show_time_interval_from_same_class
Show time interval from same class. This option only takes effect while `enable_multi_class_split_mode` is enabled.

    time_interval_leader_text
Set text indicator for race leader in time interval column.

    show_laptime
Show driver's last lap time or pit timer if available. If `show_best_laptime` is not enabled, this option will show driver's session best lap time in none-race sessions.

    show_best_laptime
Show driver's session best lap time.

    show_delta_laptime
Show lap time difference (delta) between player and opponents from most recent laps (up to 5 recent lap time records). The default layout order shows delta lap time records from right side column (most recent lap) to left.

A green color (default) delta indicates that player's recent lap time is faster than opponent, while orange color delta indicates the opposite.

    show_inverted_delta_laptime_layout
Enable this option to invert layout order for delta lap time records.

    number_of_delta_laptime
Set number of delta lap time records to display. Minimum number is limited to `2`, maximum is limited to `5`.

[**`Back to Top`**](#)


## Steering
**This widget displays steering input info.**

    bar_width, bar_height
Set steering bar width and height in pixels.

    bar_edge_width
Set left and right edge boundary width.

    manual_steering_range
Manually set steering display range in degree. Set to `0` to read physical steering range from API. This option may be useful when steering range value is not provided by some vehicles.

    show_steering_angle
Show steering angle text in degree.

    show_scale_mark
This enables scale marks on steering bar.

    scale_mark_degree
Set gap between each scale mark in degree. Default is `90` degree. Minimum value is limited to `10` degree.

[**`Back to Top`**](#)


## Steering wheel
**This widget displays virtual steering wheel.**

    show_custom_steering_wheel
Show user-defined custom steering wheel image instead of default image.

    custom_steering_wheel_image_file
Set custom steering wheel image file path. Double-click this option in widget's `Config` dialog to select an image file.

Note, image file must be in `PNG` format with same width and height. Maximum supported `PNG` file size is limited to `5MB`. Default image will be used if selected image is not valid.

    display_size
Set widget display size in pixels.

    display_margin
Set widget display margin in pixels.

    show_steering_angle
Show steering angle text in degree.

    manual_steering_range
Manually set steering display range in degree. Set to `0` to read physical steering range from API. This option may be useful when steering range value is not provided by some vehicles.

    show_rotation_line
Show steering rotation reference line, which can be useful to see if physical steering wheel is misaligned.

    show_rotation_line_while_stationary_only
Show rotation line only while vehicle is stationary (less than 1m/s).

[**`Back to Top`**](#)


## Stint history
**This widget displays stint history info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = reversed vertical layout.

    stint_history_count
Set the number of stint history display. Default is to show `2` most recent stints.

    show_virtual_energy_if_available
Show virtual energy consumption instead of fuel consumption if available. This option is enabled by default.

    show_empty_history
Show empty stint history. Default is `false`, which hides empty rows.

    minimum_stint_threshold_minutes
Set the minimum stint time threshold in minutes for updating stint history. This only affects ESC.

[**`Back to Top`**](#)


## Suspension force
**This widget displays visualized suspension force and ratio info.**

    show_force_ratio
Show percentage force ratio between each and total suspension force. Set `false` to show individual suspension force in Newtons.

[**`Back to Top`**](#)


## Suspension position
**This widget displays visualized suspension position info.**

    position_max_range
Set visualized maximum suspension position display range (millimeter).

    show_third_spring_position_mark
Show front and rear third spring position mark relative to each suspension position.

[**`Back to Top`**](#)


## System performance
**This widget displays system performance info.**

    show_system_performance
Show system's overall CPU utilization (percent) and memory usage (GB). Note, sampling interval is determined by `update_interval` setting.

    show_tinypedal_performance
Show TinyPedal's CPU utilization (percent) and memory usage (MB).

    average_samples
Set number of samples for average CPU utilization calculation (EMA). Value range in `1` to `500`. Lower value may result more fluctuated reading. Set `1` to disable averaging.

[**`Back to Top`**](#)


## Timing
**This widget displays lap time info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_session_best
Show current session best lap time from all vehicle classes.

    show_session_best_from_same_class_only
Show current session best lap time from same vehicle class only.

    show_best
Show personal all time best lap time.

    show_last
Show personal last lap time.

    show_current
Show personal current lap time.

    show_estimated
Show personal current estimated lap time.

    show_session_personal_best
Show personal current session best lap time.

    show_stint_best
Show personal current stint best lap time.

    show_average_pace
Show personal current average lap time pace, this reading is also used in real-time fuel calculation. Note, additional `average lap time pace` calculation setting can be found in [Delta Module](#delta-module) config. After ESC or session ended, lap time pace reading will be reset, and aligned to `all time personal best lap time` if available.

[**`Back to Top`**](#)


## Track map
**This widget displays track map and standings. Note: at least one complete and valid lap is required to generate track map.**

    display_orientation
Set track map display orientation in degrees. For example, a `270` value will rotate map by `270` degrees clockwise. Default value is `0`, which always displays track map `North Up` in game's coordinate system.

    display_detail_level
Sets detail level for track map. Default value is `1`, which auto adjusts map detail according to display size. Higher value reduces map detail and RAM usage, and may also help reduce rough edges from large map. Set to `0` for full detail.

    area_size
Set area display size.

    area_margin
Set area margin size.

    show_background
Show widget background.

    show_map_background
Show background of the inner map area. This option only works for circular type tracks.

    map_width
Set track map line width.

    map_outline_width
Set track map outline width.

    show_start_line
Show start line mark.

    show_sector_line
Show sector line mark.

    show_vehicle_standings
Show vehicle standings info on track map. Note, if `enable_multi_class_styling` is enabled, position in class will be displayed for each vehicle class instead.

    enable_multi_class_styling
Show vehicles in multi-class color styles on map instead. Multi-class color can be customized from [Vehicle Class Editor](#vehicle-class-editor).

Note, while multi-class styling is enabled, following color styles will not be displayed:
`vehicle_color_player`, `vehicle_color_leader`, `vehicle_color_same_lap`, `vehicle_color_laps_ahead`, `vehicle_color_laps_behind`.

    show_position_in_class
Show position in class while `enable_multi_class_styling` option is also enabled, otherwise this option has no effect.

    show_pitout_prediction
Show estimated pit out on-track position indication for each pit stop duration. Default indication shows `circle` with `pit stop duration` displayed above.

Note, pit out position prediction is based on `delta best` data which scaled with player's latest `lap time pace` for accurate real-time position prediction under various track conditions. Pit out prediction requires both valid `track map` and `delta best` data to display. At least `one valid lap` for any car and track combo is required to display pit out prediction.

For accurate prediction, the location of `pit out line` must be found first. And since each track has different pit out line location, it is required to `pit out` at least `once per session` to mark the correct pit out line location. This can be easily done by driving out of pit lane.

    show_pitout_prediction_while_requested_pitstop
Show estimated pit out on-track position indication while player has requested pitstop and not in pit lane.

    number_of_predication
Set number of pit out predication to display. Value range is limited in `1` to `20`.

    pitstop_duration_minimum
Set pit stop duration (in seconds) of first predication.

    pitstop_duration_increment
Set each pit stop duration (in seconds) increment after previous predication. Default increment is `10` seconds.

Note, each time when pit stop duration of the nearest predication exceeded current pit stop timer, the predication circle will be removed, and a new predication circle will be appended with pit stop duration increment after the last predication.

    pitout_time_offset
Set amount time offset (in seconds) for catching up with vehicle speed after pit out. Default is `3` seconds.

Note, this value is important for accurate prediction, as initial vehicle speed is much slower after pit out, so extra time is needed for driver to catch up, and also affected by pit out line location. For most tracks, this extra time after pit out is roughly within `1` to `5` seconds.

    show_pitstop_duration
Show pit stop duration reading on top of each predication circle.

[**`Back to Top`**](#)


## Track notes
**This widget displays track notes, comments, debugging info.**

    show_background
Show background color. Turn off to show text only.

    show_track_notes
Show nearest track notes info behind current vehicle position.

    track_notes_uppercase
Set track notes text to uppercase.

    show_comments
Show nearest track notes comments info behind current vehicle position.

    enable_comments_line_break
Enable line break for displaying multi-line comments. To break a line into multiple lines, add `\n` to any part of the comment.

    show_debugging
Show nearest track notes index number behind current vehicle position, and distance value (meters) behind current position to next index position.

    track_notes_width, comments_width, debugging_width
Set maximum display width, value in chars, such as 10 = 10 chars.

    auto_hide_if_not_available
Auto hide this widget if track notes data is not available for current track.

    maximum_display_duration
Set maximum display duration (seconds) of each note. Set to `-1` to always display notes. Default is `-1`.

[**`Back to Top`**](#)


## Trailing
**This widget displays pedal input and force feedback plots.**

    display_width
Set pedal plot display width in pixels.

    display_height
Set pedal plot display height in pixels.

    display_margin
Set pedal plot display margin (vertical relative to pedal) in pixels.

    display_scale
Set plot display scale. Default scale is `2`. Minimum scale is limited to `1`.

    show_inverted_pedal
Invert pedal range display.

    show_inverted_trailing
Invert trailing direction.

    show_throttle
Show filtered throttle plot. Note, some vehicles may not provide filtered pedal input value, which the value will be zero.

    show_raw_throttle
Show unfiltered throttle instead.

    show_absolute_ffb
Convert force feedback value to absolute value before plotting. Set to `false` to show force feedback plot in both positive and negative range.

    *_line_width
Set trailing line width in pixels.

    *_line_style
Set trailing line style. `0` for solid line, `1` for dashed line.

    show_wheel_lock
Show wheel lock (slip ratio) plot under braking when slip ratio has exceeded `wheel_lock_threshold` value.

    wheel_lock_threshold
Set percentage threshold for triggering wheel lock warning under braking. `0.3` means 30% of tyre slip ratio.

    show_wheel_slip
Show wheel slip (slip ratio) plot under acceleration when slip ratio has exceeded `wheel_slip_threshold` value.

    wheel_slip_threshold
Set percentage threshold for triggering wheel slip warning under acceleration. `0.1` means 10% of tyre slip ratio.

    show_reference_line
Show reference line.

    reference_line_*_offset
Set reference line vertical offset position (percentage) relative to pedal, value range in `0.0` to `1.0`.

    reference_line_*_style
Set reference line style. `0` for solid line, `1` for dashed line.

    reference_line_*_width
Set reference line width in pixels. Set value to `0` to hide line.

    draw_order_index_*
Set draw order of plot lines.

[**`Back to Top`**](#)


## Tyre carcass temperature
**This widget displays tyre carcass temperature info.**

Note, if temperature drops below `-100` degrees Celsius, temperature readings will be replaced by unavailable sign as `-`.

    enable_heatmap_auto_matching
Enable automatically heatmap style matching for specific tyre compounds defined in `compounds.json` preset. This option applies matching heatmap style to front and rear tyre compounds separately.

Note, separate compounds info for tyres on the same axle is not available from game API, which currently it is not possible to show left and right compounds separately.

    heatmap_name
Set heatmap preset name that is defined in `heatmap.json` preset. Note, this option has no effect while `enable_heatmap_auto_matching` is enabled.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_rate_of_change
Show carcass temeperature rate of change for a specific time interval.

    rate_of_change_interval
Set time interval in seconds for rate of change calculation. Default interval is `5` seconds. Minimum interval is limited to `1` second, maximum interval is limited to `60` seconds.

    rate_of_change_smoothing_samples
Set number of samples for rate of change data smoothing calculation (EMA). Value range in `1` to `500`. Lower value may result more fluctuated reading. Set `1` to disable smoothing.

    show_tyre_compound
Show tyre compound symbols (front and rear) that matches specific tyre compounds defined in `compounds.json` preset.

[**`Back to Top`**](#)


## Tyre inner layer
**This widget displays tyre inner layer temperature info.**

Note, if temperature drops below `-100` degrees Celsius, temperature readings will be replaced by unavailable sign as `-`.

    enable_heatmap_auto_matching
Enable automatically heatmap style matching for specific tyre compounds defined in `compounds.json` preset. This option applies matching heatmap style to front and rear tyre compounds separately.

Note, separate compounds info for tyres on the same axle is not available from game API, which currently it is not possible to show left and right compounds separately.

    heatmap_name
Set heatmap preset name that is defined in `heatmap.json` preset. Note, this option has no effect while `enable_heatmap_auto_matching` is enabled.

    swap_style
Swap heatmap color between font and background color.

    show_inner_center_outer
Set inner, center, outer temperature display mode. Set `false` to show average temperature instead.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_tyre_compound
Show tyre compound symbols (front and rear) that matches specific tyre compounds defined in `compounds.json` preset.

[**`Back to Top`**](#)


## Tyre load
**This widget displays visualized tyre load and ratio info.**

    show_tyre_load_ratio
Show percentage load ratio between each and total tyre load. Set `false` to show individual tyre load in Newtons.

[**`Back to Top`**](#)


## Tyre pressure
**This widget displays tyre pressure info.**

[**`Back to Top`**](#)


## Tyre temperature
**This widget displays tyre surface temperature info.**

Note, if temperature drops below `-100` degrees Celsius, temperature readings will be replaced by unavailable sign as `-`.

    enable_heatmap_auto_matching
Enable automatically heatmap style matching for specific tyre compounds defined in `compounds.json` preset. This option applies matching heatmap style to front and rear tyre compounds separately.

Note, separate compounds info for tyres on the same axle is not available from game API, which currently it is not possible to show left and right compounds separately.

    heatmap_name
Set heatmap preset name that is defined in `heatmap.json` preset. Note, this option has no effect while `enable_heatmap_auto_matching` is enabled.

    swap_style
Swap heatmap color between font and background color.

    show_inner_center_outer
Set inner, center, outer temperature display mode. Set `false` to show average temperature instead.

    show_degree_sign
Set `true` to show degree sign for each temperature value.

    leading_zero
Set amount leading zeros for each temperature value. Default is `2`. Minimum value is limited to `1`.

    show_tyre_compound
Show tyre compound symbols (front and rear) that matches specific tyre compounds defined in `compounds.json` preset.

[**`Back to Top`**](#)


## Tyre wear
**This widget displays tyre wear info.**

    layout
2 layouts are available: `0` = vertical layout, `1` = horizontal layout.

    show_remaining
Show total remaining tyre in percentage that changes color according to wear.

    show_wear_difference
Show total tyre wear difference of previous lap.

    show_live_wear_difference
Show tyre wear difference of current lap that constantly updated.

    freeze_duration
Set freeze duration (seconds) for displaying previous lap tyre wear if `show_live_wear_difference` is enabled. Value range in `0` to `30` seconds. Default is `10` seconds.

    show_lifespan_laps
Show estimated tyre lifespan in laps.

    show_lifespan_minutes
Show estimated tyre lifespan in minutes.

    warning_threshold_remaining
Set warning threshold for total remaining tyre in percentage. Default is `30` percent.

    warning_threshold_wear
Set warning threshold for total amount tyre wear of last lap in percentage. Default is `3` percent.

    warning_threshold_laps
Set warning threshold for estimated tyre lifespan in laps. Default is `5` laps.

    warning_threshold_minutes
Set warning threshold for estimated tyre lifespan in minutes. Default is `5` laps.

[**`Back to Top`**](#)


## Virtual energy
**This widget displays virtual energy usage info.**

Note, most options are inherited from [Fuel](#fuel) widget, with some additions noted below.

Virtual energy is not `real energy`, and different from `battery charge`. For battery charge usage info, see [Battery](#battery) widget.

    show_absolute_refilling
Show absolute refilling value instead of relative refilling when enabled. Note, `+` or `-` sign is not displayed with absolute refilling.

    *ratio
Show fuel ratio between estimated fuel and energy consumption, which can help balance fuel and energy usage, as well as providing refueling reference for adjusting pit stop `Fuel ratio` during race.

    *bias
Show fuel bias (unit in laps) that calculated from estimated laps difference between fuel and virtual energy.

Positive value indicates more laps can be run on fuel than virtual energy; in other words, virtual energy will deplete sooner than fuel. For example, a value of `+1.5` indicates that there will be `1.5 laps` of extra fuel remaining after virtual energy depleted.

Note, depleting virtual energy could result a `Stop-Go` penalty in `LMU`; while running out of fuel means no power for vehicle and would result retirement from race. So it is a good idea to keep fuel bias close to `0.0`, and slightly towards positive side to avoid depleting fuel before virtual energy.

[**`Back to Top`**](#)


## Weather
**This widget displays weather info.**

    show_temperature
Show track and ambient temperature.

    show_rain
Show rain precipitation in percentage.

    show_wetness
Show average surface wetness in percentage.

    temperature_trend_interval, raininess_trend_interval, wetness_trend_interval
Set weather change trend interval in seconds for temperature, raininess, surface wetness readings. Default interval is `60` seconds.

If weather readings increased within the interval, `▲` uparrow sign will be shown; if readings decreased within the interval, `▼` downarrow sign will be shown; If readings has not changed during the interval, `●` sign will be shown after.

    decimal_places_temperature
Set amount decimal places to keep. Default is `1` decimal place, set to `0` to hide decimals. Note, when number of digits is less than expected, extra leading zero or decimal place will be added to fill the gap.

[**`Back to Top`**](#)


## Weather forecast
**This widget displays weather forecast info.**

    layout
2 layouts are available: `0` = show columns from left to right, `1` = show columns from right to left. Note, the `now` column always shows current weather condition.

    show_estimated_time
Show estimated time reading for upcoming weather. Note, estimated time reading only works in time-based race. Other race type such as lap-based race shows `n/a` instead.

    show_ambient_temperature
Show estimated ambient temperature reading for upcoming weather. Note, the `now` column always shows current ambient temperature instead.

    show_rain_chance_bar
Show visualized rain chance bar reading for upcoming weather. Note, the `now` column always shows current raininess instead.

    number_of_forecasts
Set number of forecasts to display. Value range in `1` to `4`. Default is `4` forecasts.

    show_unavailable_data
Show columns with unavailable weather data. Set `False` to auto hide columns with unavailable data. Note, auto hide only works for time-based race.

[**`Back to Top`**](#)


## Wheel alignment
**This widget displays camber and toe-in info.**

    show_camber
Show camber in degree.

    show_toe_in
Show toe-in in degree.

[**`Back to Top`**](#)
