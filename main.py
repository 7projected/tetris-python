import pygame, sys
import board

pygame.init()

screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
DEBUG_FONT = pygame.font.Font('assets/joystix monospace.otf', 12)
FRAMERATE :int= 30
delta :float= 0
game_board = board.Board(8, 16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill([0, 0, 0])
    
    game_board.draw(screen)
    
    fps_text = DEBUG_FONT.render(f'{int(clock.get_fps())}', False, [127, 127, 127])
    screen.blit(fps_text, [0, 0])
    
    pygame.display.update()
    delta = clock.tick(FRAMERATE) / 1000