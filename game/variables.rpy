# Place to keep all variables and flags so they don't get redefined elsewhere

# player 0 is Grey, player 1 is Pink
default player = 0
default curseTransferCompleted = False

# Variables for when playing as Grey
default g_swordLevel = 0
default g_magicLevel = 0
default g_curseTransferDiscovered = False
default g_curseBreakDiscovered = False
default g_curseTransferObtained = False

# Variables for when playing as Pink
default p_swordLevel = 0
default p_magicLevel = 0
default p_curseTransferDiscovered = False
default p_curseBreakDiscovered = False
default p_curseTransferObtained = False

# Function to easily reset variables
init python:
    def resetVariables():
        g_swordLevel = 0
        g_magicLevel = 0
        g_curseTransferObtained = False
        p_swordLevel = 0
        p_magicLevel = 0
        p_curseTransferObtained = False
        # discoveries persist between runs
        return