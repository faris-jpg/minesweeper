import sys, pygame, random
from tile import Tile
from cursor import Cursor

class Minesweeper:
    def __init__(self):
        self.tile_size = 16
        self.size = width, height = self.tile_size*30, self.tile_size*16
        self.gray = 147, 151, 153
        self.tiles: list[Tile] = [Tile(x*self.tile_size, y*self.tile_size) for x in range(30) for y in range(16)]
        self.cursor: Cursor = Cursor(0, 0, self.tile_size, width, height)
        self.selected: Tile = self.tiles[0].select()
        self.screen: pygame.surface.Surface = pygame.display.set_mode(self.size)
        self.is_first = True
        
    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
                
                self.select_tile()
                              
                self.set_screen()
                    
                pygame.display.flip()
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
                    sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.reveal_tile()
            else:
                self.cursor.move_cursor(event)
    
    def select_tile(self):
        for tile in self.tiles:
            if tile.rect.collidepoint(self.cursor.get_pos()):
                self.selected.unselect()
                self.selected = tile.select()
                break
    
    def reveal_tile(self):
        self.selected.reveal()
        print('here')
        if not self.is_first:
            return  
        self.set_bombs() 
    
    def set_bombs(self):
        tiles_without_selected = [tile for tile in self.tiles if tile != self.selected]
        self.bomb_tiles = random.sample(tiles_without_selected, 100)
        for tile in self.bomb_tiles:
            tile.set_bomb()
        self.is_first = False
            
    def set_screen(self):
        self.screen.fill(self.gray)
        for tile in self.tiles: 
            self.screen.blit(tile.image.get_current(), tile.rect)
        

if __name__ == "__main__":
    pygame.init()
    Minesweeper().run()
        
        