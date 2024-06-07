import pygame, random

TILE_SIZE = 32

TILE = pygame.image.load('assets/tile.png')
TILE = pygame.transform.scale(TILE, [TILE_SIZE, TILE_SIZE])
CYAN_TILE = TILE.copy()
YELLOW_TILE = TILE.copy()
PURPLE_TILE = TILE.copy()
GREEN_TILE = TILE.copy()
BLUE_TILE = TILE.copy()
RED_TILE = TILE.copy()
ORANGE_TILE = TILE.copy()

# CODE WRITTEN BY CHAT GPT :
COLOR_SUBTRACT = 100
BRIGHT = 255
DIM = 200
CYAN_TILE.fill([0, BRIGHT - COLOR_SUBTRACT, BRIGHT - COLOR_SUBTRACT], special_flags=pygame.BLEND_ADD)
YELLOW_TILE.fill([BRIGHT - COLOR_SUBTRACT, BRIGHT - COLOR_SUBTRACT, 0], special_flags=pygame.BLEND_ADD)
PURPLE_TILE.fill([DIM - COLOR_SUBTRACT, 0, DIM - COLOR_SUBTRACT], special_flags=pygame.BLEND_ADD)
GREEN_TILE.fill([0, BRIGHT - COLOR_SUBTRACT, 0], special_flags=pygame.BLEND_ADD)
BLUE_TILE.fill([0, 0, BRIGHT - COLOR_SUBTRACT], special_flags=pygame.BLEND_ADD)
RED_TILE.fill([BRIGHT - COLOR_SUBTRACT, 0, 0], special_flags=pygame.BLEND_ADD)
ORANGE_TILE.fill([BRIGHT - COLOR_SUBTRACT, 165 - COLOR_SUBTRACT, 0], special_flags=pygame.BLEND_ADD)
# : END OF CHAT GPT WRITTEN CODE

SPRITE_LIST :list= [CYAN_TILE, YELLOW_TILE, PURPLE_TILE, GREEN_TILE, BLUE_TILE, RED_TILE, ORANGE_TILE]

class Board:
    def __init__(self, x_tiles:int, y_tiles:int):
        self.tile_list = []
        for y in range(y_tiles):
            app = []
            for x in range(x_tiles):
                app.append(random.randint(0, 1) - 1)
            self.tile_list.append(app)
    
    def draw(self, surf:pygame.Surface):
        for y_index, y in enumerate(self.tile_list):
            for x_index, x in enumerate(y):
                if x != -1:
                    surf.blit(SPRITE_LIST[x], [x_index * TILE_SIZE, y_index * TILE_SIZE])