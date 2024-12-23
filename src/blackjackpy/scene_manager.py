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

from enum import IntEnum
from typing import Callable

import pygame


class State(IntEnum):
    """State used within StateMachine implementation
    """

    NOT_STARTED = -1
    FADE_IN = 0
    ACTIVE = 1
    PAUSED = 2
    FADE_OUT = 3
    DONE = 4


OnUpdateFunc = Callable[['Scene', float], None]


class Scene(pygame.sprite.Sprite):
    """A scene which manages state and transitions.
    """

    image: pygame.Surface
    rect: pygame.Rect
    transition_counter: float
    state: State
    on_update: OnUpdateFunc
    on_pause_update: OnUpdateFunc

    def __init__(self, surface: pygame.Surface, on_update: OnUpdateFunc, 
                 on_pause_update: OnUpdateFunc | None = None) -> None:
        """Initialize a Scene instance.

        Args:
            surface (pygame.Surface): Surface for the scene.
            on_update (OnUpdateFunc): Function to be called during updates.
            on_pause_update (OnUpdateFunc | None, optional): Function to be 
            called during paused updates. Defaults to None.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.rect = surface.get_rect()

        self.image.set_alpha(0)
        self.image.convert_alpha()

        self.transition_counter = 0.0
        self.transition_value = 0.0
        self.transition_length = 1.0
        self.state = State.NOT_STARTED
        self.on_update = on_update
        self.on_pause_update = on_pause_update

    def update(self, delta_time: float) -> None:
        """Controls updating scene and scene transitions.

        Args:
            delta_time (float): Time since last frame
        """
        alpha = int(self.transition_counter * 255)
        self.image.set_alpha(alpha)
        self.image.convert_alpha()

        match self.state:
            case State.NOT_STARTED:
                self.state = State.FADE_IN
                self.transition_counter = 0.0
                self.transition_value = 0.0

            case State.FADE_IN:
                self.transition_counter += delta_time
                self.transition_value = min(1.0, self.transition_counter / self.transition_length)
                if self.transition_counter >= self.transition_length:
                    self.state = State.ACTIVE

            case State.ACTIVE:
                self.on_update(self, delta_time)

            case State.PAUSED:
                if self.on_pause_update:
                    self.on_pause_update(self, delta_time)
                else:
                    # default pause functionality?
                    # just dont allow pause?
                    self.state = State.ACTIVE

            case State.FADE_OUT:
                self.transition_counter -= delta_time
                self.transition_value = max(0.0, self.transition_counter / self.transition_length)
                if self.transition_counter <= 0.0:
                    self.state = State.DONE

            case State.DONE:
                pass
            case _:
                pass

class SceneManager(pygame.sprite.Group):
    """Manages scenes' states and displays them in FIFO order. When a scene's 
    state changes to DONE, the scene is removed from the manager.
    """

    background: pygame.Surface

    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.background = pygame.Surface((256, 256))
        self.background.fill("pink")

    def update(self, delta_time: float):
        """Update the active state, given in FIFO order.

        Args:
            delta_time (float): Time between frames.
        """
        scenes = self.sprites()
        if scenes:
            scene: pygame.sprite.Sprite = scenes[0]
            if hasattr(scene, "state"):
                if scene.state == State.DONE:
                    self.remove(scene)
                else:
                    scene.update(delta_time)

    def draw(self, surface: pygame.Surface, 
             bgsurf: pygame.Surface | None = None,  # pylint: disable=unused-argument
             special_flags: int = 0) -> list:
        """Draw the scene that was added first (FIFO ordering).

        Args:
            surface (pygame.Surface): Surface to draw the scene to.
            bgsurf (pygame.Surface, optional): Used by some internal pygame 
            function. Defaults to None.
            special_flags (int, optional): Special flags. Defaults to 0.

        Returns:
            list: _description_
        """
        sprites = self.sprites()
        if sprites:
            sprite: pygame.sprite.Sprite = sprites[0]

            self.spritedict[sprite] = surface.blit(
                sprite.image,
                sprite.rect,
                None,
                special_flags
            )

            self.lostsprites = []
            dirty = self.lostsprites

            return dirty
        else:
            surface.fill("fuchsia")
            return []
