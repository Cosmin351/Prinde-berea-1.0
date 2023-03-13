import pygame
import random

pygame.font.init()
# Culori
White = (255, 255, 255)
Red = (255, 0, 0)
Cul = (100, 100, 100)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
GreenEnd = (50, 255, 0)
BlueStart = (50, 50, 255)

Latime = 1200
Inaltime = 600

Font = pygame.font.SysFont('freesanbold.ttf', 23)
Font2 = pygame.font.SysFont('freesanbold.ttf', 30)

# Poza
Coordpoze = (325, 55)
Nrpoza = 1

class Bere:
    y_speed = 5
    x_start = 10
    y_start = 10

    def __init__(self, x_start, y_start, y_speed):
        self.x_start = x_start
        self.y_start = y_start
        self.y_speed = y_speed
    def draw(self, ecran, x2, y2):
        img = pygame.image.load('Game data needed/bere.png')
        ecran.blit(img, (x2, y2))


class Lada:
    x_start = Latime//2
    y_start = 522
    x_speed = 0

    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start

    def draw(self, ecran, xL, yL):
        img2 = pygame.image.load('Game data needed/lada.png')
        ecran.blit(img2, (xL, yL))


class Scor:
    def __init__(self, x_start, y_start):
        self.x_scor = x_start
        self.y_scor = y_start

    def draw(self, ecran, b, v, n):
        Berri = Font.render('Beri prinse: ' + str(b), True, White)
        Vietti = Font.render('Vieti ramase: ' + str(v), True, White)
        Nivell = Font.render('Nivelul: ' + str(n), True, White)

        Text_Berri = Berri.get_rect()
        Text_Vietti = Vietti.get_rect()
        Text_Nivell = Nivell.get_rect()

        Text_Nivell.center = (925, 5)
        Text_Vietti.center = (945, 25)
        Text_Berri.center = (940, 45)

        ecran.blit(Nivell, Text_Nivell)
        ecran.blit(Vietti, Text_Vietti)
        ecran.blit(Berri, Text_Berri)


