import pygame

from .events import (
    GAMEPLAY_PAUSE
)


class Gameplay(pygame.sprite.Group):
    is_paused: bool

    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.is_paused = False

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(GAMEPLAY_PAUSE))
