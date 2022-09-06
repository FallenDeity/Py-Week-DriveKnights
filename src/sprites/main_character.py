import pygame
from typing import Callable, Union
from functools import wraps
from .worldmap import MapGenerator


class MainCharacter(pygame.sprite.Sprite):

    ANIMATION_COOLDOWN: int = 50

    @staticmethod
    def wrapper(func: Callable[..., None]) -> Callable[..., None]:
        @wraps(func)
        def inner(cls: "MainCharacter", *args: Union[str, int], **kwargs: Union[str, int]) -> None:
            func(cls, *args, **kwargs)
            cls.animate()

        return inner

    def __init__(self, animations: dict[str, list[pygame.surface.Surface]], size: tuple[int, int], world: MapGenerator) -> None:
        super().__init__()
        self.world = world
        self.screen = size
        self.animations = animations
        self.image = self.animations["up"][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.screen[0] // 2
        self.rect.y = self.screen[1] // 2
        self.world.pos_x = self.rect.x
        self.world.pos_y = self.rect.y
        self.velocity = 4
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
                if self.world.pos_y - speed > 0:
                    self.world.pos_y -= speed
            case "down":
                if self.world.pos_y + speed < self.world.size[1] - self.rect.height:
                    self.world.pos_y += speed
            case "left":
                if self.world.pos_x - speed > 0:
                    self.world.pos_x -= speed
            case "right":
                if self.world.pos_x + speed < self.world.size[0] - self.rect.width:
                    self.world.pos_x += speed
            case _:
                ...
        self.is_moving = False
