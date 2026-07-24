#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

define tile_size = 72
default moving_up = False
default moving_down = False
default moving_left = False
default moving_right = False

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
                return
            self.map[y][x].occupant = denizen

        def unoccupy (self, x, y):
            self.map[y][x].occupant = None
        
        def movePlayerDenizen(self, offx, offy):
            x = store.gray_sprite.x
            y = store.gray_sprite.y

            if self.isEmpty(x, y):
                return
            # Boundary checks
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return

            # Shift occupant grid values
            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y+offy][x+offx].occupant = denizen
            
            store.gray_sprite.x += offx
            store.gray_sprite.y += offy

            # Update engine camera mapping center vectors
            self.center_x = store.gray_sprite.x
            self.center_y = store.gray_sprite.y

            renpy.restart_interaction()

        def triggerInteraction (self, x, y):
            if (x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map)):
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

        def interact (self):
            self.interaction(self)

    # Building Map Matrices; j is x, i is y
    house_map = [[MapTile() for j in range(12)] for i in range(11)]
    town_map = [[MapTile() for j in range(51)] for i in range(34)]

    # Initializing Rooms with Camera matching Player (9, 5)
    gray_house = LandMap(house_map, "gray house indoors.png", 9, 5)
    town = LandMap(town_map, "town base.png", 13, 14)

    # Creating Player Instance
    store.gray_sprite = MapDenizen (9, 5, "gray", 72, 72, lambda d: None)
    gray_house.occupy (9, 5, store.gray_sprite)

    # Environment Blocks
    wall = MapOccupant (6, 10)
    gray_house.occupy (6, 10, wall)

    inside_house_door = MapDenizen (4, 10, "house door.png", 49, 49, leave_room)
    gray_house.occupy (4, 10, inside_house_door)

    #stupid wall implementation
    i = 0
    while (i < 25):
        town.occupy (13+i, 7, wall)
        town.occupy (13+i, 26, wall)
        i += 1

    j = 0
    while (j < 18):
        town.occupy (13, 8+j, wall)
        town.occupy (37, 8+j, wall)
        j += 1

    k = 0
    while (k < 7):
        l = 0
        while (l < 3):
            town.occupy (29 + k, 13 + l, wall)
            l+= 1
        k += 1

    m = 0
    while (m < 7):
        n = 0
        while (n < 3):
            town.occupy (18 + m, 14 + n, wall)
            n+= 1
        m += 1

    #hand coded wall blocks. pray for me
    town.occupy (14, 10, wall)
    town.occupy (14, 15, wall)
    town.occupy (14, 16, wall)

    town.occupy (14, 21, wall)
    town.occupy (15, 22, wall)
    town.occupy (16, 23, wall)
    town.occupy (17, 24, wall)
    town.occupy (18, 24, wall)
    town.occupy (19, 25, wall)
    town.occupy (20, 25, wall)
    town.occupy (21, 26, wall)
    town.occupy (22, 26, wall)
    town.occupy (23, 27, wall)
    town.occupy (24, 27, wall)

    #so you can kinda step inside the cave and triggers have room
    town.unoccupy (13, 12)
    town.unoccupy (13, 13)
    town.unoccupy (30, 15)
    town.unoccupy (24, 7)
    town.unoccupy (34, 7)
    town.unoccupy (23, 16)
    town.unoccupy (27, 26)

    cave = MapDenizen (23, 16, "house door.png", 49, 49, cave)
    town.occupy (12, 12, cave)
    town.occupy (12, 13, cave)

    outside_house_door = MapDenizen (23, 16, "house door.png", 49, 49, leave_room)
    town.occupy (23, 16, inside_house_door)

    lancer = MapDenizen (30, 15, "lancer.png", 72, 70, shop)
    town.occupy (30, 15, lancer)

    blacksmith = MapDenizen (24, 7, "lancer.png", 72, 70, blacksmith)
    town.occupy (24, 7, blacksmith)

    library_door = MapDenizen (34, 7, "lancer.png", 72, 70, library)
    town.occupy (34, 7, library_door)

    bridge = MapDenizen (27, 26, "lancer.png", 72, 70, bridge)
    town.occupy (27, 26, bridge)

    # FIX: Interaction tracking mapping engine logic
    def grayInteracts():
        x = store.gray_sprite.x
        y = store.gray_sprite.y
        
        if store.g_dir == "back": y -= 1
        elif store.g_dir == "front": y += 1
        elif store.g_dir == "left": x -= 1
        elif store.g_dir == "right": x += 1
            
        store.room.triggerInteraction(x, y)