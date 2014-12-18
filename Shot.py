import pygame, random, math
class Shot(pygame.sprite.Sprite):

    image = None
    DamageTowerSound = pygame.mixer.Sound('damagetowersound.wav')
    TowerSound = pygame.mixer.Sound('notdamagetowersound.wav')
    DamageTowerSound.set_volume(.2)
    TowerSound.set_volume(.1)
    def __init__(self,tower,target):
        pygame.sprite.Sprite.__init__(self)

        if Shot.image is None:
            Shot.image = pygame.image.load("Shot.png")
        self.image = Shot.image
        self.x = tower.x
        self.y = tower.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        #calculate the angle between tower and target
        dx = target.x - tower.x
        dy = target.y - tower.y
        self.rads = math.atan2(dy,dx)
        if tower.__class__.__name__ == 'DamageTower':
            Shot.DamageTowerSound.play()
            self.damage = 2
        else:
            self.damage = 1
            Shot.TowerSound.play()
        
    def move(self):
        #uses angle to move shot
       self.x = self.x + math.cos(self.rads) * 30
       self.y = self.y + math.sin(self.rads) * 30
       self.rect.center = (self.x, self.y)
        
   
