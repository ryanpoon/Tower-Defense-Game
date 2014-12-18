sqsz = 50

import pygame, random, math
class Monster(pygame.sprite.Sprite):

    movement = ['rrruuuurrrddddddlllddrrrrruuuuuuuurrrrdddrdrddddrruuuurrrrrr',
                'rrrruuulldddrrrrurrdddrrrruuuuluurrrrrddddrrrrr',
                'rrrrrurrdrrdrrurrrurrdrrrrr']

    def __init__(self,life,speed,value,level):
        pygame.sprite.Sprite.__init__(self)

        self.level = level
        self.x = -1*50+25
        self.y = 5*50+25
        self.movementspot = 0
        self.movementtimes = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.alive = True
        self.life = life
        self.speed = speed
        self.value = value

    def hit(self,damage):
        self.life-=damage

    def isdead(self):
        if self.life <= 0:
            return True
        else:
            return False
            

    def move(self):
        if self.movementspot == len(Monster.movement[self.level]):
            self.alive = False
            return
        
        way = Monster.movement[self.level][self.movementspot]
        if way == 'r':
            self.x = self.x + self.speed
        elif way == 'l':
            self.x = self.x -self.speed
        elif way == 'u':
            self.y = self.y -self.speed
        elif way == 'd':
            self.y = self.y +self.speed
        
        self.movementtimes = self.movementtimes +1
        if self.movementtimes == sqsz/self.speed:
            self.movementspot = self.movementspot +1
            self.movementtimes = 0
        self.rect.center = (self.x, self.y)



class BasicMonster(Monster):

    image = None
    
    def __init__(self,level):
        if BasicMonster.image is None:
            BasicMonster.image = pygame.image.load("Monster.png")
        self.image = BasicMonster.image
        Monster.__init__(self,2,2,10,level)

class LifeMonster(Monster):

    image = None

    def __init__(self,level):
        if LifeMonster.image is None:
            LifeMonster.image = pygame.image.load("LifeMonster.png")
        self.image = LifeMonster.image
        Monster.__init__(self,5,2,10,level)

class SpeedMonster(Monster):

    image = None

    def __init__(self,level):
        if SpeedMonster.image is None:
            SpeedMonster.image = pygame.image.load("SpeedMonster.png")
        self.image = SpeedMonster.image
        Monster.__init__(self,2,4.1666666666666666,10,level)

class HenchMonster(Monster):
    image = None

    def __init__(self,level):
        if HenchMonster.image is None:
            HenchMonster.image = pygame.image.load("HenchMonster.png")
        self.image = HenchMonster.image
        Monster.__init__(self,3,2,10,level)

class LifeyMonster(Monster):

    image = None

    def __init__(self,level):
        if LifeyMonster.image is None:
            LifeyMonster.image = pygame.image.load("LifeMonster.png")
        self.image = LifeyMonster.image
        Monster.__init__(self,5,2.5,10,level)

class SuperSpeedMonster(Monster):

    image = None

    def __init__(self,level):
        if SpeedMonster.image is None:
            SpeedMonster.image = pygame.image.load("SpeedMonster.png")
        self.image = SpeedMonster.image
        Monster.__init__(self,4,4.1666666666666666,10,level)

    

        

