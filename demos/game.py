import  pygame

import graphics
import entity
import events

pygame.init()

graphics.init((400, 400))
george = entity.George()
graphics.add(george)

graphics.background = graphics.load("stars.png")

def quit(e):
	global run
	if (e.type == pygame.KEYUP):
		if (e.key == pygame.K_F4 and
		    e.mod & pygame.KMOD_ALT):
			run = False
	elif (e.type == pygame.QUIT):
		run = False

events.register(pygame.QUIT, quit)
events.register(pygame.KEYUP, quit)

events.register(pygame.KEYDOWN, george.key_handler)
events.register(pygame.KEYUP, george.key_handler)

clock = pygame.time.Clock()

run = True
while run:
	clock.tick(30)

	# event handling
	events.update()
	# game physics
	george.update()
	# rendering
	graphics.render()
	
pygame.quit()


