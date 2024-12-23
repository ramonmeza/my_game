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

import logging
import os

import pygame

from .scene_manager import SceneManager, Scene, State
from .spritesheet import Spritesheet


class Game:
    """
    Composes the game using defined objects and manages their states and interactions.
    """
    scene_manager: SceneManager
    screen: pygame.Surface

    def run(self) -> None:
        """Run the game.
        """
        deck: Spritesheet = Spritesheet("data/sprites/playingCardBacks.xml")
        card = deck.get("cardBack_red3")

        self.screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        delta_time: int = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            delta_time: float = clock.tick(60) / 1000.0
            self.update(delta_time)
            self.render()

    def init(self) -> None:
        """Initialize the game.
        """
        logging.info("Starting initialization...")
        pygame.init()
        self.display_splash_screen()
        self.load()
        logging.info("Initialization complete!")

    def display_splash_screen(self) -> None:
        """Displays the splashscreen for the game.
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        background = pygame.image.load("data/img/splashscreen.png")
        screen = pygame.display.set_mode(background.get_size(), pygame.NOFRAME)
        screen.blit(background.convert(), (0,0))
        pygame.display.update()

        # artifical stall for splashscreen display
        import time  # pylint: disable=import-outside-toplevel
        time.sleep(1)

    def load(self) -> None:
        """Loads data for the game
        """
        self.scene_manager = SceneManager()
        self.scene_manager.add(Scene(
            pygame.image.load("data/img/pygame.png"),
            on_update=intro_slide_update
        ))
        self.scene_manager.add(Scene(
            pygame.image.load("data/img/kenney.png"),
            on_update=intro_slide_update,
        ))

    def update(self, delta_time: float) -> None:
        """Updates the game."""
        self.scene_manager.update(delta_time)

    def render(self) -> None:
        """Renders the game."""
        # green: #35654d
        self.screen.fill("#000000")
        self.scene_manager.draw(self.screen)
        pygame.display.flip()

    def shutdown(self) -> None:
        """Safely shutdown the game.
        """
        logging.info("Starting shutdown...")
        pygame.quit()
        logging.info("Shutdown complete!")


def intro_slide_update(scene: Scene, delta_time: float) -> None:
    if hasattr(scene, "intro_counter"):
        scene.intro_counter -= delta_time
        if scene.intro_counter <= 0.0:
            scene.state = State.FADE_OUT
            delattr(scene, "intro_counter")
    else:
        scene.intro_counter = 3.0


Blackjack: Game = Game()
