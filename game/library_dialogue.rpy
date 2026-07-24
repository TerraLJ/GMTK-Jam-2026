label library:
    # shared start for entering library

    # TODO: set background image

    if curseTransferObtained and magicLevel >= 3:
        player "(I have everything I need now. I think I can cast the spell to transfer the curse...)"
        player "(...Should I do it?)"
        menu:
            "> This will take 1 action."

            "Transfer the curse.":
                $ curseTransferCompleted = True
                # TODO
                jump curseTransferEnding

            "Do not.":
                # if player == g:
                #     jump library_g
                # else:
                #     jump library_p
                # For now, just always jump to library_g
                jump library_g

label library_g:
    # library scenes when playing as Grey
    if not g_curseBreakDiscovered:
        # Has never studied in the library before
        player "(A library... Perhaps I could find something in here about the curse?)"
        menu:
            "> Search the library? This will take 1 action."

            "Look around.":
                player "(I combed through the library's vast collection, desperate for ANYTHING that might help my situation.)"
                player "(And...)"
                player "(I actually found something. An old spellbook, detailing a way to break even the strongest of curses.)"
                player "(It's an advanced spell, unlike anything I've ever tried to cast before.)"
                player "(But... It might be my only hope. I just need to practice, starting now.)"
                "> Time passes..."
                "> Your magical ability leveled up! It is now level 1."
                python:
                    magicLevel = 1
                    magicPracticeCount = 1
                    g_curseBreakDiscovered = True
                    actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay
            
            "Leave the library.":
                call screen map_screen

    player "(I'm still not skilled enough to break the curse... Should I practice my magic?)"
    menu:
        "> Practice magic? This will take 1 action."

        "Spend time practicing magic.":
            player "(I read through the book and practiced my control over casting spells.)"
            $  magicPracticeCount += 1
            if updateMagic(magicPracticeCount):
                player "(I really feel like I'm getting better!)"
                "> Your magical ability leveled up! It is now level [magicLevel]."
            else:
                player "(Progress was slower today. I'm still making some, but... It just never feels like enough.)"
                "> You will need to practice again before you can level up..."
            $ actionsLeft -= 1
            if magicLevel == 5:
                jump spellEnding
            if actionsLeft <= 0:
                jump endOfDay
        
        "Leave the library.":
            call screen map_screen

label library_p:
    # library scenes when playing as Pink

label curseTransferEnding:
    "placeholder."

label spellEnding:
    player "(I think... I think I've finally done it.)"
    player "(I understand the spell completely. I've honed my ability to wield my magic.)"
    player "(I can break the curse.)"
    player "(...)"
    player "-!? (When did it get so late!? I need to get home, now!)"
    # TODO add more