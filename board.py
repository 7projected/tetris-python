import pygame, random

def generateBackground(surf:pygame.Surface, x_tiles:int, y_tiles:int) -> pygame.Surface:
    ret_surf = pygame.Surface([surf.get_width() * x_tiles, surf.get_height() * y_tiles])
    for y in range(y_tiles):
        for x in range(x_tiles):
            ret_surf.blit(surf, [x * surf.get_width(), y * surf.get_height()])
    return ret_surf
    

def loadTiles(tile_size:int) -> list:
    tile = pygame.image.load('assets/tile.png')
    tile = pygame.transform.scale(tile, [tile_size, tile_size])
    cyan_tile = tile.copy()
    yellow_tile = tile.copy()
    purple_tile = tile.copy()
    green_tile = tile.copy()
    blue_tile = tile.copy()
    red_tile = tile.copy()
    orange_tile = tile.copy()

    # code written by chat gpt:
    color_subtract = 100
    bright = 255
    dim = 200
    cyan_tile.fill([0, bright - color_subtract, bright - color_subtract], special_flags=pygame.BLEND_ADD)
    yellow_tile.fill([bright - color_subtract, bright - color_subtract, 0], special_flags=pygame.BLEND_ADD)
    purple_tile.fill([dim - color_subtract, 0, dim - color_subtract], special_flags=pygame.BLEND_ADD)
    green_tile.fill([0, bright - color_subtract, 0], special_flags=pygame.BLEND_ADD)
    blue_tile.fill([0, 0, bright - color_subtract], special_flags=pygame.BLEND_ADD)
    red_tile.fill([bright - color_subtract, 0, 0], special_flags=pygame.BLEND_ADD)
    orange_tile.fill([bright - color_subtract, 165 - color_subtract, 0], special_flags=pygame.BLEND_ADD)
    # end of chat gpt written code

    return [cyan_tile, yellow_tile, purple_tile, green_tile, blue_tile, red_tile, orange_tile]

class Board:
    def __init__(self, position:list, x_tiles:int, y_tiles:int, tile_size:int):
        self.tile_list = []
        self.position = position
        self.tile_size = tile_size
        self.sprite_list = loadTiles(tile_size)
        for y in range(y_tiles):
            app = []
            for x in range(x_tiles):
                app.append(-1)
            self.tile_list.append(app)
    
    def draw(self, surf:pygame.Surface):
        y_size = self.tile_size * len(self.tile_list)
        x_size = self.tile_size * len(self.tile_list[0])
        pygame.draw.rect(surf, [75, 75, 75], [self.position[0], self.position[1], x_size, y_size])
        pygame.draw.rect(surf, [0, 0, 0], [self.position[0], self.position[1], x_size, y_size], 1)
        for y_index, y in enumerate(self.tile_list):
            for x_index, x in enumerate(y):
                if x != -1:
                    surf.blit(self.sprite_list[x], [x_index * self.tile_size + self.position[0] , y_index * self.tile_size + self.position[1]])