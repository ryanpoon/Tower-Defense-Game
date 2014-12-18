import pygame, random, math
class Tower(pygame.sprite.Sprite):

    image = None

    def __init__(self,x,y,shotrange,rate,cost):
        pygame.sprite.Sprite.__init__(self)

        
        self.x = x*50+25
        self.y = y*50+20
        self.tilex = x
        self.tiley = y
        self.reload_time = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.range = shotrange
        self.firerate =rate
        self.cost = cost

    def inrange(self,target):
        base = self.x - target.x
        height = self.y - target.y
        step1 = base*base + height*height
        if math.sqrt(step1) < self.range:
            return True
        else:
            return False
            

    def tryShoot(self, target_list):
        self.reload_time -= 1
        if self.reload_time < 1:
            for basicmonster in target_list:
                if self.inrange(basicmonster) == True:
                    self.reload_time = self.firerate
                    return basicmonster
        return None

class BasicTower(Tower):

    image = None

    def __init__(self,x,y):
        if BasicTower.image is None:
            BasicTower.image = pygame.image.load("Turret.png")
        self.image = BasicTower.image
        Tower.__init__(self,x,y,121,40,100)

class FastTower(Tower):

    image = None

    def __init__(self,x,y):
        if FastTower.image is None:
            FastTower.image = pygame.image.load("FastTower.png")
        self.image = FastTower.image
        Tower.__init__(self,x,y,121,30,140)

class RangeTower(Tower):

    image = None

    def __init__(self,x,y):
        if RangeTower.image is None:
            RangeTower.image = pygame.image.load("RangeTower.png")
        self.image = RangeTower.image
        Tower.__init__(self,x,y,242,40,120)

class DamageTower(Tower):

    image = None

    def __init__(self,x,y):
        if DamageTower.image is None:
            DamageTower.image = pygame.image.load("DamageTower.png")
        self.image = DamageTower.image
        Tower.__init__(self,x,y,121,40,180)

