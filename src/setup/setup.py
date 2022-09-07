import os
import pygame
from src.sprites import MapGenerator
from src.sprites import MainCharacter
PATH: str = "assets/characters/mc/"
ALPHA: tuple[int, int, int] = (255, 255, 255)
ANIMATIONS: dict[str, list[pygame.surface.Surface]] = {}
ANIMATION: dict[str, list[pygame.surface.Surface]] = {}



class Setup:

    mc: MainCharacter
    @staticmethod
    def get_mc_frames() -> dict[str, list[pygame.surface.Surface]]:
        for i in os.listdir(PATH):
            for j in os.listdir(f"{PATH}/{i}"):
                img = pygame.image.load(f"{PATH}/{i}/{j}").convert_alpha()
                img.set_colorkey(ALPHA)
                if i not in ANIMATIONS:
                    ANIMATIONS[i] = [img]
                else:
                    ANIMATIONS[i].append(img)
        return ANIMATIONS

    def __init__(self, screen: tuple[int, int], world: MapGenerator) -> None:
        self.get_mc_frames()
        self.mc = MainCharacter(ANIMATIONS, screen, world)
        self.resize()
        self.mc = MainCharacter(ANIMATION, screen, world)

    def resize(self) -> None:
        ht = self.mc.screen[1]
        for i in ANIMATIONS:
            for j in ANIMATIONS[i]:
                res = pygame.transform.scale(j, (ht // 8, ht // 8))
                res.set_colorkey(ALPHA)
                if i not in ANIMATION:
                    ANIMATION[i] = [res]
                else:
                    ANIMATION[i].append(res)
