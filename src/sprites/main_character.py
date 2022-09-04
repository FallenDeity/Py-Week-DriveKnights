import pygame
from typing import Callable, Union
from functools import wraps


class MainCharacter(pygame.sprite.Sprite):

    ANIMATION_COOLDOWN: int = 50

    @staticmethod
    def wrapper(func: Callable[..., None]) -> Callable[..., None]:
        @wraps(func)
        def inner(cls: "MainCharacter", *args: Union[str, int], **kwargs: Union[str, int]) -> None:
            func(cls, *args, **kwargs)
            cls.animate()

        return inner

    def __init__(self, animations: dict[str, list[pygame.surface.Surface]], size: tuple[int, int]) -> None:
        super().__init__()
        self.animations = animations
        self.image = self.animations["up"][0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velocity = 3
        self.direction = "up"
        self.is_moving = False
        self.is_jumping = False
        self.is_falling = False
        self.jump_velocity = 10
        self.jump_time = 1
        self.gravity = 0.5
        self.max_fall_velocity = 10
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.flip = False
        self.screen = size

    # Animate the character
    def animate(self) -> None:
        # Update the animation
        now = pygame.time.get_ticks()
        if now - self.update_time > self.ANIMATION_COOLDOWN:
            self.update_time = now
            self.frame_index += 1
        # Check if the animation has run out of frames
        if self.frame_index >= len(self.animations[self.direction]):
            self.frame_index = 0
        # Update the image
        self.image = self.animations[self.direction][self.frame_index]

    # Move the character
    @wrapper
    def animate_move(self, direction: str, velocity: int = None) -> None:
        speed = velocity or self.velocity
        self.direction = direction
        self.is_moving = True
        match self.direction:
            case "up":
                if self.rect.y - speed > 0:
                    self.rect.y -= speed
            case "down":
                if self.rect.y + speed < self.screen[1] - self.rect.height:
                    self.rect.y += speed
            case "left":
                if self.rect.x - speed > 0:
                    self.rect.x -= speed
            case "right":
                if self.rect.x + speed < self.screen[0] - self.rect.width:
                    self.rect.x += speed
            case _:
                ...
        self.is_moving = False
