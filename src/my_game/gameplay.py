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

from typing import Tuple
from .events import GAMEPLAY_PAUSE


class GameObject(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, sprite: pygame.Surface):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()

    @property
    def position(self) -> Tuple[int, int]:
        return (self.rect.x, self.rect.y)

    @position.setter
    def position(self, value: Tuple[int, int]) -> None:
        self.rect = pygame.Rect(value, self.rect.size)


class Ball(GameObject):
    speed: float
    velocity: Tuple[float, float]

    def __init__(self):
        surf = pygame.Surface((10, 10))
        pygame.draw.circle(surf, "red", (5, 5), 5)
        super().__init__(surf)

        self.speed = 1000
        self.velocity = (self.speed, self.speed)

    def update(self, delta_time: float) -> None:
        self.position = (self.position[0] + (self.velocity[0] * delta_time),
                        (self.position[1] + (self.velocity[1] * delta_time)))
        
        bounds = pygame.display.get_window_size()

        if self.position[0] < 0:
            self.velocity = (-self.velocity[0], self.velocity[1])
            print("bounce off left wall")
            
        if self.position[0] > bounds[0]:
            self.velocity = (-self.velocity[0], self.velocity[1])
            print("bounce off right wall")

        if self.position[1] < 0:
            self.velocity = (self.velocity[0], -self.velocity[1])
            print("bounce off top wall")
            
        if self.position[1] > bounds[1]:
            self.velocity = (self.velocity[0], -self.velocity[1])
            print("bounce off bottom wall")


class Gameplay(pygame.sprite.Group):
    """Contains all gameplay related functionality."""

    is_paused: bool

    def __init__(self):
        super().__init__([
            Ball()
        ])
        self.is_paused = False

    def update(self, *args, **kwargs) -> None:
        """Update gameplay."""
        super().update(*args, **kwargs)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(GAMEPLAY_PAUSE))
