import pygame, sys, pyperclip
X_TILES :int= 4
Y_TILES :int= 4
TILE_SIZE :int= 64
tile_list = []

# 0 = drawn   1 = rotation point   2 = empty
colors = [[255, 255, 255], [0, 255, 0], [0, 0, 0]]

for y in range(Y_TILES):
    app = []
    for x in range(X_TILES):
        app.append(2)
    tile_list.append(app)

pygame.init()

screen = pygame.display.set_mode([X_TILES * TILE_SIZE, Y_TILES * TILE_SIZE])
clock = pygame.time.Clock()

def save_to_clipboard():
    str = "["
    for y in tile_list:
        ap = "["
        for x in y:
            ap += f'{x},'
        ap += "]"
        str += ap
    str += "]"
    pyperclip.copy(str)

def gridify(coords:list, tile_size:int):
    snapped_x = int(coords[0] / tile_size)
    snapped_y = int(coords[1] / tile_size)
    return [snapped_x, snapped_y]

def paint(mouse_pos:list, num:int):
    grid_mouse_pos = gridify(mouse_pos, TILE_SIZE)
    tile_list[grid_mouse_pos[1]][grid_mouse_pos[0]] = num-1

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button <= 3:
                paint(mouse_pos, event.button)
        if event.type == pygame.KEYDOWN:
            save_to_clipboard()
    
    screen.fill([0, 0, 0])
    
    for y in range(len(tile_list)):
        for x in range(len(tile_list[y])):
            tile = tile_list[y][x]
            pygame.draw.rect(screen, colors[tile], [x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE])
    
    for x in range(X_TILES):
        pygame.draw.line(screen, [255,255,255], [(x+1) * TILE_SIZE, 0], [(x+1) * TILE_SIZE, Y_TILES * TILE_SIZE])
    
    for y in range(Y_TILES):
        pygame.draw.line(screen, [255,255,255], [0, (y+1) * TILE_SIZE], [X_TILES * TILE_SIZE, (y + 1) * TILE_SIZE])
            
    
    pygame.display.update()
    clock.tick(60)