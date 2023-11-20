# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image bg entrance = im.Scale("bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("bg_entrance_ticket.png", config.screen_width, config.screen_height)


# The game starts here.

label start:

    show bg entrance
    pause 6.0
    scene bg entrance_ticket
    with Dissolve(2.0)
    pause 5.0
    with Fade(1.0,0.0,1.0)

    # $ renpy.movie_cutscene("movies/opening.mp4")

    menu Characterselection:
        "Choose a character"
        "Renee":
            jump Sorry
        "Julia":
            jump Juila_Start
        "Quol":
            jump Sorry
        

    return

label Sorry:
    "sorry this character isnt avaabile for now, Juila is available though."
    jump Juila_Start
    return

label Juila_Start:
    "yayayayaya"
    return
