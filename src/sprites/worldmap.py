import os
import random

import pygame
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from pygame.locals import Rect
import numpy as np

TILE_W, TILE_H = 128, 128
TILES = {
    "grass": (0, 0),
    "darkgrass": (128, 0),
    "dirt": (256, 0),
    "road": (384, 0),
    "rock": (512, 0),
    "red soil top": (640, 0),
    "red soil": (768, 0),
    "barrel": (896, 0),
}
DEBUG: bool = False


class MapGenerator:

    x: int
    y: int
    tiles: np.ndarray
    offset: tuple[int, int]
    tiles_x: int
    tiles_y: int
    tileset: pygame.surface.Surface
    rect: pygame.rect.Rect
    pos_x: int
    pos_y: int

    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.size = 2048, 2048
        self.screen = surface
        print(self.screen)
        self.walls = [6]
        self.load_tileset(os.path.join("assets/maps", "tileset.bmp"))
        self.generate()

    def reset(self) -> None:
        self.tiles_x, self.tiles_y = self.size[0] // TILE_W, self.size[1] // TILE_H
        self.tiles = np.zeros((self.tiles_y, self.tiles_x), dtype=int)
        return None

    # Generate map using perlin noise
    def generate(self) -> None:
        self.reset()
        noise = PerlinNoise(octaves=6, seed=random.randint(0, 100))
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                z = [x / self.tiles_x, y / self.tiles_y]
                n = noise(z)
                print(n)
                if n < 0.2:
                    self.tiles[y][x] = 5
                elif n < 0.3:
                    self.tiles[y][x] = 6
                elif n < 0.4:
                    self.tiles[y][x] = 7
                elif n < 0.6:
                    self.tiles[y][x] = 4
                else:
                    self.tiles[y][x] = 2
        if DEBUG:
            plt.imshow(self.tiles)
            plt.show()
        return None

    def load_tileset(self, image: str = "tileset.bmp") -> None:
        self.tileset = pygame.image.load(image)
        self.rect = self.tileset.get_rect()
        return None

    # Draw map around player position
    def draw(self, pos: tuple[int, int] = None) -> None:
        position = pos or (self.pos_x, self.pos_y)
        self.offset = position[0] - self.screen.get_width() // 2, position[1] - self.screen.get_height() // 2
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                tile = self.tiles[y][x]
                _type = list(TILES.keys())[tile]
                coords = TILES[_type]
                self.screen.blit(
                    self.tileset,
                    (x * TILE_W - self.offset[0], y * TILE_H - self.offset[1]),
                    Rect(coords[0], coords[1], TILE_W, TILE_H),
                )
