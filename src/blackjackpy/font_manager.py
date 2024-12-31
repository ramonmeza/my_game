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

from typing import Dict

import pygame


class FontManager:
    """Manages loaded fonts."""

    fonts: Dict[str, pygame.font.Font]

    def __init__(self) -> None:
        if not pygame.font.get_init():
            pygame.font.init()

        self.fonts = {}

    def add(self, path: str, name: str = "default", size: int = 12) -> None:
        """Add a font to the manager.

        Args:
            path (str): Path to the font file (.ttf, .otf)
            name (str, optional): String name ID of the font. Defaults to "default".
            size (int, optional): Size for the font. Defaults to 12.
        """
        self.fonts[name] = pygame.font.Font(path, size)

    def get(self, name: str = "default") -> pygame.font.Font:
        """Get a loaded font.

        Args:
            name (str, optional): String name ID of the font. Defaults to "default".

        Returns:
            pygame.font.Font | None: The requested font. If not font is loaded, None is returned.
        """
        if name not in self.fonts:
            return None
        return self.fonts[name]
