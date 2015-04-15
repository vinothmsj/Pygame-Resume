""""
File contians
1. Class defnition
2. pygame implementation
3. logic for mousebuttondown, mouse pos
4. collide point
5. to call page implementation
"""
# logic for displaying on surface, mousebuttondown, mouse pos and call switch case for page change
import os
import sys
import pygame
from pygame.locals import *
from py_res import GetData

black = (0, 0, 0)


class MyResume:
	def __init__(self):
		self.get_data = GetData()
		
		pygame.init()
		pygame.display.set_caption('My resume')
		self.size = self.width, self.height = 900, 600
		self.screen = pygame.display.set_mode(self.size)
		

		# Fill background
		# import pdb; pdb.set_trace()
		self.text_area = pygame.Surface((self.width, self.height - 200))
		self.text_area = self.text_area.convert()
		self.text_area.fill(black)

		self.screen.fill((black))
		#self.add_buttons()
		self.font = pygame.font.SysFont("Verdana", 18)
		self.bigger_font = pygame.font.SysFont("Verdana", 24)
		self.page = 1

		# get content for first page
		self.update_screen(self.get_data(self.page))
		self.add_buttons()
		pygame.display.update()

	def add_buttons(self):
	
		self.button_forward = pygame.draw.rect(self.screen,
			(140, 240, 130), (self.width - 200, self.height - 100, 20, 20), 2)
		self.button_backward = pygame.draw.rect(self.screen,
			(140, 240, 130), (200, self.height - 100, 20, 20), 2)
		#pygame.display.update()


	def update_screen(self, data):
		myoutstring = data
		if type(data) == list:
		# if data is a list then create a string out of it
			myoutstring = "".join(data)
		
		text = self.font.render(myoutstring, 1, (255, 255, 0))
		textpos = text.get_rect()
		textpos.centerx = self.text_area.get_rect().centerx
		self.text_area.fill((black))
		self.text_area.blit(text, (textpos[0], 100, 0, 0))
		#self.update_page_no()
			# Blit everything to the screen
		self.screen.blit(self.text_area, (0, 0))
		pygame.display.flip()
	def main(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				# logic for forward button
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					text = pygame.mouse.get_pos()
					print text
					if self.button_forward.collidepoint(text):
						self.page = self.page + 1
					# logic for backward button
					elif self.button_backward.collidepoint(text):
						self.page = self.page - 1

					page_data = self.get_data(self.page)

					if page_data:
						# update screen
						self.update_screen(page_data)
					else:
						self.update_screen('Invalid page no')

if __name__ == '__main__':
	res = MyResume()
	res.main()
