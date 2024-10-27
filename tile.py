import pygame
from imagepath import ImagePath

class Tile(pygame.rect.Rect):
    def __init__(self, x, y):
        self.image: ImagePath = ImagePath()
        self.state = 'unopened'
        self.x = x
        self.y = y
        self.rect = self.get_rect()
        self.is_revealed = False
        self.is_bomb = False
        
    def get_rect(self):
        return self.image.get_current().get_rect(topleft=(self.x, self.y))
    
    def reveal(self):
        self.image.revealed()
        self.image.open_()
        self.is_revealed = True
    
    def select(self):
        self.image.select()
        return self
    
    def unselect(self):
        self.image.unselect()
        
    def set_bomb(self):
        self.image.set_bomb()
        self.is_bomb = True