import pygame, random
pygame.init()
mushroom_image = pygame.image.load('mushroom.gif')
screen = pygame.display.set_mode([625,700])
game_map = []
mushrooms = []
running = True
pygame.draw.rect(screen, pygame.color.THECOLORS['black'], (0,0,750,840))
def setup_game_map():
    
    for x in range(0,28):
        arrayOfZeros = [0]*25
        game_map.append(arrayOfZeros)
    for x in range (0,30):
        mushroomx = random.randint(0, 24)
        mushroomy = random.randint(0, 27)
        mushrooms.append("mushroom")
        #print "x: " , mushroomx
        #print "y: " , mushroomy
        game_map[mushroomy][mushroomx] = 1
        #mushroom(mushroomx, mushroomy)
        
    print game_map

setup_game_map()
def draw_game_map():
        for column in range(25):
            for row in range(28):
                spot = game_map[row][column]
                if spot == 1:
                    screen.blit(mushroom_image, [column*25, row*25])
while running:
    for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                running = False
    pygame.time.delay(15)
    draw_game_map()
    pygame.display.update()
pygame.quit()
