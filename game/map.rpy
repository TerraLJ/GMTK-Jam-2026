#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

define tile_size = 16
define moving_up = False
define moving_down = False
define moving_left = False
define moving_right = False

init python:

    class LandMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty (self, x, y):
            return self.map[y][x].occupant is None
        
        def occupy (self, x, y, denizen):
            if not self.isEmpty (x, y):
                #then there's no room!
                return

            self.map[y][x].occupant = denizen

        #kill the occupant
        def unoccupy (self, x, y):
            self.map[y][x].occupant = None

        def moveDenizen (self, x, y, offx, offy):
            if self.isEmpty(x, y):
                return

            #if we run off the edge of map x-style
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return

            #if we run off the edge of map y-style
            if y + offy >= len(self.map) or y + offy < 0:
                return

            if not self.isEmpty(x + offx, y+offy):
                return

            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y+offy][x+offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy
            if self.center_x == x and self.center_y == y:
                self.center_x += offx
                self.center_y += offy

        def triggerInteraction (self, x, y):
            if (x < 0 or x >= len (self.map[0]) or y < 0 or y >= len (self.map)):
                return
            if (self.isEmpty (x, y)) or not isinstance(self.map[y][x].occupant, MapDenizen):
                return
            self.map[y][x].occupant.interact()

    class MapTile:
        def __init__(self, occupant=None):
            self.occupant = occupant

    class MapOccupant:
        def __init__ (self, x, y):
            self.x = x
            self.y = y

    class MapDenizen (MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x, y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        def getOffset (self):
            return (tile_size - self.width, tile_size - self.height)

        #TODO: different interacts for every individual. general solution here
        def interact (self):
            self.interaction(self)

    house_map = []

    #number of rows for the house
    for i in range(11):
        new_row = []

        #number of columns
        for j in range (12):
            new_row.append(MapTile())
        house_map.append(new_row)

    town_map = []

    #number of rows for the town
    for i in range(11):
        new_row = []

        #number of columns
        for j in range (12):
            new_row.append(MapTile())
        town_map.append(new_row)

    #TODO: change the center
    gray_house = LandMap(house_map, "gray house indoors.png", 4, 9)

    #TODO: change this to fit the sprite dimensions. also idk why 5, 5

    gray_sprite = MapDenizen (5, 9, "gray", 15, 32, self_op)
    gray_house.occupy (5, 9, gray_sprite)

    #TODO: make the walls fit the actual map. good luck. maybe use a for loop
    wall = MapOccupant (5, 10)
    gray_house.occupy (5, 10, wall)

    #TODO: interactables. lancer is my default
    lancer = MapDenizen (3, 10, "lancer.png", 72, 70, disappear)
    gray_house.occupy (3, 10, lancer)

    #TODO: Town layout
    town = LandMap(town_map, "town base.png", 4, 9)