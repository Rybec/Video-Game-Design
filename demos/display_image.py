import pygame
import time

pygame.display.init()
screen = pygame.display.set_mode((800, 600))
back = pygame.image.load("stars.png")
george = pygame.image.load("george.png")
george_anim = {
	"down" : [(0, 48 * i, 48 ,48) for i in xrange(4)],
	"left" : [(48, 48 * i, 48 ,48) for i in xrange(4)],
	"up"   : [(96, 48 * i, 48 ,48) for i in xrange(4)],
	"right": [(144, 48 * i, 48 ,48) for i in xrange(4)]
}

run = True
frame = 0
while (run):
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run = False
		elif e.type == pygame.KEYUP:
			if ((e.key == pygame.K_F4) and
			   (e.mod and pygame.KMOD_ALT)):
				run = False

	screen.blit(back, (0, 0, 800, 600), (400, 100, 800, 600))
	screen.blit(george, (10, 10, 48, 48), george_anim["down"][frame])

	pygame.display.flip()				
	
	frame = (frame + 1) % 4

pygame.display.quit()
