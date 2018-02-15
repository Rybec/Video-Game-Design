import pygame

height = 800
width = 600

assets = {}

renderables = []

background = None

screen = None

def update():
	global screen, background, renderables
	
	screen.fill((0,0,0))
	
	if background:
		screen.blit(background, (0, 0, height, width))	
	
	for r in renderables:
		r.render(screen)

	pygame.display.flip()				

def register(renderable):
	global renderables
	if renderable not in renderables:
		renderables.append(renderable)

def remove(renderable):
	global renderables
	if renderable in renderables:
		renderables.remove(renderable)

		
def init():
	global screen
	pygame.display.init()
	screen = pygame.display.set_mode((height, width))

	
def load(file):
	global assets
	if file in assets:
		return assets[file]
	else:
		image = pygame.image.load(file)
		assets[file] = image
		return image
	
