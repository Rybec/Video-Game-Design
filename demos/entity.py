import os

import pygame

import graphics

class Entity(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.sprite = None
		
class George(Entity):
	frames = {	
		"up":    [(2 * 48, y * 48, 48, 48)
		          for y in xrange(4)],
		"down":  [(0 * 48, y * 48, 48, 48)
		          for y in xrange(4)],
		"left":  [(1 * 48, y * 48, 48, 48)
		          for y in xrange(4)],
		"right": [(3 * 48, y * 48, 48, 48)
		          for y in xrange(4)],
	}
	def __init__(self):
		super(George, self).__init__()
		self.sprite = graphics.load(
			os.path.join("george.png")
		)
		self.frame = self.frames["down"][0]
		self.frame_num = 0
		self.facing = "down"
		self.speed = 0.5
		self.velocity = [0, 0]
		
	def update(self):
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		self.frame_num = (self.frame_num + self.speed * 0.25) % 4
		self.frame = self.frames[self.facing][int(self.frame_num)]
		
	def key_handler(self, e):
		if (e.type == pygame.KEYDOWN):
			if (e.key == pygame.K_UP):
				self.velocity[1] -= self.speed
				self.facing = "up"
			elif (e.key == pygame.K_DOWN):
				self.velocity[1] += self.speed
				self.facing = "down"
			elif (e.key == pygame.K_LEFT):
				self.velocity[0] -= self.speed
				self.facing = "left"
			elif (e.key == pygame.K_RIGHT):
				self.velocity[0] += self.speed
				self.facing = "right"
		elif (e.type == pygame.KEYUP):
			if (e.key == pygame.K_UP):
				self.velocity[1] += self.speed
			elif (e.key == pygame.K_DOWN):
				self.velocity[1] -= self.speed
			elif (e.key == pygame.K_LEFT):
				self.velocity[0] += self.speed
			elif (e.key == pygame.K_RIGHT):
				self.velocity[0] -= self.speed
	
		
		