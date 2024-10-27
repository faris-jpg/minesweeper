import pygame
class Cursor:
    def __init__(self, x, y, stepsize, width, height):
        self.x = x
        self.y = y
        self.stepsize = stepsize
        self.width = width - stepsize
        self.height = height - stepsize
    
    def move_cursor(self, event):
        if event.key == pygame.K_UP:
            self.move_up()
        elif event.key == pygame.K_DOWN:
            self.move_down()
        elif event.key == pygame.K_LEFT:
            self.move_left()
        elif event.key == pygame.K_RIGHT:
            self.move_right()
        else:
            return False
        return True
        
    def move_up(self):
        if self.y <= 0:
            return
        self.y -= self.stepsize
        print(self.get_pos())
    
    def move_down(self):
        if self.y >= self.height:
            return
        self.y += self.stepsize
        print(self.get_pos())

        
    def move_right(self):
        if self.x >= self.width:
            return
        self.x += self.stepsize
        print(self.get_pos())

    
    def move_left(self):
        if self.x <= 0:
            return
        self.x -= self.stepsize
        print(self.get_pos())

        
    def get_pos(self):
        return self.x, self.y
        

    def __repr__(self):
        return f'Cursor({self.x}, {self.y})'