"""
My journey toward learning game development using Python. 
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

import pygame


MAIN_MENU_PLAY: int = pygame.event.custom_type()
MAIN_MENU_OPTIONS: int = pygame.event.custom_type()

OPTIONS_MENU_TOGGLE_FULLSCREEN: int = pygame.event.custom_type()
OPTIONS_MENU_GO_BACK: int = pygame.event.custom_type()

GAMEPLAY_PAUSE: int = pygame.event.custom_type()

PAUSE_MENU_RESUME: int = pygame.event.custom_type()
PAUSE_MENU_GOTO_MAIN_MENU: int = pygame.event.custom_type()
