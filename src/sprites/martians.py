import pygame


class Martian(pygame.sprite.Sprite):

    ANIMATION_COOLDOWN: int = 50

    def __init__(
        self, animations: dict[str, list[pygame.surface.Surface]], size: tuple[int, int], surface: pygame.surface.Surface
    ) -> None:
        self.world = surface
        self.screen = size
        self.animations = animations
        self.target_x, self.target_y = self.screen[0] // 2, self.screen[1] // 2
        self.health = 100
        self.image = self.animations["up"][0]
        self.rect = self.image.get_rect()
        self.direction = "up"
        super().__init__()
