import pygame, random, math
class BasicTower(pygame.sprite.Sprite):

    image = None

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        if BasicTower.image is None:
            BasicTower.image = pygame.image.load("Turret.png")
        self.image = BasicTower.image
        self.x = x*50+25
        self.y = y*50+20
        self.tilex = x
        self.tiley = y
        self.reload_time = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def inrange(self,target):
        base = self.x - target.x
        height = self.y - target.y
        step1 = base*base + height*height
        if math.sqrt(step1) < 121:
            return True
        else:
            return False
            

    def tryShoot(self, target_list):
        self.reload_time -= 1
        if self.reload_time < 1:
            for basicmonster in target_list:
                if self.inrange(basicmonster) == True:
                    self.reload_time = 40
                    return basicmonster
        return None
