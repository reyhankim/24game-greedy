import pygame, sys
import random
from pygame.locals import *

FPS = 30
BGCOLOR = (3, 115, 46)
BEFORECLICK = (22, 22, 106)
AFTERCLICK = (200, 200, 200)
WHITE = (0, 0, 0)

boardWidth = 800
boardHeight = 800
rectX = 50
rectY = 50
rectWidth = 100
rectHeight = 150
myRectangle = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
arr_card = ['H', 'K', 'S', 'W']

def op(oper):
    if (oper == 5):
        return "+"
    elif (oper == 4):
        return "-"
    elif (oper == 3):
        return "*"
    else:
        return "/"

def result(res,num):
    n = nilai(res[1]) + nilai(res[3]) + nilai(res[5]) - Close(num,24)
    if ((res[3] == "*") | (res[3] == "/")) & ((res[1] == "+") | (res[1] == "-")):
        print("(",res[0],res[1],res[2],")",res[3], res[4], res[5], res[6])
        print(n-2)
    else:
        print(res[0],res[1],res[2],res[3], res[4], res[5], res[6])
        print(n)

def nilai(oper):
    if (oper == "+"):
        return 5
    elif (oper == "-"):
        return 4
    elif (oper == "*"):
        return 3
    else:
        return 2

def targ(n):
    if (n == 1):
        return 24
    elif(n == 2):
        return 20
    else:
        return 10

def Close(sco, tar):
    return (abs(tar-sco))

def Olah(sco, ope, num):
    if (ope == 5):
        return sco+num
    elif (ope == 4):
        return sco-num
    elif (ope == 3):
        return sco*num
    else:
        return sco/num

def Score1(sco, ope, num):
    if (ope == 5):
        return sco + ope - Close(sco+num,24) 
    elif (ope == 4):
        return sco + ope - Close(sco-num,24) 
    elif (ope == 3):
        return sco + ope - Close(sco*num,24) 
    else:
        return sco + ope - Close(sco/num,24) 

def Score2(sco, ope, num, n):
    if (ope == 5):
        return sco + ope - Close(sco+num,targ(n)) - (sco+num) % 4
    elif (ope == 4):
        return sco + ope - Close(sco-num,targ(n)) - (sco-num) % 4
    elif (ope == 3):
        return sco + ope - Close(sco*num,targ(n)) - (sco*num) % 4
    else:
        return sco + ope - Close(sco/num,targ(n)) - (sco/num) % 4

def Solve1(arr):
    num = arr[0]
    res = []
    opp = []
    ind = 0
    tmp = 0

    for i in range(1,4):
        if (arr[i] > num):
            num = arr[i]
            ind = i
    res.append(arr[ind])
    del arr[ind]

    ind = 0
    cho = -999
    neff = 3

    while (arr != []):
        cho = -999
        for i in range(0,4):
            ope = 5-i
            for j  in range(0,neff):
                sc = Score1(num,ope,arr[j])
                if (cho  < sc):
                    cho = sc
                    ind = j
                    tmp = ope
        te = arr[ind]
        num = Olah(num,tmp,te)
        opp.append(tmp)
        res.append(op(tmp))
        res.append(arr[ind])
        del arr[ind]
        neff -= 1
    result(res,num)

