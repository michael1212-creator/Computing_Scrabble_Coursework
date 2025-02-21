import pygame
import TextBox
import Button as Btn		
	
class GLetterTile(Btn.Button):
	def __init__(
				self, 
				colour = (255, 255, 255),
				position = (0, 0),
				width = 50, 
				height = 50, 
				outline_colour = None, 
				text = "", 
				text_size = 20, 
				text_colour = (0, 0, 0), 
				fade_value = 20,
				is_active = True,
				outline_size = 4,
				point_worth = 0):

		super(GLetterTile, self).__init__(colour, position, width, height, outline_colour, text, text_size, text_colour, fade_value, is_active, outline_size)		
		
		self.point_text = TextBox.TextBox(
									(0, 0),
									point_worth,
									int(text_size / 2),
									'arial',
									text_colour
									)
		self.SetPointWorthTextPosition()
		
	# Similarly to other visual objects which contain other visual objects, this one also needs to set the position of the objects which it contains
	def SetPosition(self, position):
		super(GLetterTile, self).SetPosition(position)
		self.SetPointWorthTextPosition()
		
	# calculates the position for the point text
	def SetPointWorthTextPosition(self):
		self.point_text.SetPosition((self.position[0] + 2 * self.width / 3.4, self.position[1] + 2 * self.height / 3))		
	
	def Draw(self, surface):
		super(GLetterTile, self).Draw(surface)
		self.point_text.Draw(surface)		
		
	def __str__(self):
		return self.GetText()	
	
	def __int__(self):
		return int(self.point_text.GetText())		
	
	# If I want to change what a tile looks like, I can do so using this method. This is used when I am populating the (visual) rack
	def ChangeLooks(self, letter = None, point_worth = None, colour = None, outline_colour = None):
		if letter == None:
			letter = self.btn_text.GetText()
		if point_worth == None:
			self.point_text.GetText()
		if colour == None:
			colour = self.colour
		if outline_colour == None:
			outline_colour = self.outline_colour
		
		self.btn_text.SetText(letter)
		self.point_text.SetText(point_worth)
		self.colour = colour
		self.outline_colour = outline_colour				
		
	def GetPointWorth(self):
		return int(self.point_text.GetText())
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		