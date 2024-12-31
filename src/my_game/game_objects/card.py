from enum import IntEnum

import pygame

from .game_object import GameObject


class CardState(IntEnum):
    FACE_UP = 0
    FACE_DOWN = 1
    FLIPPING = 2


class Card(GameObject):

    anim_state: CardState
    state: CardState
    face_texture: pygame.Surface
    back_texture: pygame.Surface
    anim_state: CardState
    anim_counter: float

    def __init__(
        self,
        face_texture: pygame.Surface,
        back_texture: pygame.Surface,
        initial_state: CardState = CardState.FACE_DOWN,
    ) -> None:
        super().__init__()
        self.state = initial_state
        self.face_texture = face_texture
        self.back_texture = back_texture
        self.rect = self.face_texture.get_rect()
        self.anim_counter = 0.0
        self.anim_state = initial_state

    @property
    def image(self) -> pygame.Surface:
        match self.anim_state:
            case CardState.FACE_UP:
                return self.face_texture
            case CardState.FACE_DOWN:
                return self.back_texture
            case _:
                raise RuntimeError

    def update(self, delta_time: float) -> None:
        _ = delta_time

        # if space pressed and not spinning
        if (
            pygame.key.get_pressed()[pygame.K_SPACE]
            and self.state != CardState.FLIPPING
        ):
            # reset anim
            self.anim_counter = 0.0

            # determine next state
            match self.state:
                case CardState.FACE_UP:
                    self.anim_state = CardState.FACE_DOWN
                case CardState.FACE_DOWN:
                    self.anim_state = CardState.FACE_UP
                case _:
                    pass
            self.state = CardState.FLIPPING

        if self.state == CardState.FLIPPING:
            self.anim_counter += delta_time

            if self.anim_counter >= 1.0:
                self.anim_counter = 1.0

                # switch anim stat
                self.state = self.anim_state
