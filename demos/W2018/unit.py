import pygame

import graphics


class unit(object):
	def __init__(self, x, y):
			self.x = x
			self.y = y
			self.frame = 0.0
			
class George(unit):
	def __init__(self, x, y):
		super(George, self).__init__(x, y)
		self.spritesheet = graphics.load("george.png")
		self.mapping = {
			"down" : [(0, 48 * i, 48 ,48) for i in xrange(4)],
			"left" : [(48, 48 * i, 48 ,48) for i in xrange(4)],
			"up"   : [(96, 48 * i, 48 ,48) for i in xrange(4)],
			"right": [(144, 48 * i, 48 ,48) for i in xrange(4)]
		}
		self.facing = "up"
		self.speed = 0.2
		
	def update(self):
		self.frame = (self.frame + self.speed) % 4

	def render(self, surface):
		surface.blit(self.spritesheet,
		             (self.x, self.y, 48,48),
		             self.mapping[self.facing][int(self.frame)])
					 
	def handler(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				self.y -= 1
				if self.y < 0:
					self.y = 0
			elif event.key == pygame.K_DOWN:
				self.y += 1
				if self.y > (599 - 48):
					self.y = 599 - 48
			elif event.key == pygame.K_LEFT:
				self.x -= 1
				if self.x < 0:
					self.x = 0
			elif event.key == pygame.K_RIGHT:
				self.x += 1
				if self.x > (799 - 48):
					self.x = 799 - 48
				
					
