import pygame
import sys
import random

screen = pygame.display.set_mode((1250, 700))

hero = pygame.Rect(605, 655, 40, 40)
rx = 50
ry = 50

trawa = (0, 255, 0)
droga = (120, 120, 120)
woda = (92, 171, 224)
start = (28, 28, 28)
auto_c = (227, 72, 30)

ruch1 = 0.6
ruch2 = -0.8
ruch3 = -0.6

def rys_auta(x, y, szerokosc, los1, los2):
	licznik = 0
	auta = []
	for i in range(4):
		auto = pygame.Rect(x, y, szerokosc, 40)
		auta.append(auto)
		x += random.randint(los1, los2)
	return auta

def ruch_aut(auta, ruch, hero):
	for auto in auta:
		if pygame.Rect.colliderect(auto, hero):
			hero.x = 605
			hero.y = 655
			
		pygame.draw.rect(screen, auto_c, auto)
		
		auto.x -= ruch
		if auto.x <= -100 and ruch > 0:
			auto.x = 1250

		if auto.x >= 1350 and ruch < 0:
			auto.x = 0

auta1 = rys_auta(600, 555, 100, 340, 450)
auta2 = rys_auta(0, 505, 40, 320, 480)
auta3 = rys_auta(620, 405, 140, 600, 700)
auta4 = rys_auta(0, 305, 140, 600, 700)
auta5 = rys_auta(0, 255, 140, 600, 700)
auta6 = rys_auta(0, 155, 40, 320, 480)
auta7 = rys_auta(0, 105, 40, 320, 480)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

    	#sterowanie
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			hero.y -= ry
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			hero.y += ry
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			hero.x += rx
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			hero.x -= rx

    	#poza ekran
		if hero.y > 700:
			hero.y = 655
		if hero.y < 0:
			hero.y = 5
		if hero.x > 1250:
			hero.x = 1205
		if hero.x < 0:
			hero.x = 5
		if hero.y < 100:
			pygame.time.delay(500)
			pygame.quit()



	pygame.draw.rect(screen, trawa, (0, 0, 1280, 100))
	pygame.draw.rect(screen, droga, (0, 100, 1280, 100))
	pygame.draw.rect(screen, trawa, (0, 200, 1280, 50))
	pygame.draw.rect(screen, droga, (0, 250, 1280, 100))
	pygame.draw.rect(screen, trawa, (0, 350, 1280, 50))
	pygame.draw.rect(screen, droga, (0, 400, 1280, 200))
	pygame.draw.rect(screen, trawa, (0, 600, 1280, 50))
	pygame.draw.rect(screen, start, (0, 650, 1280, 50))
	pygame.draw.rect(screen, trawa, (0, 450, 1280, 50))

	ruch_aut(auta1, ruch1, hero)
	ruch_aut(auta2, ruch2, hero)
	ruch_aut(auta3, ruch1, hero)
	ruch_aut(auta6, ruch3, hero)
	ruch_aut(auta7, ruch1, hero)
	ruch_aut(auta4, ruch1, hero)
	ruch_aut(auta5, ruch3, hero) 
	

	pygame.time.delay(3)

	pygame.draw.rect(screen, (222, 154, 29), hero)
	pygame.display.flip()


