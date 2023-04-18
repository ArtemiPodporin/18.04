from pickle import FALSE
import pygame, sys

pygame.init()
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
pudge=pygame.image.load("zxc.png")
posX=0
posY=0
lõpp=False 
samm=2
suund = "paremale"
while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
            
    if suund == "paremale":
        if posX >= X - pudge.get_rect().width:
            suund = "alla"
        else:
            posX += samm
    elif suund == "alla":
        if posY >= Y - pudge.get_rect().height:
            suund = "vasakule"
        else:
            posY += samm
    elif suund == "vasakule":
        if posX <= 0:
            suund = "üles"
        else:
            posX -= samm
    elif suund == "üles":
        if posY <= 0:
            suund = "peatatud"  
        else:
            posY -= samm

    if suund != "peatatud":  
        ekraan.blit(pudge,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()


