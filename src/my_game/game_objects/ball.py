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

from .game_object import GameObject


class Ball(GameObject):
    """A bouncing ball."""

    speed: float
    velocity: Tuple[float, float]

    def __init__(self):
        size = (24, 24)
        half_size = (12, 12)
        surf = pygame.Surface(size)
        pygame.draw.circle(surf, "red", half_size, half_size[0])
        super().__init__(surf)

        self.speed = 400
        self.velocity = (self.speed, self.speed)

    def update(self, delta_time: int) -> None:
        """Moves ball and bounces ball as needed."""
        print(delta_time)
        self.position = (
            self.position[0] + self.velocity[0] * delta_time,
            self.position[1] + self.velocity[1] * delta_time,
        )

        bounds = pygame.display.get_window_size()

        if self.position[0] < 0:
            self.velocity = (-self.velocity[0], self.velocity[1])
            self.position = (self.position[0] + 1, self.position[1])

        if self.position[0] > bounds[0]:
            self.velocity = (-self.velocity[0], self.velocity[1])
            self.position = (self.position[0] - 1, self.position[1])

        if self.position[1] < 0:
            self.velocity = (self.velocity[0], -self.velocity[1])
            self.position = (self.position[0], self.position[1] + 1)

        if self.position[1] > bounds[1]:
            self.velocity = (self.velocity[0], -self.velocity[1])
            self.position = (self.position[0], self.position[1] - 1)
