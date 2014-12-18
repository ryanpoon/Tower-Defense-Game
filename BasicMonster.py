import pygame, random, math
class Monster(pygame.sprite.Sprite):

    image = None
    movement = 'rrruuuurrrddddddlllddrrrrruuuuuuuurrrrdddrdrddddrruuuurrrrrr'

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if Monster.image is None:
            Monster.image = pygame.image.load("Monster.png")
        self.image = Monster.image
        self.x = -1*50+25
        self.y = 6*50+25
        self.movementspot = 0
        self.movementtimes = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.alive = True
        self.life = 2

    def hit(self):
        self.life-=1

    def isdead(self):
        if self.life == 0:
            return True
        else:
            return False
            

     
    def move(self):
        if self.movementspot == len(Monster.movement):
            self.alive = False
            return
        
        way = Monster.movement[self.movementspot]
        if way == 'r':
            self.x = self.x + 2
        elif way == 'l':
            self.x = self.x -2
        elif way == 'u':
            self.y = self.y -2
        elif way == 'd':
            self.y = self.y +2
        
        self.movementtimes = self.movementtimes +1
        if self.movementtimes == 25:
            self.movementspot = self.movementspot +1
            self.movementtimes = 0
        self.rect.center = (self.x, self.y)

        