def Solve2(arr):
    num = arr[0]
    res = []
    opp = []
    ind = 0
    tmp = 0

    for i in range(1,4):
        if (arr[i] > num):
            num = arr[i]
            ind = i
    res.append(arr[ind])
    del arr[ind]

    ind = 0
    cho = -999
    neff = 3

    while (arr != []):
        cho = -999
        for i in range(0,4):
            ope = 5-i
            for j  in range(0,neff):
                sc = Score2(num,ope,arr[j],neff)
                if (cho  < sc):
                    cho = sc
                    ind = j
                    tmp = ope
        te = arr[ind]
        num = Olah(num,tmp,te)
        opp.append(tmp)
        res.append(op(tmp))
        res.append(arr[ind])
        del arr[ind]
        neff -= 1
    result(res,num)

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    pygame.font.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    
    myFont = pygame.font.SysFont("Times New Roman", 18)
    pygame.display.set_caption("Bismillah tubes kelar")

    mousex = 0
    mousey = 0


    button_color = BEFORECLICK
    alt_button_color = AFTERCLICK
    mouseOver = False
    isClicked = False

    card = pygame.image.load("Gambar/card.png")
    cardrect = card.get_rect(center=(100, 125))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                if mouseOver:
                    # Change the current color if button was clicked.
                    isClicked = not isClicked    
                    choice_arr = []
                    num_arr = []

                    str_card1 = str(random.randint(1,13)) + random.choice(arr_card)
                    choice_arr.append(str_card1)
                    card1 = pygame.image.load("Gambar/" + str_card1 + ".png")
                    num_arr.append(int(str_card1[:-1]))

                    str_card2 = str(random.randint(1,13)) + random.choice(arr_card)
                    while str_card2 in choice_arr : 
                        str_card2 = str(random.randint(1,13)) + random.choice(arr_card)
                    choice_arr.append(str_card2)
                    card2 = pygame.image.load("Gambar/" + str_card2 + ".png")
                    num_arr.append(int(str_card2[:-1]))

                    str_card3 = str(random.randint(1,13)) + random.choice(arr_card)
                    while str_card2 in choice_arr : 
                        str_card2 = str(random.randint(1,13)) + random.choice(arr_card)
                    choice_arr.append(str_card3)
                    card3 = pygame.image.load("Gambar/" + str_card3 + ".png")
                    num_arr.append(int(str_card3[:-1]))

                    str_card4 = str(random.randint(1,13)) + random.choice(arr_card)
                    while str_card4 in choice_arr : 
                        str_card4 = str(random.randint(1,13)) + random.choice(arr_card)
                    choice_arr.append(str_card4)
                    card4 = pygame.image.load("Gambar/" + str_card4 + ".png")
                    num_arr.append(int(str_card4[:-1]))
                    
                    tmp = num_arr[:]
                    Solve1(tmp)
                    tmp = num_arr[:]
                    Solve2(tmp)
                    

        mouseOver = cardrect.collidepoint(mousex, mousey)
        button_color = AFTERCLICK if isClicked else BEFORECLICK
        alt_button_color = BEFORECLICK if isClicked else AFTERCLICK

        DISPLAYSURF.fill(BGCOLOR)
        # Just draw the rect with the current button color.
        #pygame.draw.rect(DISPLAYSURF, button_color, myRectangle)
        DISPLAYSURF.blit(card, (rectX, rectY))

        if mouseOver:
            pygame.draw.rect(DISPLAYSURF, alt_button_color, cardrect, 3)

        if isClicked:
            
            num_card1 = myFont.render(str_card1[:-1], 1, WHITE)
            num_card2 = myFont.render(str_card2[:-1], 1, WHITE)
            num_card3 = myFont.render(str_card3[:-1], 1, WHITE)
            num_card4 = myFont.render(str_card4[:-1], 1, WHITE)

            DISPLAYSURF.blit(card1, [225, 200])
            DISPLAYSURF.blit(card2, [375, 200])
            DISPLAYSURF.blit(card3, [525, 200])
            DISPLAYSURF.blit(card4, [675, 200])
            
            DISPLAYSURF.blit(num_card1, (225, 420))
            DISPLAYSURF.blit(num_card2, (375, 420))
            DISPLAYSURF.blit(num_card3, (525, 420))
            DISPLAYSURF.blit(num_card4, (675, 420))

        pygame.display.update()
        FPSCLOCK.tick(30)

def determine_mouseOver(valx, valy):
    if myRectangle.collidepoint(valx, valy):
        return True
    else:
        return False

main()