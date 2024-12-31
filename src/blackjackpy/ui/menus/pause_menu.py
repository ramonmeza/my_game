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

from ..widgets.ui_button import UIButton, UIButtonStyle
from ..widgets.ui_container import UIContainer
from ...events import (
    PAUSE_MENU_RESUME,
    PAUSE_MENU_GOTO_MAIN_MENU,
)


class PauseMenu(UIContainer):
    """Implementation of the main menu. Declares the actual UI and provides
    hooks to UI widgets.
    """

    def __init__(self, font: pygame.font.Font):
        super().__init__(
            [
                UIButton(
                    "Resume",
                    style=UIButtonStyle(
                        font=font,
                        font_color="#ffffff",
                        bg_color="#188d46",
                        hover_color="#66B083",
                        press_color="#465f50",
                        padding=(40, 20),
                    ),
                    on_pressed_callback=self.on_resume_pressed,
                ),
                UIButton(
                    "Quit",
                    style=UIButtonStyle(
                        font=font,
                        font_color="#ffffff",
                        bg_color="#188d46",
                        hover_color="#66B083",
                        press_color="#465f50",
                        padding=(40, 20),
                    ),
                    on_pressed_callback=self.on_quit_pressed,
                ),
            ]
        )

    def on_resume_pressed(self) -> None:
        """Adds `PAUSE_MENU_RESUME` event to the pygame event queue."""
        pygame.event.post(pygame.event.Event(PAUSE_MENU_RESUME))

    def on_quit_pressed(self) -> None:
        """Adds `PAUSE_MENU_GOTO_MAIN_MENU` event to the pygame event queue."""
        pygame.event.post(pygame.event.Event(PAUSE_MENU_GOTO_MAIN_MENU))
