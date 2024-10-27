import pygame
filepath = "images/"
opened_filepath = filepath + 'opened/'
selected_filepath = filepath + 'selected/'
class ImagePath:
    def __init__(self):
        self.images = {
            'unopened': filepath + 'unopened.png' ,
            'selected': selected_filepath + 'blank.png' ,
            'opened': opened_filepath + 'empty.png'
        }
        self.state = 'unopened'
        self.prev_state = 'unopened'
        self.is_revealed = False
        self.is_bomb = False
        self.is_number = False
        self.number = 1
        
    def get_current(self):
        return pygame.image.load(self.images[self.state])
    
    def open_(self):
        self.state = 'opened'
        self.prev_state = 'opened'
    
    def select(self):
        self.prev_state = self.state
        self.state = 'selected'
        
    def unselect(self):
        self.state = self.prev_state
        
    def revealed(self):
        if self.is_bomb:
            self.images['selected'] = selected_filepath + 'bomb.png'
        elif self.is_number:
            self.images['selected'] = selected_filepath + str(self.number) + '.png'
        else:
            self.images['selected'] = selected_filepath + 'empty.png'

        
    
    def set_bomb(self):
        self.images['opened'] = opened_filepath + 'bomb.png'
        self.is_bomb = True
        return
    
    def set_number(self, number):
        self.is_number = True
        number = str(number) + '.png'
        self.images['selected'] = selected_filepath + number
        self.images['opened'] = opened_filepath + number
        