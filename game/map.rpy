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
    town_map = [[MapTile() for j in range(33)] for i in range(26)]

    # Initializing Rooms with Camera matching Player (9, 5)
    gray_house = LandMap(house_map, "gray house indoors.png", 9, 5)
    town = LandMap(town_map, "town base.png", 13, 14)

    # Creating Player Instance
    store.gray_sprite = MapDenizen (9, 5, "gray", 72, 72, lambda d: None)
    gray_house.occupy (9, 5, store.gray_sprite)

    # Environment Blocks
    wall = MapOccupant (6, 10)
    gray_house.occupy (6, 10, wall)

    def self_op(denizen): pass
    def no_op(denizen): pass
    def disappear(denizen): room.unoccupy (denizen.x, denizen.y)
    def shop (denizen): renpy.jump("shopMenu")
    def library (denizen): pass
    def blacksmith (denizen): pass

    lancer = MapDenizen (3, 10, "lancer.png", 72, 70, shop)
    gray_house.occupy (3, 10, lancer)

    def leave_room (denizen):
        global room_name
        global room
        teleport_x = 0
        teleport_y = 0

        store.moving_up = False
        store.moving_down = False
        store.moving_left = False
        store.moving_right = False
        store.move = ""

        if room is not None:
            room.unoccupy(store.gray_sprite.x, store.gray_sprite.y)

        if (room_name == "gray_house"):
            room_name = "town"
            teleport_x = 14
            teleport_y = 12
        else:
            room_name = "gray_house"
            teleport_x = 9
            teleport_y = 5

        room = getattr(store, room_name)
        
        # FIX: Relocate the sprite position and map arrays correctly
        store.gray_sprite.x = teleport_x
        store.gray_sprite.y = teleport_y
        room.occupy(teleport_x, teleport_y, store.gray_sprite)
        
        # FIX: Align the room camera onto the fresh spawn coordinate location
        room.center_x = teleport_x
        room.center_y = teleport_y

        return True

    house_door = MapDenizen (4, 10, "house door.png", 72, 70, leave_room)
    gray_house.occupy (4, 10, house_door)

    # FIX: Interaction tracking mapping engine logic
    def grayInteracts():
        x = store.gray_sprite.x
        y = store.gray_sprite.y
        
        if store.g_dir == "back": y -= 1
        elif store.g_dir == "front": y += 1
        elif store.g_dir == "left": x -= 1
        elif store.g_dir == "right": x += 1
            
        store.room.triggerInteraction(x, y)