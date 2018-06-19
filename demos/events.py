import pygame

listeners = {
	pygame.QUIT: [],
	pygame.KEYDOWN: [],
	pygame.KEYUP: [],
}

def register(type, handler):
	global listeners
	if handler not in listeners[type]:
		listeners[type].append(handler)


def update():
	global listeners
	for e in pygame.event.get():
		if e.type in listeners:
			for l in listeners[e.type]:
				l(e)