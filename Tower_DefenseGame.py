import pygame, random, math, datetime
pygame.init()
from Tower import *
from Monster import *
from Shot import *

pygame.display.set_caption('Tower Defense')
mode = 'menu'
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([1200,500])
lives = 20
myfont = pygame.font.SysFont("Arial", 20)
smallfont = pygame.font.SysFont("Arial", 15)
heart_image = pygame.image.load('Heart.png')
grass_image = pygame.image.load('Grass 4.jpg')
path_image = pygame.image.load('Path 2.jpg')

white = [255, 255, 255]
money = 100
kills = 0
running = True
LoseHealthsound = pygame.mixer.Sound('LoseHealth.wav')
titlefont = pygame.font.SysFont("Baskerville", 100)
towers = []
waves = [
            ['bbbbbbbb','hhhbhbhhh','sssssss','sslllllss','yyyaaaaaayyyy','yyyyyyaaaaaaaaaaaa'],
            ['bbbbbbbb','hhhsshsshhh','lhhlslslhhl','yyyyyyyyyyyy','yyyyaaaaaaaaayyyy','aaaaaaaaaaaaaaaaaaaaa'],
            ['ssssssss','hhssssssssssshh','aaassssssssaaaa','aaaaasssssaaaaaaa','aaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaaa']
         ]  
