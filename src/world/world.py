import pygame
import sys
from src.setup import Setup


class World:

    @staticmethod
    def get_screen_res() -> tuple[int, int]:
        """Function to get the user's screen resolution"""
        display_info = pygame.display.Info()
        return display_info.current_w, display_info.current_h

    def __init__(self) -> None:
        pygame.init()
        self.screen = self.get_screen_res()
        self.surface = pygame.display.set_mode((*self.screen,))
        pygame.display.set_caption("DriveKnights")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.setup = Setup()

    def continue_running(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.setup.mc.move("up", 5)
        elif keys[pygame.K_DOWN]:
            self.setup.mc.move("down", 5)
        elif keys[pygame.K_LEFT]:
            self.setup.mc.move("left", 5)
        elif keys[pygame.K_RIGHT]:
            self.setup.mc.move("right", 5)

    def events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                            pygame.quit()
                            sys.exit()
                        case pygame.K_UP:
                            self.setup.mc.move("up")
                        case pygame.K_DOWN:
                            self.setup.mc.move("down")
                        case pygame.K_LEFT:
                            self.setup.mc.move("left")
                        case pygame.K_RIGHT:
                            self.setup.mc.move("right")
                        case _:
                            ...
                case _:
                    ...
        self.continue_running()

    def update(self) -> None:
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.setup.mc.image, self.setup.mc.rect)
        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
