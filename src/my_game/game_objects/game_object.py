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

from typing import Tuple

import pygame


class GameObject(pygame.sprite.Sprite):
    """Base class for visible game objects."""

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, sprite: pygame.Surface):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()

    @property
    def position(self) -> Tuple[int, int]:
        """Get the GameObject's position."""
        return (self.rect.x, self.rect.y)

    @position.setter
    def position(self, value: Tuple[int, int]) -> None:
        """Set the GameObject's position.

        Args:
            value (Tuple[int, int]): New position.
        """
        self.rect = pygame.Rect(value, self.rect.size)
