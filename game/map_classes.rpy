#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

define tile_size = 72
default moving_up = False
default moving_down = False
default moving_left = False
default moving_right = False
define repeat_input = 0.06
define buffer = 5

init python:
    class MapTile:
        def __init__(self, occupant=None):
            self.occupant = occupant

    class MapOccupant(object):
        def __init__ (self, x, y):
            self.x = x
            self.y = y
            self._sort_y = y 

        @property
        def sort_y(self):
            return self._sort_y

    class MapDenizen (MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x, y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        @property
        def sort_y(self):
            return self.y

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            self.interaction(self)

    class MapBuilding(MapOccupant):
        def __init__(self, x, y, img, width, height, visual_h_tiles=1, interaction=None):
            super(MapBuilding, self).__init__(x, y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction
            self._sort_y = y

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            if self.interaction:
                self.interaction(self)

    class LandMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty (self, x, y):
            return self.map[y][x].occupant is None
        
        def occupy (self, x, y, denizen):
            self.map[y][x].occupant = denizen

        def unoccupy (self, x, y):
            self.map[y][x].occupant = None
        
        def movePlayerDenizen(self, offx, offy):
            x = store.gray_sprite.x
            y = store.gray_sprite.y

            if self.isEmpty(x, y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return

            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y+offy][x+offx].occupant = denizen
            
            store.gray_sprite.x += offx
            store.gray_sprite.y += offy

            self.center_x = store.gray_sprite.x
            self.center_y = store.gray_sprite.y

            renpy.restart_interaction()

        def triggerInteraction (self, x, y):
            if (x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map)):
                return
            if (self.isEmpty (x, y)) or not isinstance(self.map[y][x].occupant, MapDenizen):
                return
            self.map[y][x].occupant.interact()

    def handle_character_input():
        """
        Returns a tuple: (should_move, dx, dy, target_dir) or None
        """

        if moving_up: target, dx, dy = "back", 0, -1
        elif moving_down:  target, dx, dy = "front", 0, 1
        elif moving_left:  target, dx, dy = "left", -1, 0
        elif moving_right: target, dx, dy = "right", 1, 0
        else:
            return None

        if g_dir == target:
            return (True, dx, dy, target)
        
        return (False, 0, 0, target)

    def grayInteracts():
        x = store.gray_sprite.x
        y = store.gray_sprite.y
        
        if store.g_dir == "back": y -= 1
        elif store.g_dir == "front": y += 1
        elif store.g_dir == "left": x -= 1
        elif store.g_dir == "right": x += 1
            
        store.room.triggerInteraction(x, y)