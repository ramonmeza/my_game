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

from . import __window_caption__
from .managers import (
    AssetManager,
    FontManager,
    StateManager,
)

from .events import (
    GAMEPLAY_PAUSE,
    MAIN_MENU_OPTIONS,
    MAIN_MENU_PLAY,
    OPTIONS_MENU_GO_BACK,
    OPTIONS_MENU_TOGGLE_FULLSCREEN,
    PAUSE_MENU_RESUME,
    PAUSE_MENU_GOTO_MAIN_MENU,
)
from .gameplay import Gameplay
from .game_states import GameStates
from .ui.menus import MainMenu, OptionsMenu, PauseMenu


MAX_FPS: int = 250
MAX_FPS_IN_MENU: int = 60


class Game:
    """Represents the game. Initializes the main window and controls the main
    game loop.
    """

    is_running: bool
    clock: pygame.time.Clock
    window: pygame.Surface
    asset_manager: AssetManager
    font_manager: FontManager
    state_manager: StateManager
    max_fps: int

    def init(self) -> None:
        """Initialize the main systems."""
        pygame.init()
        self.is_running = False

        # initialize window
        self.max_fps = MAX_FPS_IN_MENU
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(__window_caption__)

        # initialize managers
        self.asset_manager = AssetManager()
        self.font_manager = FontManager()
        self.state_manager = StateManager()

        # intialize game components
        self.init_game()

    def init_game(self) -> None:
        """Construct and load the actual game."""
        # load fonts
        self.font_manager.add("data/fonts/Rijusans-Regular.ttf")

        # load assets
        self.asset_manager.load_spritesheet("data/spritesheets/playingCards.xml")
        self.asset_manager.load_spritesheet("data/spritesheets/playingCardBacks.xml")

        # add states to state machine
        self.state_manager.add(
            GameStates.MAIN_MENU, MainMenu(font=self.font_manager.get())
        )
        self.state_manager.add(
            GameStates.OPTIONS_MENU, OptionsMenu(font=self.font_manager.get())
        )
        self.state_manager.add(GameStates.GAMEPLAY, Gameplay(self.asset_manager))
        self.state_manager.add(
            GameStates.PAUSE_MENU, PauseMenu(font=self.font_manager.get())
        )

    def run(self) -> None:
        """Run the game."""
        self.is_running = True
        while self.is_running:
            delta_time: float = self.clock.tick_busy_loop(self.max_fps) / 1000.0
            self.handle_events()
            self.update(delta_time)
            self.render()

    def handle_user_event(self, event: pygame.event.Event) -> None:
        """Handles custom events. Used to manage game state.

        Args:
            event (pygame.event.Event): The custom event.
        """
        if event.type == MAIN_MENU_PLAY:
            self.max_fps = MAX_FPS
            self.state_manager.change_state(GameStates.GAMEPLAY)

        elif event.type == MAIN_MENU_OPTIONS:
            self.state_manager.change_state(GameStates.OPTIONS_MENU)
            self.max_fps = MAX_FPS_IN_MENU

        elif event.type == OPTIONS_MENU_TOGGLE_FULLSCREEN:
            self.max_fps = MAX_FPS_IN_MENU
            pygame.display.toggle_fullscreen()

        elif event.type == OPTIONS_MENU_GO_BACK:
            self.max_fps = MAX_FPS_IN_MENU
            self.state_manager.go_back()

        elif event.type == GAMEPLAY_PAUSE:
            self.max_fps = MAX_FPS_IN_MENU
            self.state_manager.change_state(GameStates.PAUSE_MENU)

        elif event.type == PAUSE_MENU_RESUME:
            self.max_fps = MAX_FPS
            self.state_manager.change_state(GameStates.GAMEPLAY)

        elif event.type == PAUSE_MENU_GOTO_MAIN_MENU:
            self.max_fps = MAX_FPS_IN_MENU
            self.state_manager.change_state(GameStates.MAIN_MENU)

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
