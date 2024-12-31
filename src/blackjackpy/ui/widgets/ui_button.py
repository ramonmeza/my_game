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

from dataclasses import dataclass
from enum import IntEnum
from typing import Callable, Tuple

import pygame


@dataclass
class UIButtonStyle:
    """Data structure for holding properties related to button styling."""

    font: pygame.font.Font
    font_color: pygame.Color
    bg_color: pygame.Color
    hover_color: pygame.Color
    press_color: pygame.Color
    padding: Tuple[int, int]


class UIButtonState(IntEnum):
    """Different states a UI widget can be in."""

    DEFAULT = 0
    HOVERED = 1
    PRESSED = 2


OnPressedCallbackFn = Callable[
    [
        None,
    ],
    None,
]


class UIButton(pygame.sprite.Sprite):  # pylint: disable=R0902
    """A button with text. Provides a callback for `on_pressed` events."""

    CLICK_DELAY: int = 20

    state: UIButtonState
    image: pygame.Surface
    rect: pygame.Rect
    text: str
    stlye: UIButtonStyle
    button_surface: pygame.Surface
    text_surface: pygame.Surface
    on_pressed_callback: OnPressedCallbackFn | None
    was_pressed: bool

    def __init__(
        self,
        text: str,
        style: UIButtonStyle,
        on_pressed_callback: OnPressedCallbackFn | None = None,
    ):
        super().__init__()
        self.state = UIButtonState.DEFAULT
        self.was_pressed = False
        self.on_pressed_callback = on_pressed_callback
        self.style = style
        self.text = text
        self.text_surface = style.font.render(text, 0, style.font_color)

        text_size = self.text_surface.get_size()
        button_size = (
            text_size[0] + (2 * style.padding[0]),
            text_size[1] + (2 * style.padding[1]),
        )
        self.button_surface = pygame.Surface(button_size)
        self.button_surface.fill(style.bg_color)

        text_offset = (
            (button_size[0] - text_size[0]) / 2,
            (button_size[1] - text_size[1]) / 2,
        )

        self.image = pygame.Surface(button_size)
        self.image.blits(
            [
                (self.button_surface, (0, 0)),
                (self.text_surface, text_offset),
            ]
        )
        self.rect = self.image.get_rect()

    @property
    def position(self) -> Tuple[int, int]:
        """Get the position of this UIButton.

        Returns:
            Tuple[int, int]: The position as a tuple.
        """
        return (self.rect.x, self.rect.y)

    @position.setter
    def position(self, position: Tuple[int, int]) -> None:
        """Update the position of this UIButton.

        Args:
            position (Tuple[int, int]): New position to set to.
        """
        self.rect = pygame.Rect(position, self.rect.size)

    @property
    def size(self) -> Tuple[int, int]:
        """Get the size of this UIButton.

        Returns:
            Tuple[int, int]: The size as a tuple.
        """
        return self.rect.size

    @size.setter
    def size(self, size: Tuple[int, int]) -> None:
        """Update the size of this UIButton.

        Args:
            size (Tuple[int, int]): New size to set to.
        """
        self.rect.size = size

    def is_hovered(self) -> bool:
        """Returns whether this element is being hovered over by the user's mouse.

        Returns:
            bool: Whether the element is being hovered over.
        """
        mouse_pos = pygame.mouse.get_pos()
        return (
            self.rect.left <= mouse_pos[0] <= self.rect.right
            and self.rect.top <= mouse_pos[1] <= self.rect.bottom
        )

    def _set_state(self, state: UIButtonState) -> None:
        """Set the state of the button. Used internally.

        Args:
            state (UIButtonState): Next state.
        """
        self.state = state
        match self.state:
            case UIButtonState.DEFAULT:
                self.button_surface.fill(self.style.bg_color)

            case UIButtonState.HOVERED:
                self.button_surface.fill(self.style.hover_color)

            case UIButtonState.PRESSED:
                self.button_surface.fill(self.style.press_color)

            case _:
                pass

        text_size = self.text_surface.get_size()
        button_size = (
            text_size[0] + (2 * self.style.padding[0]),
            text_size[1] + (2 * self.style.padding[1]),
        )
        text_offset = (
            (button_size[0] - text_size[0]) / 2,
            (button_size[1] - text_size[1]) / 2,
        )
        self.image.blits(
            [
                (self.button_surface, (0, 0)),
                (self.text_surface, text_offset),
            ]
        )

    def update(self) -> None:
        """Updates the state of the UIButton."""
        is_mouse_pressed: bool = pygame.mouse.get_pressed()[0] is True

        # ignore input if not hovered
        hovered = self.is_hovered()
        if hovered:
            if (
                not self.was_pressed
                and self.state != UIButtonState.PRESSED
                and is_mouse_pressed
            ):
                self._set_state(UIButtonState.PRESSED)

            elif self.state == UIButtonState.PRESSED and not is_mouse_pressed:
                if self.on_pressed_callback:
                    self.on_pressed_callback()
                pygame.time.wait(UIButton.CLICK_DELAY)
                self._set_state(UIButtonState.HOVERED)

            elif self.state != UIButtonState.HOVERED and not is_mouse_pressed:
                self._set_state(UIButtonState.HOVERED)

        elif self.state != UIButtonState.DEFAULT:
            self._set_state(UIButtonState.DEFAULT)

        self.was_pressed = is_mouse_pressed
