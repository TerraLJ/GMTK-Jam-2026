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
        if (room == gray_house):
            room = town

        else:
            room = gray_house

    def shop (denizen):
        renpy.jump("shopMenu")

    def library (denizen):
        pass

    def blacksmith (denizen):
        pass

    def leave_rpg (denizen):
        rpg = false
