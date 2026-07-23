label library:
    # shared start for entering library
    if curseTransferObtained and magicLevel >= 3:
        if player == 0:
            g "(I have everything I need now. I think I can cast the spell to transfer the curse...)"
            g "(...Should I do it?)"
        else:
            # TODO: rewrite for Pink?
            p "(I have everything I need now. I think I can cast the spell to transfer the curse...)"
            p "(...Should I do it?)"
        menu:
            "> This will take 1 action."

            "Transfer the curse.":
                $ curseTransferCompleted = True
                # TODO
                jump curseTransferEnding

            "Do not.":
                if player == 0:
                    jump library_g
                else:
                    jump library_p

label library_g:
    # library scenes when playing as Grey
    if not curseBreakDiscovered:
        # Has never studied in the library before
        g "(A library... Perhaps I could find something in here about the curse?)"
        menu:
            "> Search the library? Will take 1 action."

            "Look around.":
                g "(I combed through the library's vast collection, desperate for ANYTHING that might help my situation.)"
                g "(And...)"
                g "(I actually found something. An old spellbook, detailing a way to break any curse.)"
                g "(It's an advanced spell, unlike anything I've ever tried to cast before.)"
                g "(But... It might be my only hope. I just need to practice, starting now.)"
                "> Time passes..."
                "> Your magical ability leveled up! It is now level 1."
                python:
                    magicLevel = 1
                    g_curseBreakDiscovered = True
                    actionsLeft -= 1
                if actionsLeft <= 0:
                    jump endOfDay
            
            "Leave the library.":
                #TODO jump to overworld

    "(I'm still not good enough to break the curse... Should I practice my magic?)"
    menu:
        "> Practice magic? Will take 1 action."

        "Spend time practicing magic.":
            #
            $ actionsLeft -= 1
            if actionsLeft <= 0:
                jump endOfDay
        
        "Leave the library.":
            #TODO jump to overworld

label library_p:
    # library scenes when playing as Pink

label curseTransferEnding:
    "placeholder."