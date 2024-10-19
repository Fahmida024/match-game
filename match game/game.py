import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
textfont=pygame.font.SysFont('comicsans',40)
screen=pygame.display.set_mode((600,600))
playing=True
templerun=pygame.image.load('TempleRun.jpg')
templerun1=pygame.transform.scale(templerun,(80,80))
crossyroad=pygame.transform.scale(pygame.image.load('Crossy_Road_icon.jpeg'),(80,80))
pianogame=pygame.transform.scale(pygame.image.load('piano.jpeg'),(80,80))
mario=pygame.transform.scale(pygame.image.load('Mario.png'),(80,80))



while playing:
    screen.fill('purple')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False


    screen.blit(templerun1,(50,50))
    screen.blit(crossyroad,(50,200))
    screen.blit(mario,(50,350))
    screen.blit(pianogame,(50,500))


    game1text=textfont.render('Crossy Road',1,('black'))
    screen.blit(game1text,(300,50))
    game2text=textfont.render('Piano game',1,('black'))
    screen.blit(game2text,(300,200))
    game3text=textfont.render('Temple Run',1,('black'))
    screen.blit(game3text,(300,350))
    game4text=textfont.render('Mario',1,('black'))
    screen.blit(game4text,(300,500))

    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(pos),20,0)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(pos2),20,10)
        pygame.display.update()
    





    pygame.display.update()