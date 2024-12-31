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

from . import __window_caption__
from .font_manager import FontManager
from .state_manager import StateManager

from .events import (
    MAIN_MENU_PLAY,
    MAIN_MENU_OPTIONS,
    OPTIONS_MENU_TOGGLE_FULLSCREEN,
    OPTIONS_MENU_GO_BACK,
)
from .ui.menus import MainMenu, OptionsMenu


class Game:
    """Represents the game. Initializes the main window and controls the main
    game loop.
    """

    is_running: bool
    clock: pygame.time.Clock
    window: pygame.Surface
    font_manager: FontManager
    state_manager: StateManager

    def init(self) -> None:
        """Initialize the main systems."""
        pygame.init()
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption(__window_caption__)
        self.font_manager = FontManager()
        self.state_manager = StateManager()
        self.init_game()

    def init_game(self) -> None:
        """Construct and load the actual game."""
        # load fonts
        self.font_manager.add("data/fonts/Rijusans-Regular.ttf")

        # load menus
        self.state_manager.add("main_menu", MainMenu(font=self.font_manager.get()))
        self.state_manager.add(
            "options_menu", OptionsMenu(font=self.font_manager.get())
        )

    def run(self) -> None:
        """Run the game."""
        self.is_running = True
        while self.is_running:
            delta_time: float = self.clock.tick()
            self.handle_events()
            self.update(delta_time)
            self.render()

    def handle_user_event(self, event: pygame.event.Event) -> None:
        """Handles custom events. Used to manage game state.

        Args:
            event (pygame.event.Event): The custom event.
        """
        if event.type == MAIN_MENU_PLAY:
            print("play")

        elif event.type == MAIN_MENU_OPTIONS:
            print("goto options")
            self.state_manager.change_state("options_menu")

        elif event.type == OPTIONS_MENU_TOGGLE_FULLSCREEN:
            print("toggle fullscreen")
            pygame.display.toggle_fullscreen()

        elif event.type == OPTIONS_MENU_GO_BACK:
            print("go back")
            self.state_manager.go_back()

    def handle_events(self) -> None:
        """Handle system and game events."""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_running = False

                case _ if event.type >= pygame.USEREVENT:
                    self.handle_user_event(event)

                case _:
                    pass

    def update(self, delta_time: float) -> None:
        """Update the game.

        Args:
            delta_time (float): Delta between frames, in milliseconds.
        """
        pygame.display.set_caption(
            f"{__window_caption__} FPS: {self.clock.get_fps():.0f}"
        )
        self.state_manager.update(delta_time=delta_time)

    def render(self) -> None:
        """Render the game."""
        self.window.fill("#000000")
        self.state_manager.draw(surface=self.window)
        pygame.display.flip()

    def deinit(self) -> None:
        """Safely close the main systems."""
        pygame.quit()
