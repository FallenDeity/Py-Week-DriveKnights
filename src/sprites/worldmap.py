import os
from random import randint

import pygame
from pygame.locals import Rect
import numpy as np

TILE_W, TILE_H = 32, 32
TILES = {
    "grass": (0, 0),
    "darkgrass": (32, 0),
    "dirt": (64, 0),
    "road": (96, 0),
    "rock": (128, 0),
    "red soil top": (160, 0),
    "red soil": (192, 0),
    "barrel": (224, 0),
}


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
        self.size = 2496, 2496
        self.screen = surface
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
