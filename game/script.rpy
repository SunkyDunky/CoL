# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# defining characters
define J = Character("Juila",color="#F400FF")
define R = Character("Renee", color= "#FF8700",image="Renee")
define Q = Character("Quol", color="#0094FF")
define L = Character("Layon", color= "#ff0000")
define LQ = Character("Lenorra", color="#00ff11")
define G = Character("Goon",color="#cacaca")

# define character sprites
image Renee sad:   
    "characters/Renee sad.png"
    zoom 0.5

# defining bgs
image bg entrance = im.Scale("backgrounds/bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("backgrounds/bg_entrance_ticket.png", config.screen_width, config.screen_height)
image bg stage = im.Scale("backgrounds/stage.png", config.screen_width, config.screen_height)

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
    "sorry this character isn't available for now, Juila is available though."
    jump Juila_Start
    return

label Juila_Start:
    window hide 
    pause 0.5 
    $ renpy.movie_cutscene("images/opening.webm")
    show bg stage
    pause 1.0 
    window show
    show Juila worried at center
    J"""Aren't those agents?
    
    what are they doing here??"""

    hide Juila worried

    show Goon at left with Dissolve(0.5)
    pause 1.0
    hide Goon with Dissolve(0.5)
    pause 0.5
    show Goon at right with Dissolve(0.5)
    pause 1.0
    hide Goon with Dissolve(0.5)
    pause 0.5
    show Goon at center with Dissolve(0.5)
    pause 1.0
    hide Goon with Dissolve(0.5)
   
    show Juila worried
    J"""This isn't a good sign..

    what should I do?"""

    menu:
        "what should I do?"
        "Warn my bandmates about them":
            jump J1
        "Ignore them and hope it doesn't worsen the situation":
            jump J2

    return

label J1:
    J"""I should tell them about this.
    
    Who should I warn first though..."""
    menu:
        "Who should I warn first though..."
        "Quol":
            jump JQ0
        "Renee":
            jump JR0

label J2:
    J"""I should ignore them...
    
    I think it would be okay, right?"""

    hide Juila worried

    show Goon at center with Dissolve(0.3)
    pause 0.5
    hide Goon with Dissolve(0.3)
    show Goon at center with Dissolve(0.3)
    pause 0.5
    hide Goon with Dissolve(0.3)
    show Goon at center with Dissolve(0.3)
    pause 0.5
    hide Goon with Dissolve(0.3)
    show Goon at center with Dissolve(0.3)
    pause 0.5
    hide Goon with Dissolve(0.3)

    J"""They... they are coming closer..
    
    I should do something...right?
    
    what do I do.."""

    menu:
        "what do I do.."
        "Stand my ground, don't move a muscle..":
            jump JQ0
        "I have to leave, I have to go!":
            jump JR0
