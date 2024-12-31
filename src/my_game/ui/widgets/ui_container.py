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


class UIContainer(pygame.sprite.Group):
    """A container for UI widgets which automatically centers them and provides
    Y-padding to items.
    """

    def __init__(self, *widgets, y_padding: int = 10):
        super().__init__(*widgets)
        self._position_items(y_padding=y_padding)

    def _position_items(self, y_padding: int) -> None:
        size = pygame.display.get_window_size()
        center = (size[0] / 2, size[1] / 2)

        sprites = self.sprites()
        y_height = sum(item.size[1] for item in sprites) + (
            max(0, (len(sprites) - 1)) * y_padding
        )

        for i, item in enumerate(sprites):
            x_offset = item.size[0] / 2
            y_offset = i * (item.size[1] + y_padding) - (y_height / 2)
            item.position = (center[0] - x_offset, center[1] + y_offset)
