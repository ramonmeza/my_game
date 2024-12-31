"""
The classic card game Blackjack, implemented in Python. 
Copyright (C) 2024  Ramon Meza

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from enum import StrEnum


class GameStates(StrEnum):
    """Contains ID's used to manage state of the game.
    """
    MAIN_MENU: str = "main_menu"
    OPTIONS_MENU: str = "options_menu"
    GAMEPLAY: str = "gameplay"
    PAUSE_MENU: str = "pause_menu"