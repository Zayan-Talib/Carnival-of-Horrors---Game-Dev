# The script of the game goes in this file.

# Transformations : Sprite Position

transform closeleft:
    xalign 0.38
    yalign 1.0

transform closeright:
    align 0.62
    yalign 1.0

transform slightleft:
    xalign 0.3
    yalign 1.0

transform slightright:
    xalign 0.7
    yalign 1.0

transform midleft:
    xalign 0.2
    yalign 1.0

transform midright:
    xalign 0.8
    yalign 1.0

transform left:
    xalign 0.1
    yalign 1.0

transform right:
    xalign 0.9
    yalign 1.0

transform extremeleft:
    xalign 0.0
    yalign 1.0

transform extremeright:
    xalign 1.0
    yalign 1.0

transform halfsize:

##############################################################################################

# Variables are used to make it less tedious to recall who is saying which line.
# Make sure character name colors are spelled "color" and not "colour"

define y = Character ("You", who_color = "#584747")
define p = Character ("Patty", who_color = "#59862e")
define b = Character ("Brad", who_color = "#503d19")


# Game starts here

label start:

    scene bg playground       # This is how to call scenes
    with fade                 # Transition

    show patty argue          # Calling a character sprite
    with dissolve       
        
    p "What do {i}you{/i} want to do?"    # This is how you italicize text in Ren'Py

    show patty argue at extremeleft
    with dissolve
    show brad argue at extremeright 
    with dissolve  

    b "I don't know, Patty. What do {i}you{/i} want to do?"

    p "Not fair, Brad. I asked you first."

    # Internal monologues can be written like this.

    "Patty and Brad. Your two best friends. Arguing. As usual."
    "It's the last week of August. And Patty and Brad haven't stopped fighting since your summer vacation started."
    "Patty likes being bossy. You don't mind, though. It's no big deal."
    "It's hard to win a fight with her anyway. You don't know why Brad even tries."
    "You guess it's because he doesn't want to look like a wimp in front of a girl."

    b "There's nothing to do. I guess I'll just go home."

    "You guess Brad is kind of a wimp - even if he is your best friend."

    p "You're so boring, Brad."

    "Whenever Patty complains, her freckles really pop out. Now there are about a million of them spread across her face"

    p "Hey! I know what we should do!"

    return