# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# defining
define e = Character("Eileen")
image bg entrance = im.Scale("bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("bg_entrance_ticket.png", config.screen_width, config.screen_height)

#selection screen
screen character_selection:
    vbox:
        xalign 0.5
        yalign 0.5
        hbox spacing 40:  # Add space between each option
            imagebutton:
                idle Transform("renee_opt.jpg", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("renee_opt.jpg", zoom=1.1)
                action Jump("Sorry")
            imagebutton:
                idle Transform("juila_opt.jpg", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("juila_opt.jpg", zoom=1.1)
                action Jump("Juila_Start")
            imagebutton:
                idle Transform("quol_opt.jpg", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("quol_opt.jpg", zoom=1.1)
                action Jump("Sorry")




# The game starts here.

label start:
    show bg entrance
    pause 4.0
    scene bg entrance_ticket
    with Dissolve(2.0)
    # Show your screen
    call screen character_selection
    with Fade(1.0,0.0,1.0)

    # $ renpy.movie_cutscene("movies/opening.mp4")

    return

label Sorry:
    "sorry this character isnt avaabile for now, Juila is available though."
    jump Juila_Start
    return

label Juila_Start:
    scene bg entrance_ticket
    with Fade(1.0,0.0,1.0)
    pause 1.0
    return
