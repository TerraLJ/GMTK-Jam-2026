#Grid/Tile Based
#character is centered, map moves
#interact key = item interact
#items are obstacles

define tile_size = 72
default moving_up = False
default moving_down = False
default moving_left = False
default moving_right = False
define buffer = 5

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
            # NEW: Keep self.y matched to the placement tile, but create a visual baseline
            self.sort_y = y + (visual_h_tiles - 1)
            self.interaction = interaction

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            if self.interaction:
                self.interaction(self)

    # Building Map Matrices; j is x, i is y
    house_map = [[MapTile() for j in range(12)] for i in range(11)]
    town_map = [[MapTile() for j in range(51)] for i in range(34)]

    # Initializing Rooms with Camera matching Player (9, 5)
    gray_house = LandMap(house_map, "gray house indoors.png", 9, 5)
    town = LandMap(town_map, "town base.png", 13+buffer, 14+buffer)

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
        town.occupy (13+i+buffer, 7+buffer, wall)
        town.occupy (13+i+buffer, 26+buffer, wall)
        i += 1

    j = 0
    while (j < 18):
        town.occupy (13+buffer, 8+j+buffer, wall)
        town.occupy (37+buffer, 8+j+buffer, wall)
        j += 1

    k = 0
    while (k < 7):
        l = 0
        while (l < 2):
            town.occupy (29 + k+buffer, 14 + l+buffer, wall)
            l+= 1
        k += 1

    m = 0
    while (m < 7):
        n = 0
        while (n < 2):
            town.occupy (18 + m+buffer, 15 + n+buffer, wall)
            n+= 1
        m += 1

    #hand coded wall blocks. pray for me
    town.occupy (14+buffer, 10+buffer, wall)
    town.occupy (14+buffer, 15+buffer, wall)
    town.occupy (14+buffer, 16+buffer, wall)

    town.occupy (14+buffer, 21+buffer, wall)
    town.occupy (15+buffer, 22+buffer, wall)
    town.occupy (16+buffer, 23+buffer, wall)
    town.occupy (17+buffer, 24+buffer, wall)
    town.occupy (18+buffer, 24+buffer, wall)
    town.occupy (19+buffer, 25+buffer, wall)
    town.occupy (20+buffer, 25+buffer, wall)
    town.occupy (21+buffer, 26+buffer, wall)
    town.occupy (22+buffer, 26+buffer, wall)
    town.occupy (23+buffer, 27+buffer, wall)
    town.occupy (24+buffer, 27+buffer, wall)

    #so you can kinda step inside the cave and triggers have room
    town.unoccupy (13+buffer, 12+buffer)
    town.unoccupy (13+buffer, 13+buffer)
    town.unoccupy (30+buffer, 15+buffer)
    town.unoccupy (24+buffer, 7+buffer)
    town.unoccupy (34+buffer, 7+buffer)
    town.unoccupy (23+buffer, 16+buffer)
    town.unoccupy (27+buffer, 26+buffer)
    town.unoccupy (29+buffer, 7+buffer)

    town.unoccupy(19+buffer, 7+buffer)
    town.unoccupy (24+buffer, 16+buffer)
    town.unoccupy (20+buffer, 16+buffer)
    town.unoccupy (35+buffer, 15+buffer)
    town.unoccupy (36+buffer, 7+buffer)
    town.unoccupy (26+buffer, 7+buffer)

    cave = MapDenizen (12+buffer, 12+buffer, "house door.png", 49, 49, cave)
    town.occupy (12+buffer, 12+buffer, cave)
    town.occupy (12+buffer, 13+buffer, cave)

    cave_front = MapBuilding(14+buffer, 17+buffer, "rock front.png", 432, 432, visual_h_tiles=6, interaction=no_op)
    town.occupy (14+buffer, 17+buffer, cave_front)

    house = MapBuilding(24+buffer, 16+buffer, "house outside.png", 216, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy(24+buffer, 16+buffer, house)

    # Change building_1 to look EXACTLY like this:
    building_1 = MapBuilding(19+buffer, 7+buffer, "building 1.png", 288, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy(19+buffer, 7+buffer, building_1)

    # Change building_2 to look EXACTLY like this:
    building_2 = MapBuilding(20+buffer, 16+buffer, "building 2.png", 216, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy(20+buffer, 16+buffer, building_2)

    shop_face = MapBuilding (35+buffer, 15+buffer, "store face.png", 512, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy (35+buffer, 15+buffer, shop_face)

    shop = MapDenizen (30+buffer, 15+buffer, "lancer.png", 72, 70, shop)
    town.occupy (30+buffer, 15+buffer, shop)

    blacksmith_face = MapBuilding (26+buffer, 7+buffer, "blacksmith face.png", 360, 288, visual_h_tiles=4, interaction=no_op)
    town.occupy (26+buffer, 7+buffer, blacksmith_face)

    blacksmith = MapDenizen (24+buffer, 7+buffer, "lancer.png", 72, 70, blacksmith)
    town.occupy (24+buffer, 7+buffer, blacksmith)

    library_door = MapDenizen (34+buffer, 7+buffer, "lancer.png", 72, 70, library)
    town.occupy (34+buffer, 7+buffer, library_door)

    bridge = MapDenizen (27+buffer, 26+buffer, "lancer.png", 72, 70, bridge)
    town.occupy (27+buffer, 26+buffer, bridge)

    church_library = MapBuilding (36+buffer, 7+buffer, "church library face", 648, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy (36+buffer, 7+buffer, church_library)

    church_door = MapDenizen (29+buffer, 7+buffer, "house door.png", 49, 49, church)
    town.occupy (29+buffer, 7+buffer, church_door)

    outside_house_door = MapDenizen (23+buffer, 16+buffer, "house door.png", 49, 49, leave_room)
    town.occupy (23+buffer, 16+buffer, inside_house_door)

    # FIX: Interaction tracking mapping engine logic
    def grayInteracts():
        x = store.gray_sprite.x
        y = store.gray_sprite.y
        
        if store.g_dir == "back": y -= 1
        elif store.g_dir == "front": y += 1
        elif store.g_dir == "left": x -= 1
        elif store.g_dir == "right": x += 1
            
        store.room.triggerInteraction(x, y)