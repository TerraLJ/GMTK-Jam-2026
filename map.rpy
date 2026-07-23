#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

define tile_size = 16

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

    class MapTile:
        def __init__(self, occupant=None):
            self.occupant = occupant

    class MapDenizen:
        def __init__(self, x, y, img, width, height):
            self.x = x
            self.y = y
            self.img = img
            self.width = width
            self.height = height

        def getOffset (self):
            return (tile_size - self.width, tile_size - self.height)

    house_map = []

    #number of rows; i put a random number i'll be so deadass
    for i in range(7):
        new_row = []

        #number of columns
        for j in range (10):
            new_row.append(MapTile())
        house_map.append(new_row)

    gray_house = LandMap(house_map, "gray house indoors.png", 0, 0)

    #TODO: change this to fit the sprite dimensions. also idk why 5, 5

    gray_sprite = MapDenizen (5, 5, "gray", 15, 32)
    gray_house.occupy (5, 5, gray_sprite)