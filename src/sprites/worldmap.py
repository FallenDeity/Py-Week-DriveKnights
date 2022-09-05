import os
from random import randint

import pygame
import numpy as np

TILE_W, TILE_H = 32, 32
TILES = {"grass": 0, "darkgrass": 1, "dirt": 2, "road": 3}


class MapGenerator:

    x: int
    y: int
    tiles: np.ndarray
    offset: tuple[int, int]
    tiles_x: int
    tiles_y: int
    tileset: pygame.surface.Surface
    rect: pygame.rect.Rect

    def __init__(self, surface: pygame.surface.Surface, size: tuple[int, int]) -> None:
        self.size = size
        self.screen = surface
        self.scrolling = False
        self.load_tileset(os.path.join("src/assets/maps", "tileset.bmp"))
        self.reset()
        self.randomize()

    def reset(self) -> None:
        self.tiles_x, self.tiles_y = self.size[0] // TILE_W, self.size[1] // TILE_H
        self.tiles = np.zeros((self.tiles_y, self.tiles_x), dtype=int)
        return None

    def randomize(self) -> None:
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                self.tiles[y][x] = randint(0, len(TILES.keys()) - 1)
        return None

    def load_tileset(self, image: str = "tileset.bmp") -> None:
        self.tileset = pygame.image.load(image)
        self.rect = self.tileset.get_rect()
        return None

    def draw(self) -> None:
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                cur = self.tiles[y][x]
                self.screen.blit(self.tileset, (x * TILE_W, y * TILE_H), (cur * TILE_W, 0, TILE_W, TILE_H))
        return None
