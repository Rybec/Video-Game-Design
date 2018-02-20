import pygame

import graphics
import units

graphics.init()

import event


# back = graphics.load("stars.png")

graphics.background = graphics.load("stars.png")

george = units.George(25, 25)
george2 = units.George(100, 25)
george2.speed = 0.4
george2.facing = "left"

graphics.register(george)
graphics.register(george2)

def quit(e):
	global run
	if e.type == pygame.QUIT:
		run = False
	elif e.type == pygame.KEYUP:
		if ((e.key == pygame.K_F4) and
		   (e.mod and pygame.KMOD_ALT)):
			run = False
			
event.register(george.handler)
event.register(quit)

clock = pygame.time.Clock()
run = True
frame = 0
while (run):
	clock.tick(30)

	event.update()
	george.update()
	george2.update()
	graphics.update()
	

pygame.display.quit()
