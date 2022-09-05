import pygame
import sys
from src.sprites import MapGenerator
from src.setup import Setup


class World:

    map: MapGenerator

    @staticmethod
    def get_screen_res() -> tuple[int, int]:
        """Function to get the user's screen resolution"""
        display_info = pygame.display.Info()
        return display_info.current_w, display_info.current_h

    def __init__(self) -> None:
        pygame.init()
        self.screen = 1024, 768
        self.surface = pygame.display.set_mode((*self.screen,))
        pygame.display.set_caption("DriveKnights")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.setup = Setup(self.screen)
        self.map = MapGenerator(self.surface, self.screen)

    def continue_running(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.setup.mc.animate_move("up", 5)
        elif keys[pygame.K_DOWN]:
            self.setup.mc.animate_move("down", 5)
        elif keys[pygame.K_LEFT]:
            self.setup.mc.animate_move("left", 5)
        elif keys[pygame.K_RIGHT]:
            self.setup.mc.animate_move("right", 5)
        else:
            ...

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
                            self.setup.mc.animate_move("up")
                        case pygame.K_DOWN:
                            self.setup.mc.animate_move("down")
                        case pygame.K_LEFT:
                            self.setup.mc.animate_move("left")
                        case pygame.K_RIGHT:
                            self.setup.mc.animate_move("right")
                        case pygame.K_SPACE:
                            ...  # for jump
                        case _:
                            ...
                case _:
                    ...
        self.continue_running()

    def update(self) -> None:
        self.surface.fill((255, 255, 255))
        self.map.draw()
        self.surface.blit(self.setup.mc.image, self.setup.mc.rect)
        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick(self.fps)
            self.events()
            self.update()
