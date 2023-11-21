# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# defining characters
define J = Character("Juila",color="#F400FF")
define R = Character("Renee", color= "#FF8700")
define Q = Character("Quol", color="#0094FF")


# defining bgs
image bg entrance = im.Scale("backgrounds/bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("backgrounds/bg_entrance_ticket.png", config.screen_width, config.screen_height)



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
    return

label Sorry:
    "sorry this character isn't avaabile for now, Juila is available though."
    jump Juila_Start
    return

label Juila_Start:
    window hide 
    pause 0.5 
    $ renpy.movie_cutscene("images/opening.webm")
    pause 1.0 
    window show
    J"""Aren't those agents?
    
    what are they doing here??"""
    return


