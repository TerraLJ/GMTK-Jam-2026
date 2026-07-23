init python:

    #that's me??? only add something if it's funny
    def self_op(denizen):
        pass

    #i'm not interacting with you
    def no_op(denizen):
        pass

    #i'm not interacting with you
    def disappear(denizen):
        room.unoccupy (denizen.x, denizen.y)

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
            room.unoccupy(gray_sprite.x, gray_sprite.y)

        if (room is not None and room_name == "gray_house"):
            room_name = "town"
            teleport_x = 13
            teleport_y = 14
        else:
            room_name = "gray_house"
            teleport_x = 9
            teleport_y = 5

        room = getattr(store, room_name)
        
        room.occupy (teleport_x, teleport_y, gray_sprite)

        renpy.show_screen("map_screen")

        renpy.run(Return())

    def shop (denizen):
        renpy.jump("shopMenu")

    def library (denizen):
        pass

    def blacksmith (denizen):
        pass

    def leave_rpg (denizen):
        global rpg
        rpg = False

        renpy.Return() 
