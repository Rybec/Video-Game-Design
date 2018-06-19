import pygame
#import pygame.image

resolution = None
screen = None
background = None
sprites = []
images = {}

def init(res):
	global resolution, screen
	resolution = res
	screen = pygame.display.set_mode(res)


def add(sprite):
	global sprites
	if sprite not in sprites:
		sprites.append(sprite)
		
def remove(sprite):
	global sprites
	if sprite in sprites:
		sprites.remove(sprite)
	
def render():	
	global screen, background
	screen.fill((0, 0, 0))
	
	screen.blit(background, (0, 0))
	
	for sprite in sprites:
		screen.blit(sprite.sprite,
		            (sprite.x, sprite.y),
					sprite.frame)
		
	pygame.display.flip()

def load(path):
	global images
	if path not in images:
		images[path] = pygame.image.load(path)

	return images[path]
		
		