wave = 0
towerselection = 1
shots = []
pause = False
timer = 0
wavemonster = 0
loop = 0
shouldsort =0
level = 0
topthreescores = ['','','']
monsters= []
game_map =[ [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0],
                [1,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1],
                [0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0],
                [0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0],
                [0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0]
                
            ],
            [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
                [0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
                [0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0],
                [0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0],
                [1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,1],
                [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
            ],
            [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
            ]
        ]
def get_topthreescores():
    global topthreescores
    everyscore = []
    with open('tower_defensehighscore.txt', 'r') as f:
        for line in f:
            everyscore.append(line)

    everyscore.sort()
    everyscore.reverse()
    topthreescores = everyscore[0:3]
    
get_topthreescores()
            

def draw_game_map():
    for column in range(20):
        for row in range(10):
            spot = game_map[level][row][column]
            if spot == 0 or spot == 2:
                screen.blit(grass_image, [column*50, row*50])
                #pygame.draw.rect(screen,pygame.color.THECOLORS['white'],(column*50,row*50,50,50))
            elif spot == 1:
                screen.blit(path_image, [column*50, row*50])
                #pygame.draw.rect(screen,pygame.color.THECOLORS['brown'],(column*50,row*50,50,50))

def comparemonsterlocation(monster1, monster2):
    if monster1.movementspot > monster2.movementspot:
        return -1
    elif monster1.movementspot < monster2.movementspot:
        return 1
    else:
        if monster1.movementtimes > monster2.movementtimes:
            return -1
        elif monster1.movementtimes < monster2.movementtimes:
            return 1
        else:
            return 0
def draw_sidepanel():
    pygame.draw.rect(screen,(106,181,0),(1000,0,1150,600))

    s = pygame.Surface((200,50))  # the size of your rect
    s.set_alpha(128)                # alpha level
    s.fill(pygame.color.THECOLORS['yellow'])           # this fills the entire surface
    
    if towerselection == 1:
        screen.blit(s, (1000,45)) 
    if towerselection == 2:
        screen.blit(s, (1000,115))
    if towerselection == 3:
        screen.blit(s, (1000,185))
    if towerselection == 4:
        screen.blit(s, (1000,255))
    screen.blit(myfont.render('1. Basic Tower' ,1,pygame.color.THECOLORS['black']), (1005,50))
    screen.blit(smallfont.render('$100 Average fire rate' ,1,pygame.color.THECOLORS['black']), (1020,80))
    screen.blit(myfont.render('2. Range Tower' ,1,pygame.color.THECOLORS['black']), (1005,120))
    screen.blit(smallfont.render('$120 Long Range' ,1,pygame.color.THECOLORS['black']), (1020,150))
    screen.blit(myfont.render('3. Fast Tower' ,1,pygame.color.THECOLORS['black']), (1005,190))
    screen.blit(smallfont.render('$140 Fast fire rate' ,1,pygame.color.THECOLORS['black']), (1020,220))
    screen.blit(myfont.render('4. Damage Tower' ,1,pygame.color.THECOLORS['black']), (1005,260))
    screen.blit(smallfont.render('$180 Big Damage' ,1,pygame.color.THECOLORS['black']), (1020,290))

def spawn_monsters():
    global wavemonster, waves, wave, pause, loop,timer,shouldsort
    if level == 2 and wave >= 3:
        exception = 17
    else:
        exception = 25
    
    if loop%exception == 0 and len(waves[level]) > wave and pause == False:
        if wavemonster == len(waves[level][wave]):
            wavemonster = 0
            pause = True
            timer = 0
        else:
            if waves[level][wave][wavemonster]=='b':
                basicmonster = BasicMonster(level)
                monsters.append(basicmonster)
            if waves[level][wave][wavemonster]=='l':
                lifemonster = LifeMonster(level)
                monsters.append(lifemonster)
            if waves[level][wave][wavemonster]=='s':
                speedmonster = SpeedMonster(level)
                monsters.append(speedmonster)
            if waves[level][wave][wavemonster]=='h':
                henchmonster = HenchMonster(level)
                monsters.append(henchmonster)
            if waves[level][wave][wavemonster]=='y':
                lifeymonster = LifeyMonster(level)
                monsters.append(lifeymonster)
            if waves[level][wave][wavemonster]=='a':
                superspeedmonster = SuperSpeedMonster(level)
                monsters.append(superspeedmonster)
            wavemonster = wavemonster +1
            shouldsort = 10

def checklevel():
    global wave,level,towers,money,mode
    if wave == 6 and len(monsters) == 0:
        wave = 0
        level = level+1
        towers = []
        money = 100+money/4
    if wave == 0 and level == 3 and len(monsters) ==0:
        with open('tower_defensehighscore.txt', 'a') as file_:
            file_.write('w,'+str(health) +'\n')
        get_topthreescores()
        mode = 'menu'
            
def handle_keys():
    global towerselection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        towerselection =1
    if keys[pygame.K_2]:
        towerselection =2
    if keys[pygame.K_3]:
        towerselection =3
    if keys[pygame.K_4]:
        towerselection =4
def pretty_score(score):
    if score[0] == 'w':
        return 'Won with'+' '+score[2]+' '+'health.'
    else:
        scorearray = score.split(',')
        return 'Got to level '+scorearray[0]+' with '+scorearray[1].strip('\n')+' kills.'

def moveandsortmonsters():
    global lives, shouldsort, monsters,running, mode
    for monster in monsters:
        monster.move()
        if monster.alive == False:
            monsters.remove(monster)
            lives = lives - 1
            LoseHealthsound.play()
            if lives <= 0:
                
                #'a' opens the file in append mode (it will add on to the end of the file if it
                #exists or create the file if it doesn't exist). 
                with open('tower_defensehighscore.txt', 'a') as file_:
                                       
                        file_.write(str(level+1) +','+str(kills) +'\n') #\n is the new line character to drop to the next line

 
                get_topthreescores()                       
                mode = 'menu'
        

   
    if len(monsters) > 1 and shouldsort == 10:            
        monsters = sorted(monsters, cmp=comparemonsterlocation)
        shouldsort = 0

def handleclicks():
    global towerseletion, money,towers,gamemap
    pressed=pygame.mouse.get_pressed()
    if pressed[0] ==True:
        pos = pygame.mouse.get_pos()
        tile_x = pos[0]/50
        tile_y = pos[1]/50
        if tile_y >11 or tile_x >19:
            return None
        spot = game_map[level][tile_y][tile_x]
        if towerselection ==1:
            if money >= 100:
                if spot ==  0:
                    basictower = BasicTower(tile_x,tile_y)
                    money = money - 100
                    towers.append(basictower)
                    game_map[level][tile_y][tile_x] = 2
        elif towerselection == 3:
            if money >= 140:
                if spot ==  0:
                     fasttower = FastTower(tile_x,tile_y)
                     money = money - 140
                     towers.append(fasttower)
                     game_map[level][tile_y][tile_x] = 2
        elif towerselection == 2:
            if money >= 120:
                if spot ==  0:
                     rangetower = RangeTower(tile_x,tile_y)
                     money = money - 120
                     towers.append(rangetower)
                     game_map[level][tile_y][tile_x] = 2
        elif towerselection == 4:
            if money >= 180:
                if spot ==  0:
                     damagetower = DamageTower(tile_x,tile_y)
                     money = money - 180
                     towers.append(damagetower)
                     game_map[level][tile_y][tile_x] = 2
        
    #detect shovelup
    pressed=pygame.mouse.get_pressed() 
    if pressed[2] == True:
        pos = pygame.mouse.get_pos()
        tile_x = pos[0]/50
        tile_y = pos[1]/50
        spot = game_map[level][tile_y][tile_x]
        #checks if spot is available
        if spot ==  2:
            for basictower in towers:
                if basictower.tilex == tile_x and basictower.tiley == tile_y:
                    towers.remove(basictower)
                    money+=basictower.cost/2
                    game_map[level][tile_y][tile_x] = 0
        
while running:
    for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP and mode == 'menu':
                mode = 'play'
                wave = 0
                towerselection = 1
                shots = []
                pause = False
                timer = 0
                wavemonster = 0
                loop = 0
                shouldsort =0
                level = 0
                monsters= []
                lives = 20
                money = 100
                towers = []
                kills = 0
                
    pygame.time.delay(15)
    if mode == 'menu':
        pygame.draw.rect(screen, [0,0,0],[0,0,1200,500])
        message = myfont.render("Click to Start the Game" , 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (220, 240))
        message = myfont.render("High Scores:", 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (800, 180))
        message = myfont.render('1. '+pretty_score(topthreescores[0]), 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (800, 200))
        message = myfont.render('2. '+pretty_score(topthreescores[1]), 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (800, 220))
        message = myfont.render('3. '+pretty_score(topthreescores[2]), 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (800, 240))

        title = titlefont.render("TOWER DEFENCE" , 1, pygame.color.THECOLORS['white'])
        screen.blit(title, (130, 100))
        pygame.display.update()
    if mode == 'play':
        loop = loop +1
        
        handleclicks()

        #check for pause
        timer = timer+1
        shouldsort+=1
        if pause == True and timer == 800:
            wave = wave+1
            pause = False
            print "Wave: ", wave

        handle_keys()
        
        spawn_monsters()

        checklevel()
                
        moveandsortmonsters()
                        

        #loop over all towers to call tryShoot
        for tower in towers:
            target = tower.tryShoot(monsters)
            if target != None:
                shot = Shot(tower,target)
                shots.append(shot)

        #see if shots hit
        for shot in shots:
            for monster in monsters:
                if shot.rect.colliderect(monster.rect):
                    monster.hit(shot.damage)
                    shots.remove(shot)
                    if monster.isdead()==True:
                        monsters.remove(monster)
                        kills+=1
                        money+=monster.value
                    break
                        
                        
                

        #shots move
        for shot in shots:
            shot.move()

        
        #drawing everything
        if loop % 2 == 0:
            draw_game_map() 
        for basictower in towers:
            screen.blit(basictower.image, basictower.rect)
        waveshow = myfont.render("Wave " + str(wave+1), 1, pygame.color.THECOLORS['yellow'])
        message = myfont.render("$"+ str(money) , 1, pygame.color.THECOLORS['green'])
        screen.blit(heart_image, [900, 50])
        screen.blit(message, (900, 20))
        screen.blit(waveshow, (900,80))
        for shot in shots:
            screen.blit(shot.image, shot.rect)
        for basicmonster in monsters:
            screen.blit(basicmonster.image, basicmonster.rect)
        label = myfont.render(str(lives) , 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (925, 50))
        
        draw_sidepanel()

        #update_rect = pygame.Rect(0,100,200,450)
        pygame.display.update()

pygame.quit()

