init python:
    house_map = [[MapTile() for j in range(14)] for i in range(15)]
    town_map = [[MapTile() for j in range(51)] for i in range(34)]

    gray_house = LandMap(house_map, "gray house indoors.png", 7, 8)
    town = LandMap(town_map, "town base.png", 13+buffer, 14+buffer)

    store.gray_sprite = MapDenizen (11, 1, "gray", 72, 144, lambda d: None)
    gray_house.occupy (11, 1, store.gray_sprite)

    store.pink_sprite = MapDenizen (8, 8, "pink", 72, 144, sibling)
    gray_house.occupy (8, 8, store.pink_sprite)

    wall = MapOccupant (0, 0)

    i = 0
    while (i < 14):
        gray_house.occupy (i, 0, wall)
        gray_house.occupy (i, 14, wall)
        i += 1

    #Bed walls
    gray_house.occupy (0, 1, wall)
    gray_house.occupy (1, 1, wall)
    gray_house.occupy (2, 1, wall)
    pink_bed = MapBuilding(3, 1, "pink bed.png", 288, 216, visual_h_tiles=3, interaction=no_op)
    gray_house.occupy (3, 1, pink_bed)

    gray_house.occupy (12, 1, wall)
    gray_house.occupy (12, 2, wall)
    gray_bed = MapBuilding(13, 2, "gray bed.png", 144, 288, visual_h_tiles=4, interaction=no_op)
    gray_house.occupy (13, 2, gray_bed)

    drawer = MapBuilding(11, 0, "window and drawer.png", 432, 144, visual_h_tiles=2, interaction=no_op)
    gray_house.occupy (11, 0, drawer)

    #wall walls
    gray_house.occupy (5, 4, wall)
    gray_house.occupy (8, 4, wall)
    bedroom_wall = MapBuilding(5, 1, "window and drawer.png", 72, 216, visual_h_tiles=3, interaction=no_op)
    gray_house.occupy (5, 1, bedroom_wall)
    gray_house.occupy (8, 1, bedroom_wall)

    j = 0
    while (j < 14):
        gray_house.occupy (j, 5, wall)
        j += 1

    shelf = MapDenizen (7, 14, "house door.png", 49, 49, shelf)
    k = 0
    while (k < 5):
        gray_house.occupy (k, 6, shelf)
        k += 1

    shelf = MapBuilding(5, 6, "shelf and plant.png", 432, 216, visual_h_tiles=3, interaction=no_op)
    gray_house.occupy (5, 6, shelf)

    #table
    gray_house.occupy (3, 9, wall)
    gray_house.occupy (4, 9, wall)
    gray_house.occupy (3, 10, wall)
    gray_house.occupy (4, 10, wall)
    gray_house.occupy (3, 11, wall)
    gray_house.occupy (4, 11, wall)
    gray_house.occupy (3, 12, wall)
    table = MapBuilding(4, 12, "dining table.png", 144, 360, visual_h_tiles=4, interaction=no_op)
    gray_house.occupy (4, 12, table)

    gray_house.occupy (0, 9, wall)
    gray_house.occupy (1, 9, wall)
    gray_house.occupy (1, 10, wall)
    gray_house.occupy (1, 11, wall)
    gray_house.occupy (1, 12, wall)
    gray_house.occupy (1, 13, wall)
    couch = MapBuilding(1, 13, "house couch.png", 144, 504, visual_h_tiles=6, interaction=no_op)
    gray_house.occupy (1, 13, couch)

    i = 0
    while (i < 7):
        gray_house.occupy (9, 8+i, wall)
        i += 1

    island = MapBuilding(9, 13, "kitchen island.png", 72, 504, visual_h_tiles=6, interaction=no_op)
    gray_house.occupy (9, 13, island)

    cupboards = MapDenizen (13, 14, "house door.png", 49, 49, cupboard)
    j = 0
    while (j < 8):
        gray_house.occupy (13, 6+j, cupboards)
        j += 1

    cupboard = MapBuilding(13, 11, "kitchen cabinets.png", 72, 504, visual_h_tiles=9, interaction=no_op)
    gray_house.occupy (13, 11, cupboard)
    #13, 14 is the end of the cupboards

    gray_house.unoccupy (6, 5)
    gray_house.unoccupy (7, 5)

    inside_house_door = MapDenizen (7, 14, "house door.png", 49, 49, leave_room)
    gray_house.occupy (6, 14, inside_house_door)
    gray_house.occupy (7, 14, inside_house_door)

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
    town.occupy (14+buffer, 11+buffer, wall)
    town.occupy (14+buffer, 16+buffer, wall)
    town.occupy (14+buffer, 17+buffer, wall)

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

    cave = MapDenizen (12+buffer, 12+buffer, "house door.png", 49, 49, cave)
    town.occupy (12+buffer, 12+buffer, cave)
    town.occupy (12+buffer, 13+buffer, cave)

    cave_front = MapBuilding(14+buffer, 17+buffer, "rock front.png", 432, 504, visual_h_tiles=7, interaction=no_op)
    town.occupy (14+buffer, 17+buffer, cave_front)

    house = MapBuilding(24+buffer, 16+buffer, "house outside.png", 216, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy(24+buffer, 16+buffer, house)

    building_1 = MapBuilding(19+buffer, 7+buffer, "building 1.png", 288, 216, visual_h_tiles=3, interaction=no_op)
    town.occupy(19+buffer, 7+buffer, building_1)

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

    church_library = MapBuilding (36+buffer, 7+buffer, "church library face", 648, 360, visual_h_tiles=5, interaction=no_op)
    town.occupy (36+buffer, 7+buffer, church_library)

    church_door = MapDenizen (29+buffer, 7+buffer, "house door.png", 49, 49, church)
    town.occupy (29+buffer, 7+buffer, church_door)

    outside_house_door = MapDenizen (23+buffer, 16+buffer, "house door.png", 49, 49, leave_room)
    town.occupy (23+buffer, 16+buffer, inside_house_door)

    npc_1 = MapDenizen (15+buffer, 11+buffer, "npc 1.png", 72, 70, npc_chat)
    town.occupy (15+buffer, 11+buffer, npc_1)