import pygame
import Button as Btn	
import LetterTileHolder
import VisualObject as VO
import LetterTileHolder
		
class Board(VO.VisualObject):
	def __init__(self, horizontal_tile_num = 15, vertical_tile_num = 15, buffer_around_board = 4, tile_spacing = 2, width = 400, height = 400, position = (0, 0), board_colour = (0, 80, 0), tile_colour = (255, 255, 255)):
		super(Board, self).__init__(position)
		self.buffer_around_board = buffer_around_board
		self.board_colour = board_colour
		self.width = width
		self.height = height
		self.tile_spacing = tile_spacing
		self.buffer_around_board = buffer_around_board
		
		self.tile_height = (height - ((vertical_tile_num - 1) * (tile_spacing) + 2 * buffer_around_board)) / vertical_tile_num
		self.tile_width = (width - ((horizontal_tile_num - 1) * (tile_spacing) + 2 * buffer_around_board)) / horizontal_tile_num		

		# these are done in case the board isn't a square. It allows me to calculate size of text so it fits in the holder.
		shorter_side_length = min(self.tile_height, self.tile_width)
		text_size = round(0.49 * (shorter_side_length))
		
		first_holder_position_help = (position[0] + buffer_around_board, position[1] + buffer_around_board)
		self.tiles = [[LetterTileHolder.LetterTileHolder(
								colour = tile_colour, 
								position = (first_holder_position_help[0] + x * (self.tile_width + tile_spacing), first_holder_position_help[1] + y * (self.tile_height + tile_spacing)),
								width = self.tile_width,
								height = self.tile_height,
								outline_colour = (190, 190, 190),
								text = " ",
								text_size = text_size,
								text_colour = (0, 0, 0), 
								fade_value = 30,
								is_active = True,
								outline_size = 4) 
					  			for x in range(horizontal_tile_num)] for y in range(vertical_tile_num)]	
		
		# giving the visual representation the visual modifiers
		# this is just one octant, which is then just reflected many times to get all eight octants

		# triple letter modifier
		self.ChangeTileHolders((6, 0), "TL", (0, 235, 0))
		self.ChangeTileHolders((3, 3), "TL", (0, 235, 0))
		self.ChangeTileHolders((5, 5), "TL", (0, 235, 0))
		
		# double letter modifier
		self.ChangeTileHolders((2, 1), "DL", (0, 65, 205))
		self.ChangeTileHolders((4, 2), "DL", (0, 65, 205))
		self.ChangeTileHolders((6, 4), "DL", (0, 65, 205))
		
		# double word modifier
		self.ChangeTileHolders((5, 1), "DW", (235, 0, 0))
		self.ChangeTileHolders((7, 3), "DW", (235, 0, 0))
		
		# triple word modifier
		self.ChangeTileHolders((3, 0), "TW", (229, 148, 0))
		
		# starting position
		self.ChangeTileHolders((7, 7), "+", (198, 70, 198))
		
	
	# This method changes a tile in each octant;
	def ChangeTileHolders(self, relative_coords, text = "", colour = (255, 255, 255)):
		for x in [relative_coords[0], -(relative_coords[0] + 1)]:
			for y in [relative_coords[1], -(relative_coords[1] + 1)]:
				the_tile = self.tiles[y][x]
				the_tile.SetColour(colour)
				the_tile.SetText(text)		
				the_tile = self.tiles[x][y]
				the_tile.SetColour(colour)
				the_tile.SetText(text)
			
			
	def GetHolderAtPos(self, x, y):
		return self.tiles[y][x]
	
	# the SetPosition function isn't as simple as just adjusting the coordinates of the Board object itself; it onvolves also moving all of the holders that belong to the board, which is what this method does.
	def SetPosition(self, position):
		super(Board, self).SetPosition(position)
		first_tile_position_help = (position[0] + self.buffer_around_board, position[1] + self.buffer_around_board)
		for y, tiles_list in enumerate(self.tiles):
			for x, tile in enumerate(tiles_list):
				tile.SetPosition((first_tile_position_help[0] + x * (self.tile_width + self.tile_spacing), first_tile_position_help[1] + y * (self.tile_height + self.tile_spacing)))
		
	# this time ProcessInput() returns the TileHolder which was clicked.
	def ProcessInput(self, events):
		self.events = events
		return self.FindClickedTile()
	
	def GetTileSize(self):
		return (self.tile_width, self.tile_height)
	
	# finds the tile (and its relative coordinates) which was clicked ince the last frame (similar to the scene method which finds which button was clicked)
	def FindClickedTile(self):
		for tile_list in self.tiles:
			for tile in tile_list:
				tile.IsOver(pygame.mouse.get_pos())

		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for y, tile_list in enumerate(self.tiles):
					for x, tile in enumerate(tile_list):
						if tile.IsOver(pygame.mouse.get_pos()):
							return (tile, (x, y))
	
	def Draw(self, surface):
		pygame.draw.rect(surface, self.board_colour, (self.position, (self.width, self.height)),0)
		
		for tiles_list in self.tiles:
			for tile in tiles_list:
				tile.Draw(surface)
	
	
	
	
	
	
	
	
	
	
	
	
	
	