import pygame, sys, math
import board, inputManager

pygame.init()

screen = pygame.display.set_mode([1280, 768])
clock = pygame.time.Clock()
debug_font = pygame.font.Font('assets/joystix monospace.otf', 12)
framerate :int= 100000
delta :float= 0
tile_size = 32
game_board = board.Board([1280/2 - 160, 0], 10, 24, tile_size)
default_tile_sprite = pygame.image.load("assets/tile.png")
default_tile_sprite.fill([100, 100, 100], special_flags=pygame.BLEND_SUB)
default_tile_sprite = pygame.transform.scale(default_tile_sprite, [tile_size, tile_size])
bg = board.generateBackground(default_tile_sprite, 40, 24)
input = inputManager.InputManager([pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a])

player_move :float= 0
player_move_threshold = 1.5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input.poll(event)
    
    player_move += delta * (int(input.getKeyState(pygame.K_s) * 5) + 3) 

    if player_move > player_move_threshold:
        player_move = 0

    
    screen.fill([0, 0, 0])

    screen.blit(bg, [0, 0])    
    game_board.draw(screen)
    
    fps_text = debug_font.render(f'{int(clock.get_fps())}', False, [127, 127, 127])
    screen.blit(fps_text, [0, 0])
    
    pygame.display.update()
    delta = clock.tick(framerate) / 1000 