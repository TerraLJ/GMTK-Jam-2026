# Place to keep all variables and flags so they don't get redefined elsewhere

# player variable points to either the character g or p
default player = g
default curseTransferCompleted = False

# Variables that are shared across both characters because they reset
default swordLevel = 0
default magicLevel = 0
default timesMagicPracticed = 0
default curseTransferObtained = False

# Discovery flags are not reset across runs
default g_curseTransferDiscovered = False
default g_curseBreakDiscovered = False
default p_curseTransferDiscovered = False
default p_curseBreakDiscovered = False

# Day and action related variables
default day = 1
default actionsLeft = 5
default extraAction = False
# ^ Split extraAction into two variables for Day 2 and 3? So Pink/Grey
# can have extra comments on if you're taking care of yourself?

# Progression of interactions with Pink/Gray
default lovedOneProgression = 0

init python:
    def resetVariables():
        # Function to easily reset variables
        global swordLevel
        global magicLevel
        global timesMagicPracticed
        global curseTransferObtained
        global day
        global actionsLeft
        global extraAction
        global lovedOneProgression

        swordLevel = 0
        magicLevel = 0
        timesMagicPracticed = 0
        curseTransferObtained = False
        # discoveries persist between runs
        day = 1
        actionsLeft = 5
        extraAction = False
        lovedOneProgression = 0
        return

    def newDay():
        # sets up variables for the next day
        global day
        global actionsLeft
        global extraAction

        day += 1
        if day == 2:
            actionsLeft = 3
        elif day == 3:
            actionsLeft = 1
        else:
            actionsLeft = 0
        if extraAction:
            actionsDone += 1
        extraAction = False

    def updateMagic():
        # returns True if level up occurred
        global timesMagicPracticed
        global magicLevel
        
        timesMagicPracticed += 1
        if timesMagicPracticed == 1 and magicLevel < 1:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 2 and magicLevel < 2:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 4 and magicLevel < 3:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 6 and magicLevel < 4:
            magicLevel += 1
            return True
        elif timesMagicPracticed == 9 and magicLevel < 5:
            magicLevel += 1
            return True
        return False
