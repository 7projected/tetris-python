import pygame, sys
import board

pygame.init()

screen = pygame.display.set_mode([1280, 768])
clock = pygame.time.Clock()
debug_font = pygame.font.Font('assets/joystix monospace.otf', 12)
framerate :int= 100000
delta :float= 0
tile_size = 32
game_board = board.Board([1280/2 - 160, 0], [10, 34], tile_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill([0, 0, 0])
    
    game_board.draw(screen)
    
    fps_text = debug_font.render(f'{int(clock.get_fps())}', False, [127, 127, 127])
    screen.blit(fps_text, [0, 0])
    
    pygame.display.update()
    delta = clock.tick(framerate) / 1000