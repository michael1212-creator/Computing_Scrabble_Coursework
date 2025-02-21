import pygame
import Button as Btn
import TextBox
import VisualObject as VO

# The abstract scene class which controls most events for a specific scene; I decided to have multiple scenes instead of multiple buttons, as doing this makes the process much easier and more intuitive.
class Scene:  
	def __init__(self, width, height, theme_colour = (237, 180, 127)):
		self.theme_colour = theme_colour
		self.surface = pygame.Surface((width, height))
		self.my_buttons = []
		self.my_visual_objects = []
		self.width = self.surface.get_size()[0]
		self.height = self.surface.get_size()[1]
		self.hidden_VOs = []
		self.uninteractive_VOs = []
		
	# Called when a specific event is detected in the loop.
	def ProcessInput(self, events):
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")

	# Called from the director and defined in the subclass.
	def Update(self):
		# Game logic would go here
		raise NotImplementedError("Update abstract method must be defined in subclass.")
	
	def AddButton(self, colour = (255, 255, 255), position = (0, 0), width = 50, height = 50, outline_colour = (0, 0, 0), text = "Btn", text_size = 20, text_colour = (0, 0, 0), fade_value = 20, button = None, hidden = False, interactive = True):
		if button == None:
			self.my_buttons.append(Btn.Button(colour, position, width, height, outline_colour, text, text_size, text_colour))
		else:
			self.my_buttons.append(button)
			if not (position is None):
				button.SetPosition(position)
		self.my_visual_objects.append(self.my_buttons[-1])
		if hidden:
			self.HideVO(self.my_buttons[-1])
		return self.my_buttons[-1]		
	
	def AddText(self, position = (0, 0), text = "", font_size = 30, font_family = "arial", text_colour = (0, 0, 0)):
		self.my_visual_objects.append(TextBox.TextBox(position, text, font_size, font_family, text_colour))
		return self.my_visual_objects[-1]	
	
	def AddVONonBtn(self, VO, pos = None, hidden = False, interactive = True):
		self.my_visual_objects.append(VO)
		if pos != None:
			VO.SetPosition(pos)
		if hidden:
			self.HideVO(VO)
		return self.my_visual_objects[-1]
		
	
	# Called when you want to draw the screen.
	def Draw(self):		
		self.BgColourDrawer()
		for visual_obj in self.my_visual_objects:
			if not (visual_obj in self.hidden_VOs):
				visual_obj.Draw(self.surface)
		pygame.display.get_surface().blit(self.surface, (0, 0))
		
		
	def HideVO(self, VO):
		if not VO in self.hidden_VOs:
			self.hidden_VOs.append(VO)		
	
	def DisplayVO(self, VO):
		if VO in self.hidden_VOs:
			self.hidden_VOs.remove(VO)		
		
	def MakeVOUninteractive(self, VO):
		if not VO in self.uninteractive_VOs:
			self.uninteractive_VOs.append(VO)	
	
	def MakeVOInteractive(self, VO):
		if VO in self.uninteractive_VOs:
			self.uninteractive_VOs.remove(VO)			
			
	def DisplayAndInteractiveVO(self, VO):
		self.MakeVOInteractive(VO)
		self.DisplayVO(VO)		
	
	def HideAndUninteractiveVO(self, VO):
		self.MakeVOUninteractive(VO)
		self.UndisplayVO(VO)		
		
	def MakeAllVOsUninteractive(self):
		for VO in self.my_visual_objects:
			self.MakeVOUninteractive(VO)			
			
	def MakeAllVOsInteractive(self):
		for VO in self.my_visual_objects:
			self.MakeVOInteractive(VO)			
			
	def HideAllVOs(self):
		for VO in self.my_visual_objects:
			self.HideVO(VO)
		
		
	# Similar to the one in director, but local to the Scene class, in case I want to change the colour
	def BgColourDrawer(self):
		self.surface.fill(self.theme_colour)
		
	
	# get the button which was clicked in the current frame; if no button was clicked, returns None
	def ButtonClicked(self):
		for btn in self.my_buttons:
			if not btn in self.uninteractive_VOs:
				btn.IsOver(pygame.mouse.get_pos())	

		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for btn in self.my_buttons:
					if btn.IsOver(pygame.mouse.get_pos()) and not btn in self.uninteractive_VOs:
						return btn
					
	def GetCentreCoordinates(self):
		return (self.surface.get_width() / 2, self.surface.get_height() / 2)
			
	def CentreVOOnPos(self, VO, position = None):
		if position is None:
			position = self.GetCentreCoordinates()
		VO.SetPosition((position[0] - 0.5 * VO.GetSize()[0], position[1] - 0.5 * VO.GetSize()[1]))
			
	"""
	def DisableAllVOs(self):
		for VO in self.my_visual_objects:
			if not VO in self.disabled_VOs:
				self.disabled_VOs.append(VO)
			
			
	def EnableAllVOs(self):
		self.disabled_VOs.clear()	
	"""
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			

						