class Buton:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def draw(self):
        Iesire = Font2.render('Exit', True, Black, White)
        Dnou = Font2.render('Retry', True, Black, White)

        textIesire = Iesire.get_rect()
        textDnou = Dnou.get_rect()

        textDnou.center  = (Latime//2 - 30, Inaltime//2)
        textIesire.center = (Latime//2 + 35, Inaltime//2)

        ecran.blit(Dnou, textDnou)
        ecran.blit(Iesire, textIesire)


class PozaFemeie:
    def __init__(self, pospozax, pospozay):
        self.pospozax = pospozax
        self.pospozay = pospozay

    def draw(self, ecran, nr, lvl, coord):
        numeimg = ''
        if nr == 1:
            if lvl == 1:
                numeimg = 'Game data needed/F1p1.png'
            elif lvl == 2:
                numeimg = 'Game data needed/F1p2.png'
            elif lvl == 3:
                numeimg = 'Game data needed/F1p3.png'
            elif lvl == 4:
                numeimg = 'Game data needed/F1p4.png'
            elif lvl == 5:
                numeimg = 'Game data needed/F1p4.png'
        elif nr == 2:
            if lvl == 1:
                numeimg = 'Game data needed/F2p1.jpg'
            elif lvl == 2:
                numeimg = 'Game data needed/F2p2.jpg'
            elif lvl == 3:
                numeimg = 'Game data needed/F2p3.jpg'
            elif lvl == 4:
                numeimg = 'Game data needed/F2p4.jpg'
            elif lvl == 5:
                numeimg = 'Game data needed/special.jpg'

        imgf = pygame.image.load(numeimg)

        ecran.blit(imgf, coord)

pygame.init()


# Ecran
Marime = (Latime, Inaltime)
ecran = pygame.display.set_mode(Marime)
pygame.display.set_caption('Prinde berea, dezbraca femeia')
imgicn = pygame.image.load('Game data needed/iconmain.jpg')
pygame.display.set_icon(imgicn)
Exit = False
Exit2 = False
ForceExit = False
first = True


beri = []
beri.append(Bere(10, random.randrange(900), 6))


Ladda = Lada(Latime//2, 522)
blocat = 0


Scorr = Scor(900, 100)

Butoane = []
Butoane.append(Buton(Latime//2 - 60, Inaltime//2 + 10))
Butoane.append(Buton(Latime//2 + 40, Inaltime//2 + 10))

Poza = []

Poza.append(PozaFemeie(0, 0))
Poza.append(PozaFemeie(100, 100))

ceas = pygame.time.Clock()
x = 30
y = 40

# Scor
Vieti = 3
Nrberi = 0
Nivel = 1
Nrberitemp = 0
Nrberinivel = 5

G = False
while not Exit:
    Nrpoza =1
    Coordpoze = (125, 55)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xC = pos[0]
            yC = pos[1]
            if (125 < xC < 372) and (54 < yC < 554):
                Nrpoza = 1
                G = True
            if (725 < xC < 1020) and (45 < yC < 590):
                Nrpoza = 2
                G = True

    ecran.fill(BlueStart)
    if G:
        break
    for poze in Poza:
        poze.draw(ecran, Nrpoza, 1, Coordpoze)
        Coordpoze = (725, 45)
        Nrpoza += 1
    pygame.display.flip()

# Poza
Coordpoze = (925, 75)


while not Exit2:
    while not (Exit or ForceExit):
        if Vieti == 0 or Nivel == 5:
            Exit = True
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ForceExit = True
        ecran.fill((10, 100, 10))
        for i in beri:
            i.y_start += i.y_speed
            if i.y_start > Inaltime-157 and (i.x_start >= Ladda.x_start and i.x_start < Ladda.x_start + 163):
                Nrberi += 1
                Nrberitemp += 1
                i.y_start = 10
                i.x_start = random.randrange(600)
                if Nrberitemp == Nrberinivel:
                    Nrberinivel += 5
                    Vieti += Nivel//3
                    Nivel += 1
                    beri.append(Bere(random.randrange(600), random.randrange(50), random.randint(5, 8)))
                    Nrberitemp = 0
            elif i.y_start > Inaltime-80:
                Vieti -= 1
                i.y_start = 10
                i.x_start = random.randrange(600)


        for i in beri:
            i.draw(ecran, i.x_start, i.y_start)
        pos = pygame.mouse.get_pos()

        if 0 < pos[0] - 75 < Latime - Latime//4 - 172:
            Ladda.x_start = pos[0] - 75
            Ladda.draw(ecran, Ladda.x_start, Ladda.y_start)
        else:
            Ladda.draw(ecran, Ladda.x_start, Ladda.y_start)

        pygame.draw.rect(ecran, GreenEnd, (Latime - Latime//4 - 12, 0, Latime//4 + 12, Inaltime),0)
        Scorr.draw(ecran, Nrberi, Vieti, Nivel)
        Poza[Nrpoza-1].draw(ecran, Nrpoza, Nivel, Coordpoze)
        pygame.display.flip()
        ceas.tick(60)

    if ForceExit:
        break
    if first:
        first = False
        for i in Butoane:
            i.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit2 = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xB = pos[0]
            yB = pos[1]

            # Retry
            if ((Butoane[0].posx < xB < Butoane[0].posx + 55) and (y < Butoane[0].posy and yB > Butoane[0].posy - 20)):
                Exit = False
                first = True

                beri = []
                beri.append(Bere(10, 10, 4))

                blocat = 0

                Butoane = []
                Butoane.append(Buton(Latime // 2 - 60, Inaltime // 2 + 10))
                Butoane.append(Buton(Latime // 2 + 40, Inaltime // 2 + 10))

                Vieti = 3
                Nrberi = 0
                Nivel = 1
                Nrberitemp = 0
                Nrberinivel = 5

            # Iesire
            if ((615 < xB < 654) and (y < 310 and yB > 289)):
                    Exit2 = True
                    break
    pygame.display.flip()

pygame.quit()
