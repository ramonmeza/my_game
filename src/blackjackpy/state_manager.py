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


class StateManager:
    """Manages states and transitioning between them. Provides an interface to
    receive the current and previous states.
    """

    current_state: str
    previous_state: str
    states: Dict[str, pygame.sprite.Group]

    def __init__(self) -> None:
        self.current_state = ""
        self.previous_state = ""
        self.states = {}

    def add(self, key: str, state: pygame.sprite.Group) -> None:
        """Add a state to the state machine.

        Args:
            key (str): String name ID for the state.
            state (pygame.sprite.Group): The actual state object. Drawn when
            it's the current state.
        """
        self.previous_state = self.current_state

        if not self.current_state:
            self.current_state = key

        self.states[key] = state

    def change_state(self, next_state_key: str) -> None:
        """Change the state to the given state with matching `next_state_key`.

        Args:
            next_state_key (str): String name ID for the state.
        """
        if not self.current_state:
            return
        self.previous_state = self.current_state
        self.current_state = next_state_key

    def go_back(self) -> None:
        """Transition to the previous state."""
        if self.previous_state:
            self.change_state(self.previous_state)

    def update(self, *args, **kwargs) -> None:
        """Update the current state."""
        if self.states:
            self.states[self.current_state].update(*args, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        """Draw the current state."""
        self.states[self.current_state].draw(*args, **kwargs)
