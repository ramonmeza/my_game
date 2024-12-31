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

import pygame

from .events import GAMEPLAY_PAUSE


class Gameplay(pygame.sprite.Group):
    """Contains all gameplay related functionality."""

    is_paused: bool

    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.is_paused = False

    def update(self, *args, **kwargs) -> None:
        """Update gameplay."""
        super().update(*args, **kwargs)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(GAMEPLAY_PAUSE))
