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
import pygame

from .spritesheet import Spritesheet


class Game:
    """
    Composes the game using defined objects and manages their states and interactions.
    """

    def run(self) -> None:
        """Run the game.
        """
        deck: Spritesheet = Spritesheet("data/sprites/playingCardBacks.xml")
        card = deck.get("cardBack_red3")

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("#35654d")

            # RENDER YOUR GAME HERE
            screen.blit(card, (0, 0))

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

    def init(self) -> None:
        """Initialize the game.
        """
        logging.info("Starting initialization...")
        pygame.init()
        logging.info("Initialization complete!")

    def shutdown(self) -> None:
        """Safely shutdown the game.
        """
        logging.info("Starting shutdown...")
        pygame.quit()
        logging.info("Shutdown complete!")


Blackjack: Game = Game()
