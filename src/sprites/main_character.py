import pygame


class MainCharacter(pygame.sprite.Sprite):

    ANIMATION_COOLDOWN: int = 50

    def __init__(self, animations: dict[str, list[pygame.surface.Surface]]) -> None:
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
    def move(self, direction: str, velocity: int = None) -> None:
        speed = velocity or self.velocity
        self.is_moving = True
        self.direction = direction
        match self.direction:
            case "up":
                self.rect.y -= speed
            case "down":
                self.rect.y += speed
            case "left":
                self.rect.x -= speed
            case "right":
                self.rect.x += speed
            case _:
                ...
        self.animate()
