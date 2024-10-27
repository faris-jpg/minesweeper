import sys, pygame
from tile import Tile
from cursor import Cursor
pygame.init()


tile_size = 16
size = width, height = tile_size*30, tile_size*16
gray = 147, 151, 153
tiles: list[Tile] = [Tile(x*tile_size, y*tile_size) for x in range(30) for y in range(16)]
cursor: Cursor = Cursor(0, 0, tile_size, width, height)
selected: Tile = tiles[0].select()

screen: pygame.surface.Surface = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cursor.move_up()
            elif event.key == pygame.K_DOWN:
                cursor.move_down()
            elif event.key == pygame.K_LEFT:
                cursor.move_left()
            elif event.key == pygame.K_RIGHT:
                cursor.move_right()
            elif event.key == pygame.K_SPACE:
                selected.reveal()
                continue
                
            for tile in tiles:
                if tile.rect.collidepoint(cursor.get_pos()):
                    selected.unselect()
                    selected = tile.select()
                    break

    screen.fill(gray)
    for tile in tiles:
        screen.blit(tile.image, tile.rect)
    pygame.display.flip()
