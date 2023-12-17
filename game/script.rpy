# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#setting
default hp = 15
default haveAndrew = False

# defining characters
define J = Character("Julia",color="#F400FF")
define R = Character("Renee", color= "#FF8700")
define Q = Character("Quol", color="#0094FF")
define A = Character("Andrew", color= "#ff0000")
define LQ = Character("Lenorra", color="#00ff11")
define G1 = Character("Agent1",color="#cacaca")
define G2 = Character("Agent2",color="#cacaca")
define A1 = Character("Audience1",color="#cacaca")
define A2 = Character("Audience2",color="#cacaca")
define L = Character("Lars",color="#fcff2e")
define Z = Character("A spectator?",color="#6303ff")
define JM = Character("Ms. Sylvia Ely",color="#6337ab")
define JF = Character("Mr. Sylvia Ely",color="#563a82")

# define character sprites
#Renee
image Renee :   
    "characters/Renee.png"
    zoom 0.49
image Renee worried:   
    "characters/Renee worried.png"
    zoom 0.49  
image Renee smile:   
    "characters/Renee smile.png"
    zoom 0.49
image Renee alt:   
    "characters/Renee alt.png"
    zoom 0.49
image Renee alt worried:   
    "characters/Renee alt worried.png"
    zoom 0.49  
image Renee alt smile:   
    "characters/Renee alt smile.png"
    zoom 0.49    
#Julia        
image Julia :   
    "characters/Julia-half.png"
    zoom 0.2
image Julia nervious:   
    "characters/Julia-half nervious.png"
    zoom 0.2    
image Julia traumatized:   
    "characters/Julia-half traumatized.png"  
    zoom 0.2
image Julia exhausted:   
    "characters/Julia-half exhausted.png"  
    zoom 0.2
image Julia alt:   
    "characters/Julia-half alt.png"
    zoom 0.2
image Julia alt nervious:   
    "characters/Julia-half alt nervious.png"
    zoom 0.2    
image Julia alt traumatized:   
    "characters/Julia-half alt traumatized.png"  
    zoom 0.2
image Julia alt exhausted:   
    "characters/Julia-half alt exhausted.png"  
    zoom 0.2
image Julia raincoat:   
    "characters/Julia-half raincoat.png"
    zoom 0.2
image Julia raincoat nervious:   
    "characters/Julia-half raincoat nervious.png"
    zoom 0.2    
image Julia raincoat traumatized:   
    "characters/Julia-half raincoat traumatized.png"  
    zoom 0.2
image Julia raincoat exhausted:   
    "characters/Julia-half raincoat exhausted.png"  
    zoom 0.2        
#Quol    
image Quol :   
    "characters/Quol.png"
    zoom 1.59
image Quol Angry:   
    "characters/Quol Angry.png"
    zoom 1.78
image Quol raincoat:   
    "characters/Quol raincoat.png"
    zoom 1.59
image Quol raincoat Angry:   
    "characters/Quol raincoat Angry.png"
    zoom 1.78    
#Lenorra    
image Lenorra:   
    "characters/Lenorra.png"
    zoom 0.5  
#Andrew    
image Andrew:   
    "characters/Andrew.png"
    zoom 0.5    
#Agent    
image Agent1:   
    "characters/Agent.png"
    zoom 0.5
image Agent2:   
    "characters/Agent.png"
    zoom 0.5
#Lars    
image Lars:   
    "characters/Lars.png"
    zoom 0.5

# defining bgs
image bg entrance = im.Scale("backgrounds/bg_entrance.png", config.screen_width, config.screen_height)
image bg entrance_ticket = im.Scale("backgrounds/bg_entrance_ticket.png", config.screen_width, config.screen_height)
image bg stage = im.Scale("backgrounds/stage.png", config.screen_width, config.screen_height)
image bg greenroom = im.Scale("backgrounds/greenroom.png", config.screen_width, config.screen_height)
image bg toilet = im.Scale("backgrounds/toilet1.png", config.screen_width, config.screen_height)
image bg ReneeBedroom = im.Scale("backgrounds/ReneeBedroom.jpg", config.screen_width, config.screen_height)
image bg Hotelalley = im.Scale("backgrounds/HotelAlley.png", config.screen_width, config.screen_height)
image bg black = im.Scale("backgrounds/black.png", config.screen_width, config.screen_height)

# define other images
image Renee bag :   
    "Renee bag.png"
    zoom 0.3

#transform
transform right_center_lower:
    xalign 0.75
    ypos 0.15
transform left_center_lower:
    xalign 0.25
    ypos 0.15
transform center_lower:
    xalign 0.5
    ypos 0.15
transform textbox_over:
    xalign 1
    ypos 0.54

#disclaimer
label splashscreen:
        show text """Disclaimer

        This demo of Concert of Liberation is a work in progress and intended solely as a test of concept. Please be aware that all content within this demo is unfinished and may not represent the final quality or features of the intended game. Bugs, glitches, and incomplete elements are expected. Your feedback and insights are highly appreciated as they will help us improve and shape the final product. Thank you for participating in this early stage of development."""with dissolve 
        pause 5.0
        hide text with dissolve
        return

#selection screen
image bg entrance_ticket_dark = im.Scale("backgrounds/bg_entrance_ticket_dark.png", config.screen_width, config.screen_height)
screen character_selection:
    vbox:
        xalign 0.5
        yalign 0.5
        hbox spacing 40:  # Add space between each option
            imagebutton:
                idle Transform("ticket_Renee.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Renee.png", zoom=1.1)
                action Jump("Sorry")
            imagebutton:
                idle Transform("ticket_Julia.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Julia.png", zoom=1.1)
                action Jump("Julia_Start")
            imagebutton:
                idle Transform("ticket_Quol.png", size=(config.screen_width / 5, config.screen_height * 2 / 3), zoom=1.0)
                hover Transform("ticket_Quol.png", zoom=1.1)
                action Jump("Sorry")
    text "{b}Choose a Character{/b}" size 40 align (0.5, 0.93)  # Add title at the bottom of the screen

#timer
default downer = 0

screen timerDown(rangeD, missed_event):
    on "show" action SetVariable("downer", rangeD)
    frame:
        xalign 0.5
        yalign 0.1
        hbox:
            timer 0.1 action If(0 < downer, true = SetVariable("downer", downer - 0.1), false = [Hide("timerDown"), Jump(missed_event)]) repeat True
            hbox:
                xalign 0.5
                bar:
                    value AnimatedValue(value=downer, range=rangeD, delay= 0.1)
                    yalign 0.0
                    xmaximum 500
                    bar_invert True
                    right_bar "gui/bar/left.png"
                    left_bar "gui/bar/right.png"
                    ysize 10  # Adjust this value to change the thickness of the bar
                bar:
                    value AnimatedValue(value=downer, range=rangeD, delay= 0.1)
                    yalign 0.0
                    xmaximum 500
                    ysize 10  # Adjust this value to change the thickness of the bar            

# QTE choice screen
screen qte_choice(items):
    style_prefix "qte"
    zorder 1
    for i in items:
        frame:
            xalign i[2]  # Adjust this to move the box horizontally
            yalign i[3]  # Adjust this to move the box vertically
            has vbox:
                textbutton "{size=-10}" + i[0] + "{/size}"xalign 0.5 action [Hide("timerDown"), Jump(i[1])] style "qte_button"

#temp hp screen
screen display_hp:
    text "HP: [hp]" xpos 0.1 ypos 0.1

#Illustrations
image JS1FS = im.Scale("CG/JS1FS.png", config.screen_width, config.screen_height)
image JS11 = im.Scale("CG/JS11.png", config.screen_width, config.screen_height)



# The game starts here.

label start:
    show bg entrance
    pause 2.0
    scene bg entrance_ticket_dark with Dissolve (3.0)
    pause 0.5
    call screen character_selection
    with Fade(1.0,0.0,1.0)
    return

label Sorry:
    "sorry this character isn't available for now, Julia is available though."
    jump Julia_Start
    return

label Julia_Start:
    window hide 
    pause 1.0 
    play music "Audio/Athena.mp3"
    play movie "images/opening.webm"
    show bg stage
    pause 1.0 
    window show
    show Julia at textbox_over
    $ renpy.pause(23, hard=True)
    J"(In the crowded and noisy venue, I find myself standing above the stage, my fingers absentmindedly gripping the neck of my guitar.)"

    stop music fadeout 20.0

    J"""(The vibrant lights and pulsating music create a whirlwind of sensory overload around me, but my senses are suddenly numbed as my gaze lands on a familiar figure.)

    (Standing at the back of the venue are two enigmatic individuals, dressed in sleek white suits, their presence sending a jolt of disbelief through my core.)"""

    hide Julia

    # Fade in the new music over 5 seconds
    play music "StageBGM.mp3" fadein 10.0

    show Agent1 at left_center_lower with Dissolve(0.5)
    show Agent2 at right_center_lower with Dissolve(0.5)
    show Lenorra at Transform (yalign=5.5, xalign=0.5) with Dissolve(0.5)

   
    J"""(I can barely comprehend what I'm seeing.)

    (The agents from NewFutures Institute have infiltrated this concert.)

    (The music continues to blast through the air, but the sounds fade into the background as my focus narrows solely on the ominous figures before me.)

    (Everything seems to move in slow motion as the spotlight illuminates the agents.)

    (Their presence looms over the crowd, casting a shadow of unease and uncertainty within me.)

    (Emotionally stunned, I struggle to find my footing.)

    (Thoughts race through my mind, but clarity eludes me.)

    (This isn't a good sign.)"""

    hide Agent1
    hide Agent2
    hide Lenorra
    
    jump J2

    return

label J1:
    J"""I should tell them about this.
    
    Who should I warn first though..."""
    show Julia at textbox_over
    "a"
    show Julia nervious at textbox_over
    "a"
    show Julia traumatized at textbox_over
    "a"
    show Renee at center_lower
    "a"
    show Renee worried at center_lower
    "a"
    show Renee smile at center_lower
    "a"
    show Quol at center_lower
    "a"
    show Quol Angry at center_lower
    "a"

    show screen timerDown(3, "missedit")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Timed choice 1", "choice1", 0.2, 0.3),  # xpos and ypos for choice 1
        ("Timed choice 2", "choice2", 0.8, 0.7)   # xpos and ypos for choice 2
    ])
    return

label missedit:
    "I missed it..."
    jump finished

label choice1:
    "I picked choice 1. It was ok I guess."
    jump finished

label choice2:
    "I picked choice 2. It was ok I guess."
    jump finished

label finished:
    "And we're done"
    return
    menu:
        J"Who should I warn first though..."
        "Quol":
            jump JQ0
        "Renee":
            jump JR0


#J2-Julia self routes
label J2:
    show Julia nervious at textbox_over
    J"""(I ignore the agents, not wanting to deal with any confrontations.)

    I should just ignore them...

    (I mutter to myself, trying to convince myself that everything will be fine if I simply pretend they're not there.)"""
    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)
    pause 0.5
    hide Agent1 with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(But as one of the agents takes a step closer, my heart leaps into my throat, and my previous confidence wavers.)

    They... they are coming closer...

    (I stammer, my voice barely above a whisper.)

    (Panic starts to grip me, and my mind races, desperately searching for a solution.)

    I should do something... right?"""


    menu:
        J"What do I do.."
        "Stand my ground, don't move a muscle..":
            jump JS0
        "I have to leave, I have to go!":
            jump JH0

label JS0:
    # agent tries dragging her
    show Julia nervious at textbox_over
    J"(As I was frozen in fear, I was caught off guard by the agent suddenly lunging at me from below the stage)"
    hide Julia
    show Agent1 at Transform(xalign=0.5, yalign=0.1, zoom=1.5)
    
    J"""(Panic courses through my veins as their grip tightens around my leg, threatening to drag me off the stage.)
    
    {b}{i}Aaaah!{/i}{/b}

    (My instinct kicks in, overriding my initial shock.)

    (With every ounce of strength I can muster, I fight against the agent's grip, desperately wriggling and twisting in an attempt to break free.)

    "I have to back up! I have to back up!"

    (With a blend of panic and a hint of newfound determination, I felt a surge of adrenaline.)

    (It fuels my movements as I manage to loosen the agent's hold.)

    (Stumbling backwards, I narrowly escape being pulled off the stage, my heart pounding in my chest.)"""

    hide Agent1 with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(The sudden commotion disrupted the liveliness of the concert, a deafening silence)

    (The crowd errupted as people were panicking from the chaotic scene unfolding before them.)"""
    hide Julia
    A1"It's The Institute!"
 
    A2"Wha- Why would The Institute be here?"

    show Julia nervious at textbox_over

    J"""(Amidst the confusion, I strain to catch snippets of their conversations, hoping to glean some understanding of the situation.)

    (However, before I can piece together the puzzle, the agents, realizing that their presence has been exposed, yells out to the audience.)"""

    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)

    G1"{b}CIVILLIANS, PLEASE EXIT THE VENUE!!!{/b}"

    hide Agent1 with Dissolve(0.3)

    show Julia exhausted at textbox_over
    
    J"""(The audience, rushes and funnels out the exit like a frantic river, leaving us alone with the agents in the hall.)

    What... what just happened? 

    (Sweat trickles down my forehead, my hands trembling uncontrollably.)"""

    hide Julia

    show Quol Angry at left_center_lower with Dissolve(0.3)
    show Renee worried at right_center_lower with Dissolve(0.3)

    J"(Quol and Renee, tightly grasping their instruments, finally speaks up)"

    R "I...It's them, I did everything they wanted, why are they here?"

    J"(Her voice trembling mildly, her hands shakingly reaches for her whip.)"

    Q"These fuckers again!!"
    
    J"(Quol barked at the infiltrators in frustration)"
    
    Q"Don't you DARE lay a finger on any of us!"

    J"""(Her voice now raspy and laced with anger, she pulls up her sleeves in preperation.)

    (I find myself at the back of the stage, overwhelmed and at a loss for words.)

    (My eyes darted between the chaotic scene unfolding before me and the unwavering bravery of Quol.)

    (It's in this moment, that I realize I must do something other than stay in this vulnerable position.)"""

    menu:
        J"I'm hyperventilating.."
        "I should snap out of it":
            jump JS1
        "Run..I have to leave!":
            hide Renee
            hide Quol
            jump JH0

label JH0:
    show bg black with fade
    J"(As panic grips my racing mind, I sprint towards the backstage area, my breath coming in ragged gasps.)"
    show bg stage 
    show Julia traumatized at textbox_over
    J"(I am hiding at the backstage shaking as I am filled with fear)"
    J"..."
    J"(I take a deep breathe, the agents haven't found me yet)"
    J"I should calm down... they are not here yet." 
    J"(I take deep breaths trying to be at ease)"
    J"They are not here yet..."
    J"But..."
    J"The agents...why are they back again... did they track me somehow?" 
    J"(I hear the agents moving in the background as they tear apart the stadium looking for me. Calming down might get me captured... I... I don't want to go back to there)"
    J" ...No..."
    J"(I shake my head prolonging a mental tailspin)"
    J"""
    Haha... 
    We are safe here... we must be, right Quol? 
    """
    pause 1
    J"Quol?"
    pause 5
    J"""(I looked around the room.)
    
    (My face fills with dread)"""
    J"(No...)"
    J"Renee?"
    pause 5
    J"(I looked around the room again, eyes widening more by every second.)"
    J"Renee isn't here either..."  
    J"(I can feel my heart beginning to beat out of my chest upon realizing...)"
    pause 5
    J"{/b}'I am alone...'{/b}"
   
    J"""(Breaths accompany my slow steps and the sudden truth that I've left my friends alone.)
    
    (The weight of everything is beginning to be too heavy to bear.)
    
    (I feel uneasy)"""
    #heartbeat sfx

    J"(The agents... I hear them approaching backstage. My body flinches, almost moving on its own as I fall over)" 
    play music "Fear_And_Terror.mp3"
    J"No... they'll find me... I... I don't want to go back there"
    J"(There is little time before the agents catch me. The urgency of the situation suddenly propels me forward, my heart now pounding in my chest. I run for a way out)"
    J"...I have to hide..." 
    J"""(Amidst the chaos and confusion, two options dominate my thoughts like beacons of fleeting respite. 
    
    (I stand between two doors, the green room or the toilets.)
    
    (Which way do I go?)"""


    menu:
        J"(Which way do I go?)"
        "Green Room":
            J"I have to go, I have to go!"
            jump JS2
        "Toilet":
            jump JH1    

label JH1:
    show bg toilet 
    show Julia at textbox_over with Dissolve(0.3)
    J"(I hold the bathroom door shut so the agents don't come in, then take a few steps back when my surroundings momentarily feel silent.)"

    J"Are they gone? They shouldn't know I'm here? But what do I do now—"

    J"(I clutch my head, it is throbbing. These moments of running away feel familiar...)"

    J"(Thoughts of  the NewFutures Institute slowly flooded my mind with experiences I don't want to recall.)"
    show bg black with fade
    #(Story Beat 1 Part 1)
    J"..."
    show Lenorra at center_lower with Dissolve(0.3)
    LQ"""This is her right? 

    (Lenorra's colleagues nod and promptly scatter, preparing an operation room for memory extraction.)"""

    J """(Lenorra smiles a little as she turns towards me.)
    
    (The intent in her gaze as she eyes me causes me to shiver. )
    
    (She kneels so that we are face to face, her faint smile fills me with terror.)

    (Lenorra scoffs...)"""

    LQ"""Julia... What is with that face? 
    
    Oh I understand now, you must be confused..."""

    J"(Lenorra's smile fades for a moment as she puts her hand on my shoulder.)"

    J"""(I want to say something to her but a choking feeling dwelling in my throat silences the courage I once had.)
    
    (That courage fails to escape me as a swallow with difficulty.)"""

    LQ"Be not afraid my child, you are the key to a potential breakthrough that will change the future as we know it..."

    J"..."

    J"(Lenorra's gaze lingers as she scrutinizes me. She rubs my forehead for a brief moment before locking eye contact with me again.)"

    LQ"""This may be the last time we speak Julia, but I understand how you feel. 
    
    Dwelling in a society where you don't know your true purpose in life can only worsen when your presence remains unknown and ignored by those closest to you..."""

    J"""(Lenorra's speech was soft but somber.)
    
    (Her feelings of hope didn't reflect the dull surroundings of the Institute where I was seated...) 

    (...At that moment, what Lenorra had said was true, and because of this, she radiated as light I felt a temporary warmth in.)
    
    (Though I still shook where I sat. Something was missing...)"""

    hide Lenorra with Dissolve(0.3)
    show bg toilet with fade
    #(Transition back to reality)

    J"""(I am standing facing the bathroom door... That was a moment I experienced from the Institute)

    (I start to think to myself... Lenorra was always interested in my mind... she never saw me as a person...)

    (Footsteps can be heard rushing past the bathroom)

    !!!

    Sooner or later they will capture me... and those memories will become reality over again...

    (My eyes widen in fear as my pupils jitter... I am reminded of that lingering pain from my past)

    I don't want to go back to the institute... I don't want to leave this life behind...

    ...

    (I begin to lose balance, my body fighting to maintain control over my anxious thoughts)"""

    LQ"A crucial flaw to the human mind is its independence..."

    J"(I hear Lenorra's voice in my head again... I tear up as I lean against the wall)"
    show bg black with fade
    #(Transition back to story beat)

    J"(Lenorra lets out a soft chuckle as she sits beside me now... I am confused, it felt like Lenorra knew more than she let on...)"

    LQ"""The Amanita muscaria lacks this flaw. It is an example of why I adore fungi. 
    
    Just the ability alone to share thoughts and form a hivemind means that no mushroom is left alone in isolation by its kin..."""

    J"...what? "

    J"(I recall another moment from the Institute... one that gives my throat a constricting feeling)"

    LQ"""...now imagine if we adapted that trait onto the minds of humankind. 
    
    Our kind's collective thoughts would weave together, and become one just like this..."""

    J"(Suddenly I find myself looking at my hand as Lenorra's fingers...)"

    J"(...her fingers intertwined with mine as she holds my hand tightly...)"

    LQ"""... this is just a singular example, but we'd all get to share our findings, our research, pain, happiness... 
    
    Our everything will bleed together so that we as individuals are never lost."""

    J"(...I pull my hand away from Lenorra's, I felt uncomfortable with the weight of her glare)"

    J"...I don't even know you? Why my memories?! "

    J"(I am suddenly teary eyed... I wasn't getting any answers from her...)"

    J"...This is the first time we are meeting...and I...you..."

    J"(With every sentence, Lenorra had weaved her way into my life.)"

    LQ"You are wrong Julia, this isn't the first time we are meeting...we had a conversation earlier...remember? "

    J"What?"

    LQ" It was about the Brookcastle incident...no worries, I rather not strain your mind with those thoughts again."

    show bg toilet with fade
    #(Transition back to reality)
    
    J"(I find myself shaking for a brief moment. I look at my hand, and I am reminded of that past interaction with Lenorra at the Institute.)"

    J"""(I slowly slide against the wall, sitting down on the floor, left alone with my thoughts.)

    (I looked at my hand again for a brief moment.)
    
    (I recall Lenorra's smile and that false sense of hope she radiated.)"""

    J"Why are you back again...? to take everyone back to the institute with you?"

    J"They can't experience the same pain I did... I don't want that to happen..."

    J"""(A thought comes into my mind)

    (You could turn yourself in)

    (I don't know what to do, and suddenly ending it all here... it... it doesn't seem like a bad idea.) 
    
    (It would be better than the looks of disappointment from my friends...)"""

    J"""The same hand that held Lenorra's that day is the one I used to play guitar with my band...

    ... the one I used to beat up people with my bat, to train with Quol... or read with Renee."""

    J"""(I grip my hands, my nails digging into my skin.)
    
    (If Lenorra stood in front of me in this bathroom right now, would I be able to fight against her with the state?)"""

    J"""(I couldn't... and I hated this answer.) 

    (My vision is blurred by my tears, as I relax my hand, there's a possibility that everything right now falls to ruin because of me!)

    (I stand up and I walk towards the washroom exit... but then I find myself stopping in place.)

    (...) 

    (When I see my reflection in the mirror, I look at myself and I don't like what I see.)"""

    #A/N: 
    #(transition back to storybeat)
    show bg black with fade
    LQ"Is the room ready? I want Julia secured to the hospital bed..."

    J"(Her speech dwindles into muffles as I fall unconscious accompanied by a pounding pain in my head.)"
    show bg toilet with fade
    #(Story Beat 1 Part 1 End)
    J"""(I find that I was talking to myself in the bathroom facing the mirror...)
    
    (tears seeped down my cheeks... )
    
    (my head would continue to hurt just like that day they first caught me.)"""

    J"Could this all be my fault? Are they really here to extract my memories again?"

    J"(I look at myself in the mirror... my reflection reminded me of the terror I felt there... I get anxious)"

    J"""Just a few moments ago, everything was fine... 

    Everything felt comfortable... the debut...the...the... 

    It's... all so fragile...""" 

    J"(I glance at the mirror again as I take a few steps back, leaning against a bathroom stall)"

    J"(The face that looks right back at me stuns me... I hadn't been this terrified since the first memory extraction)"
    show bg black with fade

    #A/N: Fade to black as the stall mirror "transforms" into a window a helpless Julia bound to a hospital bed would look through 

    #(Mental Breakdown + Story Beat 1 Part 2) 

    J"(...murmurs can be heard in the background alongside miscellaneous noise, and footsteps made by Lenorra towards her colleagues)"

    J"""(...as I regain consciousness I notice restraints that bind me to a sterile bed. I am unable to move and forced to look ahead through a window... I focus on Lenorra.)

    (She was surrounded by a group of people conversing amongst one another)"""

    G1"Is it necessary to bind her to the bed like that..."

    LQ"""Her state of mind is dwindling and she wants to leave. 
    
    I got her to lower her guard and now we can begin searching her memories for any evidence of underlying Brookcastle details."""

    G1"However, she has said countless times before... she can't recall, are you sure she is the one we are looking for?"

    LQ"""... and you choose to believe the patient over your superior! 
    
    Given the circumstances provided by previous information we've found and past events, it might be beneficial to examine Julia's mind closely...

    ...even if she doesn't know whatever memories lie in her brain right now, the documents show that she is related to Brookcastle. That alone is strong enough evidence to examine her mind..."""

    J"(I gather enough strength to attempt to wiggle myself free but it does not work... it also seems to have caught Lenorra's attention)"

    J"(After a slight pause, she started to walk towards me. My trembles increase in magnitude for every step.)"

    J"(Suddenly Lenorra leans in to hug me. I don't know what to make of it. I am frozen in place...too stunned to let a word out...)"

    J"(I struggle to understand what Lenorra is talking about...)"

    J"I don't feel comfortable with this. I want to go home, please let me leave—"

    LQ" (I am suddenly embraced by Lenorra as she hugs me tightly)"

    J"... what? What is this?"

    J"(I feel a prick at my neck as Lenorra drugs me. The needle of her syringe goes deep as I feel lightheaded.)"

    LQ"""...

    I hope I've made a good impression."""

    J"No...I want to leave...Please, I'm begging you...I really don't know..."

    LQ"Excuses..."

    J"(Those were the last words escaping Lenorra's lips before I begin to lose balance...)"

    LQ"Prepare the operating room..."
      
    J"(It is starting to feel hopeless...)"
    show bg toilet with fade
    #(Transition back to reality)
    J""" Even before all of this— I don't know what I was doing with my life. 

    It was always torn away from me by them— 

    The Institute...

    These days I find myself crying alone because of them... just like right now..."""

    J"""(I look away from the mirror and for a moment I eye the exit door...)
    
    (I focus on my breathing... it's as loud as ever...)"""

    J"""Huff...huff...

    They'll eventually find me if I hide out here

    What can I do now...what do I do??"""

    menu:
        "No! The agents they will find me if I stay in here any longer":
            hide Julia
            jump JH2
        "I should just hide out here...it should be safe..":
            hide Julia
            jump JH3




label JS1:
    hide Quol with Dissolve(0.3)
    hide Renee with Dissolve(0.3)
    show Julia at textbox_over
    J"""(As the chaos ensues and my initial shock begins to fade, a fire ignites within me.)

    (Seeing as my bandmates valiantly defending me from the agents' onslaught, a surge of determination courses through my veins.)"""

    menu:
        J"Calm down...calm down..."
        "I need to help my friends!":
            jump JS1FS      

label JS1FS:
    show Julia nervious at textbox_over
    J"""(I can't stand idly while they put themselves in harm's way. I need to help them.)

    (With a deep breath, I snap out of my daze, focusing my attention on the unfolding fight.) 

    (My eyes quickly scan the area, searching for anything that could aid me in this sudden battle for survival.)"""
    
    hide Renee with Dissolve(0.3)
    hide Quol with Dissolve(0.3)
    show Renee bag at Transform(xalign=0.5, yalign=0.4) with Dissolve(0.3)

    J"""(And then I spot it ... my trusty bat, safely tucked inside Renee's bag.)

    (But before I can fully process my next move, my attention is abruptly diverted.)"""

    hide Renee bag
    show JS1FS
    show screen display_hp
    J"(An agent charges towards me, wielding a baton and swinging it with force.)"
    menu:
        J"gasp!"
        "Try to dodge the attack":
            hide JS1FS
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsa
        "Scream":
            $ hp -= 3
            if hp <= 0:
                # If hp is 0, jump to the game_over label
                jump game_over
            hide JS1FS
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsb
        "Reach for my bat":
            $ hp -= 1
            if hp <= 0:
                # If hp is 0, jump to the game_over label
                jump game_over
            hide JS1FS
            hide Julia
            show Agent1 at center_lower with Dissolve(0.3)
            jump js1fsc

# fight scene JS1
label js1fsa:
    # Julia dodges attack
    # No hp lost
    
    J"(Instinct kicks in, and I rely on my reflexes and agility.)"
    play sound "SFX/JS1FS/batonswoosh1.mp3" volume 4
    J"""(I lean to the side, narrowly dodging the incoming strike.)
    
    (I stare in disbelief as I try to process how close I was to being hit.)
    
    (But my relief is short-lived. The agent, undeterred by the missed strike, quickly regains their composure.)"""
    
    jump js1fsd

label js1fsb:
    # Julia gets struck with the baton
    $hp -= 3
    
    J"""(I'm overcome with shock and instinctively let out a loud, piercing scream.)
    
    (The sound reverberates through the air, momentarily filling the space with my alarm and surprise.)
    
    (I react instinctively, raising my arms in a desperate attempt to shield myself. In a split second, my forearms form an X-shaped barrier, intercepting the full impact of the baton.)"""
    pause 0.5
    play sound "SFX/JS1FS/batonhit.mp3" volume 4
    pause 1.0
    Q"Julia! are you alright?!?"
    
    J"(Quol's voice cuts through the chaos)"
    
    Q"I'll be there! Hang on Julia! Fight back!"
    
    J"(I gather up myself and endure the pain, then look upwards at the agent.)"
    
    jump js1fsd

label js1fsc:
    # Julia gets her bat but gets hit in the leg(?)
    $hp -= 1
    
    J"(As I swiftly dash towards Renee's bag, my eyes fixated on retrieving my bat, a sudden impact jolts through my leg.)"

    play sound "SFX/JS1FS/batonhit.mp3" volume 5
    
    J"""(The agent's swinging baton connects with my lower leg, causing an intense burst of pain to surge through my body.)
    
    (The force of the blow sends me off balance, causing me to stumble and stagger in my attempt to reach the bag.)
    
    (However, I manage to snatch my bat from Renee's bag)"""
    
    menu:
        J"and next, I'll.."
        "Block":
            jump js1fse
        "Hit him back":
            jump js1fsf

label js1fsd:
    J"(He quickly recovers himself and prepares for another hit)"
    
    menu:
        J"What do I do..?"
        "Scream":
            jump js1fsg
        "Try to dodge the attack":
            jump js1fsh
        "Reach for your bat":
            jump js1fsi

label js1fsg:
    J"""{b}AAAAAH!{/b}
    
    (I let out a startled cry.)
    
    (Voice trembling with fear and frustration, as well as an overwhelming hopelessness.)"""

    hide Agent1
    show Quol at center_lower with Dissolve(0.3)

    "(However, before the baton makes contact with me, Quol swiftly intervenes.)"
    
    play sound "SFX/JS1FS/impactkick.mp3" volume 3

    J"""(With a swift kick, she delivers a powerful blow to the agent, sending them crashing to the ground, unconscious.)
    
    (Afterwards, she extends a hand towards me, her voice filled with concern.) """
    
    Q"You alright, Julia?"
    
    J"""(I nod in response.)
    
    Thank...Thank you..."""
    
    Q"Better fight back next time."
    
    J"(I silently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
    Q"Better keep it in your hands at all times."
    
    jump js1fsafter



label js1fsh:
    J"""I'll dodge, it'll be fin-
    
    Ah!"""
    
    pause 0.5
    play sound "SFX/JS1FS/batonwoosh2.mp3" volume 5
    pause 0.5

    J"(Just as I gather my resolve to evade the agent's attack, I stumble over my own feet)"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 4

    J"""(I collide with the ground, as pain shoots through my body)
    
    Ouch!
    
    (The impact leaves me momentarily disoriented, my breath catching in my throat.)
    
    (Frustration and fear wells up within me as I watch the baton swinging down towards me.)"""
    
    hide Agent1
    show Quol at center_lower with Dissolve(0.3)

    "(However, before the baton makes contact with me, Quol swiftly intervenes.)"
    
    play sound "SFX/JS1FS/impactkick.mp3" volume 3

    J"""(With a swift kick, she delivers a powerful blow to the agent, sending them crashing to the ground, unconscious.)
    
    (Afterwards, she extends a hand towards me, her voice filled with concern.) """
    
    Q"You alright, Julia?"
    
    J"""(I nod in response.)
    
    Thank...Thank you..."""
    
    Q"Better not trip next time."
    
    J"(I silently watched as she goes over to Renee's bag and pulls out my bat, then tosses it to me.)"
    
    Q"Better keep it in your hands at all times."
    
    jump js1fsafter

label js1fsi:
    J"""(As the agent lunges towards me, their baton poised to strike, I gathered the courage to finally reach for my bat.)
    
    (Pouncing backwards, I land next to Renee's bag, and lifted my bat out of it.)
    
    (My grip tightens around the bat, my knuckles whitening as I prepare to meet the agent's attack head-on.)
    
    (The agent's baton hurtles towards me, and I brace myself for the impact.)"""

    play sound "SFX/JS1FS/batonwoosh2.mp3" volume 7

    pause 0.5

    play sound "SFX/JS1FS/batonhitbat1.mp3" volume 5


    J"(I skillfully parry the agent's attempts to strike back.)"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 3

    J"(I block again)"
    
    play sound "SFX/JS1FS/batonhit2.mp3" volume 3

    hide Agent1 with Dissolve(0.3)

    J"(and finally deliver a hard blow, knocking the agent out cold.)"
    
    show Quol at center_lower with Dissolve(0.3)

    Q"Good job!"

    hide Quol with Dissolve(0.3)
    
    J"(Quol compliments my resolve.)"
    
    jump js1fsafter

label js1fse:
    J"I should block him"
    
    play sound "SFX/JS1FS/batonhitbat2.mp3" volume 3

    J"""(As the agent launches their attack, I swiftly raise my bat, positioning it as a shield against the incoming strike.)
    
    (In the brief moment following the block, my mind races, preparing for the next move.)
    
    And then..I'll hit him back!"""
    
    jump js1fsf

label js1fsf:
    J"AAuaAGGGGHHHH!"
    
    play sound "SFX/JS1FS/batonhit.mp3" volume 5

    J"""(With a surge of energy, I propel myself forward, As I channel a powerful swing towards the agent.)
    
    (I watch as the agent staggers backward, shaking with disbelief.)
    
    (Moments later, they collapse to the ground.)"""
    
    jump js1fsafter

label js1fsafter:
    
    hide Quol
    hide Agent1
    hide screen display_hp

    show Julia exhausted at textbox_over

    J"""At least we have one less to deal with now...

    (I let out a tired sigh as I cast a glance at the fallen body, sprawled on the ground.)

    (The defeated foe lay motionless, a testament to our hard-won triumph.)

    (With a heavy heart, I shifted my focus to assess the state of my companions.)"""

    hide Julia

    show Renee worried at right_center_lower with Dissolve(0.3)

    R "Look! There's still more of them coming in from the entrance."

    J"""(I observed Renee, her face etched with her unyielding will, desperately fending off two agile Agents.)

    (With lightning-fast reflexes, she deftly swung her whip, each crack of the lash a symphony of defiance against overwhelming odds.)"""

    R "I can't hold this up forever!"

    show Quol at left_center_lower with Dissolve(0.3)

    Q"Same!"

    J"""(Quol, standing her ground nearby, fought off two relentless Agents of her own.)
    
    (They lunged at her, attempting to subdue her, but she fought back with a flurry of kicks and quick dodges.)"""

    Q"Get away from us or you'll end up like your fucking friend!"

    J"""(The determination in Quol's voice echoed through the chaos as she unleashed her own brand of defiance, refusing to yield to their onslaught.)

    (Watching them fight, I could feel a powerful momentum building within me, an irresistible urge to join the fight.)

    I want to help..

    (But who should I help first?)"""

    menu:
        J"I want to help.."
        "Help Quol first":
            jump JS11
        "Help Renee first":
            jump JS12    


label JS11:
    hide Renee
    hide Quol

    show Julia traumatized at textbox_over

    J"I'll help Quol first!"

    hide Julia

    show Agent1 at center_lower with Dissolve(0.3)

    J"""(Without hesitation, I propelled myself forward, instantly closing the distance between me and the Agent.)

    (Gripping my bat firmly, I swung it with all my might, delivering a powerful blow that connected with the Agent's body.)"""

    hide Agent1 with Dissolve(0.3)

    show Julia exhausted at textbox_over

    play sound "SFX/JS1FS/batonhit2.mp3" volume 3
    
    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    hide Julia

    show Quol at center_lower with Dissolve(0.3)

    J"""(Quol's eyes widened briefly in surprise, but a grateful smile quickly spread across her face. )

    (She wasted no time, using the opening I had created to knock down the second Agent with a kick swiftly.)

    (The air crackled with a mix of adrenaline and relief as Quol, and I stood side by side, our united front a testament to our shared resolve.)

    (The tides of battle seem to have shifted in our favour, even if just for a moment.)"""

    hide Quol with Dissolve(0.3)

    show Julia traumatized at textbox_over

    J"""(However, I turned my head towards Renee and witnessed her leg getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    hide Julia

    show Renee worried at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Renee, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)"""

    hide Renee with Dissolve(0.3)
   
    J"(And then, in that moment of uncertainty, a vivid memory flashed in my mind—a scene I had shared with Renee not too long ago.)"

    show bg ReneeBedroom

    J"""(Renee's room was bathed in soft, warm light as she and I sat side by side on the edge of the bed.)

    (It had been a long and challenging day, and we sought solace in this quiet moment of respite.)"""
   
    show Renee alt at center_lower with Dissolve(0.3)

    J"""(I looked at Renee, her presence a comforting anchor in the storm of uncertainty that swirled within me.)

    (The weight of the future pressed heavily on my mind, filling me with a sense of unease.)

    (I couldn't help but express my concerns.)

    Renee...

    I'm...uncertain about the future...
    
    It's like..like as if I'm standing at a crossroads, not knowing which path to take..

    I'm scared... that I would make wrong choices or I would not live up to my potential.

    (Renee turned to me, her eyes filled with a mixture of understanding and compassion.)

    (After a brief silence, she touched my shoulder gently.)"""

    R """Julia.

    I kind of understand that feeling. 

    You see... there was a time when I was near death when everything seemed lost. 

    But surviving taught me the value of life and each moment's preciousness."""

    J"(Her words resonated deep within me, stirring a renewed perspective.)"

    show JS11 with Dissolve(1)

    R """Being alive allows for endless possibilities, Julia. 

    It opens doors to discovering the meaning of our existence and the roles we want to play in this world. 

    It's not about finding all the answers right away, but about embracing the journey and exploring what truly matters to us."""
    show Renee alt smile at center_lower
    hide JS11 with Dissolve(0.3)
    show bg ReneeBedroom
   

    J"""(Her words held a profound truth, reminding me to cherish the gift of life and find solace in the process of self-discovery.)

    (Renee's unwavering belief in the importance of protecting one another echoed in my heart, reminding me of the bond we shared.)

    (Moved by her sincerity, I nodded, gratitude and determination shining in my eyes.)

    Thank you... Renee.

    (Renee smiled warmly, her gaze filled with trust and camaraderie.)"""

    R "I wouldn't want to see my best friends being in pain, would I?"

    hide Renee with Dissolve(0.3)
    show bg stage with fade

    J"""(I snapped back to reality, realizing her bag was near the drums. Pulling it closer, I hurriedly searched for anything that could help Renee's injured leg.)

    (As I search through her bag, I find her favorite drink, Ice Red Tea, still cold. An idea flashes in my mind, using the chilled tea like an ice pack for her bruised leg.)

    (I grab the tea, gently applying it to the affected area, hoping the cold can provide some relief to Renee.)

    (As I tended to Renee's leg, I heard footsteps approaching behind us fast. Panic surged through me as I turned around to see an agent charging toward us.)

    (I instinctively shielded Renee from the impending danger, but Quol intercepted the threat, delivering a powerful blow that left the agent unconscious.)

    (I breathed a deep sigh of relief before turning my attention back to Renee, helping her back on her feet by placing her arm over my shoulder.)

    (Quol turns to us to check, I give her a reassuring nod showing we're okay. She nods in response before her attention returns to the agents.)

    (The tension lingers in the air, a silent acknowledgment of the dangers we've faced and those that still loom ahead.)

    (I realized that I had to protect everyone.)"""

    jump JS13

label JS12:
    hide Renee
    hide Quol
    J"I'll help Renee first."

    show Agent1 at center_lower with Dissolve(0.3)

    J"""(Swiftly, I closed the distance between Renee and her assailant.)

    (As I approached, I noticed an opening—a split second where my approach momentarily diverted the Agents' attention.)

    (Seizing the opportunity, I gripped my bat firmly.)

    (I swung it with all my might, delivering a powerful blow that connected with the Agent's body.)"""

    play sound "SFX/JS1FS/batonhit2.mp3" volume 3

    hide Agent1 with Dissolve(0.3)

    J"(The force of impact sent them sprawling to the ground, momentarily stunned.)"

    show Renee at center_lower with Dissolve(0.3)

    J"""(Fueled by my unexpected intervention, Renee swiftly took advantage of the moment.)

    (Her whip cracked through the air, striking the other Agent with a resounding crack.)

    (The enemy stumbled backwards, defeated and unconscious.)

    (A mixture of relief and determination washed over us. Renee's eyes met mine, gratitude and understanding passing between us in that fleeting moment.)"""

    hide Renee with Dissolve(0.3)

    J"""(However, I turned my head towards Quol and witness her leg getting hit by the baton of one of the agents and tumbling to the floor.)

    (My heart skipped a beat.)

    (The sight sent a surge of worry coursing through me, momentarily overshadowing the triumph of our successful attack on the Agents.)"""

    show Quol at center_lower with Dissolve(0.3)

    J"""(Without a second thought, I rushed to her side, my concern overriding any other consideration.)

    Quol, are you alright?

    (I was trembling and had no idea what to do.)

    (As panic threatened to consume me, my mind raced, desperately searching for a solution.)"""

    hide Quol with Dissolve(0.3)

    J"(And then, in that moment of uncertainty, a vivid memory flashed in my mind—the scent of rain and mud..)"

    show bg Hotelalley with fade
    play music "Anxiety_Shows.mp3"

    J"""(A few weeks after I escaped from the NewFutures Institute and first meeting Quol.)

    (We tried to stay low, trying our hardest to scrape by, with the anxiety of being caught constantly looming over my mind.)

    (I had contacted someone who works for my family-run hotel, the only person who agreed to risk themselves and help me out.)
    
    (I was waiting in a dark alleyway behind the hotel with Quol beside me, I kept fiddling my thumbs)
    
    (This is a bad idea, this is a bad idea...)
    
    (The rain falling deafeningly on the hood of my raincoat, as the backdoor of the hotel swings open.)"""

    show Lars at right_center_lower with Dissolve(0.3)
    
    L"""Sorry to keep you all out in the rain, today's a hectic shift.
    
    I can't be out here for too long or they'd realize I'm gone, since you left this place became like The Institute's personal playground.
    
    There's that one girl from The Institute, Lenorra. 
    
    She acts all nice and dutiful when her boss is looking, but as soon as the Head Scientist turns around she'd just order us around like we are her personal servant or somethi-"""
    
    show Quol at left_center_lower with Dissolve(0.3)

    J"(Quol glares at Lars in annoyance)"

    L" Aha- Sorry, yeah, that's all I could gather before they would start asking questions."

    J"(Lars quickly hands me a bag of supplies, filled with canned foods, hygiene items and a few pieces of clothes.)"
    
    L"""I have to return to my shift now, I have more orders to deal with otherwise I'm in deep trouble. 
    
    Take care and be careful."""
    
    J"(Lars returns to the hotel, closing the door behind him.)"

    hide Lars with Dissolve(0.3)
    show Quol at center_lower with Dissolve(0.3)
    stop music fadeout 5

    Q"Let's go back now before someone sees us."

    J"""(I nod in response, swiftly zipping the bag shut.)

    (I sling the bag over my shoulder, taking a deep breath of relief.)

    (I scan the dimly lit alleyway, hoping that no one is around to see us. I turned towards Quol, who was ready to leave.)"""

    hide Quol with Dissolve(0.3)
    
    J"""(As I was about to take my step, something caught my attention. From the corner of my eye, I spot a silhouette of a man holding a few trash bags, frozen in place, his gaze locked onto us.)
   
    (Being caught off guard, I instinctively freeze, feeling my heartbeat undergo a sudden shift.)
    
    (The man drops the trash bags he was carrying and in a panic dashes away.)"""

    show Quol at center_lower with Dissolve(0.3)
    play music "Fear_And_Terror.mp3"
    
    J"""(Oh no! Are we gonna get caught?!)

    (I turn to Quol and without hesitation, she bolts into action in pursuing him.)

    (I stand there, paralyzed and uncertain, unable to shake off the initial shock as I watch Quol chase after the fleeing figure.)
    
    (With a burst of speed, Quol closes the gap. In a sudden, precise movement, she tackles the figure, pinning him down as he struggles to escape.)
    
    (It all happened so fast, my head couldn't wrap itself around the sudden turn of events.)
    
    (In one swift, powerful movement, Quol hits the man with a heavy bash to his head, knocking him out cold.)
    
    (She turns to me, her expression dead serious.)"""

    Q"""... We can't keep him alive.

    ... He'd tell on Lars. He'd tell on you.

    ...
    
    Julia."""

    J"""(Quol wants me to do it...)

    (My body shakes in anxiety and fear, should I do it?)

    (... Can I do it?)"""

    menu:
        "Yes":
            pause 0.0000001
        "...":
            pause 0.0000001

    hide Quol

    J"(I clutch my bat tightly, hesitantly walking towards the guy.)"

    Q"""Julia. Think about yourself.

    You would risk Lars' safety and all that he had sacrificed for us?"""

    J"""(I look at the man, then my bat...)

    (My breath is short and fast, my hands trembling. The sound of the rain seems to intensify around me.)

    (I take a moment, closing my eyes, holding my bat tightly and taking a deep breath.)

    (...)

    (... This is the moment. The sound of the rain becoming quiet.)

    (I raise my bat over my head...)
    
    (and...)"""
    show bg black with fade
    pause 0.8

    play sound "SFX/JS1FS/batonhit.mp3" volume 7

    pause 1
    show bg Hotelalley with fade

    J"""(I lift my bat back up... the smell of rusted metal lined my bat...)

    (The sound of the rain returns to its deafening tone.)

    (I did it.)

    (...)"""
    show Quol at center_lower with Dissolve(0.3)
    J"(I turn to Quol. She gives me a nod of admiration.)"

    Q"""I'm sorry, Julia.

    life is full of funny choices huh?"""

    J"(She let out a forced chuckle.)"

    hide Quol with Dissolve(0.3)

    show bg stage with fade

    J"""(I snapped back, with moments to spare, I swung with all my might, my bat knocked down the agent who injured Quol.)

    (I realized that I had to protect my friends at all cost..)"""

    jump JS13

label JS13:
    J"Fighting off all the agents, it seemed like they got backup."

    menu:
        J"What will I decide on.."
        "I should keep fighting!":
            jump js42fs
        "I should tell everyone to back up to the backstage":
            jump JS3

label JS3:
    J"""We should go to the back!
    
    (We ran towards the back entrance, Quol a little more hesistant than me or Renee but she also came along.)

    (Adrenaline fueled our every step as we sprinted, desperately seeking an escape route from the perilous situation we found ourselves in.)

    (Reaching the backdoor, a glimmer of hope ignited within us. )

    (With a surge of anticipation, we swung the door open, expecting to find a path to freedom. )
    
    (However, our hopes were shattered as we were met with an unexpected sight:) 

    (Six agents, standing in a calculated formation, blocking our way.)"""

    show Renee worried at right_center_lower with Dissolve(0.3)

    R "It's an ambush!"

    show Quol at left_center_lower with Dissolve(0.3)

    Q"Go back!"

    J"""(I was stunned at this scene and before I knew it, an agent has already grabbed my arm.)
    
    (Renee and Quol noticed and tried to pull me away from the agents)
    
    (But it was too late)
    
    (After a moment of stuggle, all three of us were apprehended.)"""
    hide Renee
    hide Quol
    jump badend




#JS2
label JS2:
    show bg greenroom with fade
    play music "GreenBGM.mp3"
    J"""I burst into the green room, slamming the door open and gasping for air. 

    It awakened the only person who was in the room, who was lying comfortably on the sofas, and he was shocked when I rushed in with such an expression, and while creating such a loud noise."""
    hide Julia
    $ haveAndrew = True
    show Andrew at center_lower with Dissolve(0.3)
    A"""Holy mother of–

    Jeez it's just you, Julia.

    Concert done already? How does it feel like debuting?

    You're drenched in sweat already, I get how tense it is!"""

    J"I....I..."

    J"Andrew.."

    J"Iam...ah ... scared ... Andrew..."

    J"there are agents, the institute... we need to ... to..."

    A"They're here...?"

    J"(I nod as I am still gasping for air.)"

    J"(Andrew stands up hastily from the couch, gently picks up a glass of water and hands it over to me.)"

    A"Here... calm down..."

    J"(I slowly drink the glass of water, then exhale in relief after I finish, putting the glass on the nearby desk. The heavy gasps decreases into smaller panting of anxiety as I daze into the floor.)"

    J"(He then grabs my right shoulder, softly caressing it to comfort me as he looks at the door, his face visibly tense up in concern.)"

    A"Stay here."

    J"(no...no I won't. I quickly look up to him, our eyes meet.)"

    J"No!..."

    J"""(I am indeed scared. I don't want to return to the institute..being caught by them is the last thing I wanted to happen...)
    
    (but I shouldn't just stay here and do nothing as my friends struggle...)"""

    A"""H-hey now...Are ya sure?...You said you're scared. 
    
    I don't want you to catch any bruises y'know?"""

    J"..."

    J"(I was about to say something, but my words caught up in my throat as the thought of my past lingers back into my mind.)"

    J"(Andrew then nudges my shoulder gently, still grabbing onto it, to have us facing each other.)"

    A"""Julia?... You okay? 
    
    Tell me anything if you want to. 
    
    I can understand you're scared."""

    J"..."

    A"Julia... I know you're holding some words in your mouth..."

    J"(I am terrified.)"

    J"""(I am terrified that all of this will keep happening, and I am really scared of the past crawling at the back of my mind...)
    
    (I can't move. I don't want to recall the past... but I can't move a single muscle.)"""

    J"(... I am terrified of the institute...the agents...)"

    J"(and her...)"

    J"""(I feel nervious, scared, it feels impossible to let out words in this state.)
    
    (But Andrew's reassuring smile makes it feel a bit...easier for me to do so.)"""

    J"""...do... do I have to keep running away? from my past? F-from...them? 
    
    What if there's no next time?--
    
    What if we're gonna be cornered?--"""

    A"Ah...um... everyone feels that way, Julia. It's... it's fine."

    J"(I noticed how he said that so apprehensively...his smile becomes more nervious and unsure.)"

    A"Don't be scared... be...Happy that you still have your friends alongside you."

    J"...I... don't get it."

    J"(I see him glancing silently into the floor as he scratches his head briefly, before looking back at me again.)"

    A"Julia... Why did you join this band in the first place?"

    J"..."

    A"""...Your... initiative of agreeing to join the band is already an effort to have great little things in your journey. 
    
    Alongside people that you can share moments and grow with."""

    J"Huh..?"

    A"..."

    J"(I do get what he is saying, I can understand he is trying. But I don't think that connects at all...)"

    J"it's not that ... Andrew..."

    A"""Ah!- 
    
    S-sorry! 
    
    W-well? 
    
    Lemme think...
    
    Uhh..."""

    J"""the institute... will they always chase us? 
    
    Will there be an end to this? 
    
    I am scared not only at this moment... 
    
    I am scared of what will happen beyond this moment... 
    
    and my pas-"""

    A"""I-i know... Julia! 
    
    Everyone feels the same way too. Everyone has their own histories..."""

    A"O-or so I thought..."

    J"(... I know everyone has their own history... what does he mean?...)"

    J"""Yes I know... 
    
    but h-how long... how long do we have to keep running away..? 
    
    From the past ... 
    
    from them..."""

    J"(Andrew shakes my shoulders lightly as he stares at me, genuine concern is visible on his face, but encouragement is vivid in his eyes.)"

    A"""Snap out of it, okay? 
    
    whatever was your past, it doesn't matter now. 
    
    I don't want to hear ifs and buts. 
    
    What's happening is now. 
    
    And that's what matters!"""

    J"(My past doesn't matter...?)"

    J"...Andrew... but..."

    J"...would you...even understand?...i..."

    A"""Trust me... I do. 
    
    I did say that everyone has their...pasts righ-"""

    J"""I know!-- 
    
    you don't need to mention it twice Andrew... but I am just..."""

    J"i don't know what to do... what to say..."

    J"(Andrew close his eyes as he sighs.)"

    A"Look...Julia. You can... you have us right? You can believe in us."

    J"""...it felt isolating... 
    
    it felt so cramped...
    
    I do have Renee,
    
    Quol,
    
    ....you... 
    
    but I can't seem to believe anyone so much, and I can't even go elsewhere...without the thought of the institute!..."""

    J"i wish...I could have back the friends I had. even if it's just a small conversation..."

    J"i wish...my family didn't..."

    J"i wish things could've been..."

    J"(Andrew's expression frowns more.)"

    A"...but what happened... has happened... Julia..."

    J"(there's a hint of troubled in his expression.)"

    J"...I know... but Andrew i-"

    A"Lets not think about that right now! Please Julia. Don't bother about it or you'll always be like this!"

    J"(I can feel Andrew getting more desperate for us to move. But he felt as if he's ignorant about it...)"

    A"Please. Are you choosing to stay here or go with me???"

    J"I... want to!"

    A"Then stop thinking about whatever that had happened! drop it now or we would never move!"

    J"""(...huh?!...)
    
    (I know I am stuck on my mind about the past...) 
    
    (but to just drop it like that isn't as easy as just simply saying it...)"""

    J"I know Andrew... But-"

    A"No buts and ifs! Do you trust me and the others?"

    J"""(I do! But that's beside the point...) 
    
    (why is he asking that?) 
    
    (Is he that desperate?) 
    
    (Is he trying to brush this off?)"""

    J"Andrew...I do trust you, you all!"

    A"Alright then don't bother over what already happened..."

    J"""(he's trying to brush it off isn't he...)
    
    (As if it's just a simple switch of a button...to forget all these...)"""

    J"Andrew! It's not easy just like that! Do you...do you have any idea!"

    A"I do Julia! It's hard! But it's what we have to do this instance!"

    J"If you do... you can't just say I could just wipe the past off!"

    J"""(I almost don't know what I am saying anymore, he says it as if it's so easy to just... let it all go.) 
    
    (I know I shouldn't be stuck in the past. )
    
    (But telling someone to just forget about it as if I have control over it...)"""

    J"(our tone raise for every exchange of words.)"

    A"Its hard to not overthink about it, but let's put it aside now!"

    J"do you forget about the past as easy as how you said it?!"

    A"""Of course I don't! Don't say that! 
    
    But if we keep clinging on the past our ass would still be sitting in here all day! 
    
    Don't bring up about the past!"""

    J"But you say it as if I should simply just be ignorant about it as much as you do!"

    A"Its better that way than just to whine about it all the time!"

    J"You wouldn't understand because you're just that ignorant!"

    A"""it doesn't matter and it never matter because it happened! 
    
    Think and whine a lot and it wouldn't just magically fix your past anyways??"""

    J"""See?! 
    
    Do you even care about any past?! about people you cared before?! Are you that ignorant about the-"""

    A"I KNOW! I JUST DONT WANT TO SEE IT BACK ANYMORE!"

    J"(I am left speechless as I realized whatever we said, my face is in shock and worry as Andrew yells, his face gets a bit redder.)"

    A"""I DONT WANT TO RECALL IT ANYMORE! I MISS THEM TOO! AS MUCH AS YOU DO TO YOUR OWN! 
    
    DO YOU THINK ITS NOT PAINFUL TO GET REMINDED OF THEM?!"""

    A"""I WISH I COULD GO OUT THERE AND TALK TO SOMEONE TOO! TALK TO MY FAMILY! MY FRIENDS! 
    
    AS IF NOTHING IS ON MY TAIL EVERY NOW AND THEN! 
    
    AS IF... if...."""

    J"(we're both gasping for air, I can only look at the floor as all the things I said finally sink into my thoughts.)"

    J"""(But he said something is after him... is the institute after him too?)
    
    (...nonetheless...I feel...guilty. )
    
    (I think this is my fault... my eyes are watery again...)"""

    A"..."

    J"""(Andrew grab my left shoulder once again, trying to comfort me. 
    
    I take a few steps back... i really have to apologize. 
    
    But it's hard. It's stuck in my throat...)"""

    A"..You know..."

    A"You remind me exactly of... myself... Julia."

    J"(as soon as I heard this, I lift my head and our eyes meet.)" 

    A"""Afraid, Anxious, Lonely, Lost... And many many doubts... but I try to ignore all of that so I could live on. 
    
    It's hard but I tried my very best. 
    
    But because of this I do admit I got a bit too... ignorant and only think about moving on."""

    A"""I didn't think about how difficult it actually is for someone else. 
    
    Just so you know Julia... no matter how much ignorant I may seem... beneath this... I am just like you. 
    
    I am just as terrified as you are, about the past and the future."""

    A"But we can't just let all those lingering thoughts halt us In the present. What matters now is what we choose to do now, what we choose to be."

    A"""The past shouldn't pull us back, it should push us forward. 
    
    It should be the reason as we go far far away from whatever happened and face what's next."""

    J"..."

    J"(as much as the past hurts me, he does have...a point.)"

    J"(I never expected us to have similar experiences. Usually he's just relaxed everytime I saw him since the day he first joined... but I never seen this side of Andrew...)"

    J"Andrew...how come you never tell us about this?..."

    A"Well.."

    J"(Andrew looks down for a brief moment, then looks at me again, faintly smiling.)"

    A"""It's not like I want to talk or hear anything about it again in the first place.

    Like I said, it's what happened. And I'm trying to venture away from it.

    But at the same time, I never want to forget about them. But all I can do is look away after all.

    We all have eyes on the front. We should be looking towards the front, seeing the present and be prepared for the future, Julia."""

    J"my eyes looked down, staring blankly, thinking about his words."

    A"*sigh* I want to thank you. I can finally lift off this sealed feeling off my chest, it sat too long inside me... I can finally express it to someone else."

    J"I look up at him once again...now with a smile."

    A"""Someone...who can understand.

    I am sorry I was so ignorant."""

    J"""...i-Its alright Andrew... I am also thankful we could... talk about this...

    ...I also apologize for being whiny...um...

    I...I know I am stuck in the past as much as you want to run away from yours.

    But I think what's best is that we...we do our best now..."""

    J"(Andrew smiles widely. He then tap my forehead, before facing towards the door.)"

    J"Eep-"

    A"""Don't tell anyone about this, alright?

    About me, about my past.

    It's best to keep this between us."""

    J"""(He then winks at me before he walks towards the door, hinting me to follow him.)

    (I reply with a smile.)

    (I am glad we had that talk...I feel less isolated...I think)

    (I can understand why he wouldn't want the others to know. I feel a bit...honored to be trusted...and to trust someone back as well.)

    (I stand still for a brief moment, I feel the past and what I lost still creeping at the back of my mind...)

    (Yes, the past did happen and impacted me as a whole.. but I think it's best to use it as a motivation to stray further away from it.)

    (For this moment... I am still having a hard time doing so..)

    (But at the very least I still could see what's in front.)

    (At the very least... I have... a bit of hope now.)

    (At the very least... I am still here.)

    (At the very least...)

    (I am trying.)

    (I then run, catching up to him.)"""
        
    jump JS23

label JS23:
    
    menu:
        "what should we do?"
        "Return to our friends":
            hide Andrew
            show bg stage
            jump js42fs
        "Exit through the backdoor":
            jump JS25    

label JS25:
    J"""(We decided to run towards the backdoor, our hearts pounding with a mix of fear and resolve. )

    (Adrenaline fueled our every step as we sprinted, desperately seeking an escape route from the perilous situation we found ourselves in.)

    (Reaching the backdoor, a glimmer of hope ignited within us. )

    (With a surge of anticipation, we swung the door open, expecting to find a path to freedom. )
    
    (However, our hopes were shattered as we were met with an unexpected sight:) 

    (Six agents, standing in a calculated formation, blocking our way.)
    
    AH-
    
    (Andrew immediately grabbed my arm and attempted to run the opposite direction, but their hands were already grabbing my arm tight.)
    
    (After a moment of struggle, both of us were apprehended.)"""
    hide Andrew with Dissolve(0.3)
    jump badend


label JH2:
    J"But... they'll catch me again..."
    J"""(I huddled onto the bathroom tiles, my back against the wall, contemplating my choices whether I should really go out there and risk myself or stay.)
    
    (I let out a quiet puff of breath, looking down at the bathroom tiles. The sound of the passing footsteps outside echoed, intensifying my panic.)
    
    (What am I gonna do... what am I gonna do...)
    
    (I continue looking at the bathroom tiles, not sure what to do.)
    
    (I attempt to hug myself for comfort)
    
    (My hands landed on the three pins on my shirt, each having a different color)
    
    (I stared at them, as i sense myself calming down a little)
    
    (I grabbed the pins tight so that the corners of the pins pains my palm.)
    
    (It brings me a sense of comfort.)
    
    (I looked at them after a while, my purple pin is sandwiched between the orange and blue ones of of Renee and Quol.)
    
    (It was a symbol of their support)
   
    (their support..)
   
    (There was a day during self defense practice where I was sandwiched between them too..)"""
    Q"That's it Julia! Beat them all! Don't leave your enemies alive!"
    R"That's... maybe a bit too much, Quol..."
    Q"What? What do you mean? Do you want your enemies to come back and beat you?"
    R"Well, no, but I think..."
    J"""(Quol and Renee began arguing on their different philosophies on the topic. I stand there and watch as Quol asserts the need to eliminate the enemies while Renee is concerned about the level of aggression.)
    
    (However, since Quol is at my right and Renee is at my left, I was caught in the middle of it)
    
    (After a while, I feel like my eardrums were doing to burst.)"""
    J"Girls.."
    J"""(I managed to speak up after a while in a more loud tone than normal, causing a paused silence in the air)
    
    (I looked at the two)"""
    J"What exactly am I fighting for?"
    J"""(Silence followed, Renee and Quol stared at each other, throwing eye signals as both their expressions deepened)
    
    (But Renee broke the silence after a while)"""
    R"You are fighting for yourself, Julia."
    Q"To be exact, your future."
    R"That's the same thing isn't it?"
    J"""(Another pause followed, as I go deep into thought.)
    
    (My future?)
    
    (Me?)
    
    (I've never really thought of that.)"""
    J".."
    Q"What do you want, Julia?"
    J"""(Quol's words hit hard, what do I want?)
    
    (I guess..)"""
    J"I want to live..."
    J"(I paused again)"
    J"I want to take control of my life.."
    J"(Quol holds my hands, which are holding the bat, and put it in a ready position)"
    Q"And that starts with you holding this bat tight and swinging it at the people you dont want in your life anymore!"
    J"""(The bat hits the dummy and it falls on the floor)
    
    (We all giggled)
    
    (I take the dummy and put it back up, and throw another swing at it)
    
    (It flies across half the room)"""
    R"The bat is your tool."
    R"You should decide on who to swing it to."
    J"(Renee looked at the fallen dummy, then back at me with a smile on her face)"
    R"And we also have our own tools to help when you need it too."
    Q"Don't ever swing it at me Julia!"
    J"(I turned to the both of them, and gave a smile)"
    J"I won't!"
    #reality
    J"They are using their tools to protect me..."
    J"I have to use mine to protect them too!"
    J"(I held my hands in the air in the ready position, as if I had my bat)"
    J"I will swing it at the agents."
    J"(I swing my arms forward)"
    J"That is what I've decided."
    J"""(I take a deep breath)
    
    (I tried to open the door, surprisingly, it opens)
    
    (I sprint towards the stage, motivated to fight.)"""
    jump jhfs5


label JH3:
    #A/N: Fade to black
    J"""I should stay...I have my friends.

    They will come for me right...?

    Won't they..?

    (I started to doubt my own words)

    (Renee and Quol are outside fighting for me, I am sure they would come for me.)

    But...but....

    (Are you sure? Julia?)

    (I stared at the door in front of me, the wall between this room and the outside world.)

    (I heard a few knocks from the door, they sounded familiar...)"""

    #Fade to black then transition to hotel

    J"""(I knock on the door)

    Mother, please be home...anyone! Please answer the door..."""

    JM"(Julia's mother opens the door to her frail daughter helpless standing there right in front of you)"

    J"(My eyes widen when I see my mother...)"

    J"Mom I...we need to leave...i-"

    JM" My daughter I...I can't believe you are safe..."

    J"I...I'm sorry Mother...I...my head..."

    J"( I want to give my mother a hug but I am too weak...I start to cry...)"

    J"""(The warm embrace of my mother...never have I ever felt more in need of it then now.)

    (I cry rivers to my mother...I did not want this moment to end.)

    (Right now...I feel seen and heard by someone who has sideline me for years.)"""

    J" Mother...the Institute is after me...please you and father have to get them to stop!"

    J"(!!!)"

    J"(My mother promptly brings me inside...at first she was happy to see me but now she is unnerved.)"

    J"I did I do something wrong—"

    JM"Is the name Lenorra familiar to you? DO you know who that—"

    J"(I cut my mother off)"

    J"""Yes! Lenorra and the NewFutures Institute are after me, please Mother, you have to do something...I don't want to go back there!!!
    (I clutch my mother's dress)"""

    JM" You father was on the phone with them this morning...I overheard him...he has sorted out a deal."

    J"(I smile at my mother)"

    J"Thank you..."

    J"(My mother smiles back faintly...she doesn't make eye contact with me for a moment.)"

    JM"I love you...please wash up and get changed...I'll make you something to eat...your favorite meal..."

    J"(I am elated. My body moves on its own.)"

    J"I love you too..."
    #reality
    J"""I murmured to myself, tears stuck on my cheek.

    I love you..."""
    #flashback
    J"""(The next day I woke up early for breakfast)

    (Taking out a few dresses from the dresser, I held them in front of me and tried to see which matched me the most.)

    This one seems best!"""
    J"(I look in the mirror satisfied with the dress I was wearing...It matched my mother's. Maybe this will make everyone more happy to see me.)"

    J"(I do a final twirl in and smile at my reflection.)"

    J"I wonder what meal Mother had the butler prepare..."

    J"(When I go to open the door the knob won't budge...)"

    J"""Huh?

    (I tried opening it again)

    (That is very weird..)"""

    J"(Why won't the door open?)"

    J"Mother...Father..."

    J"(I am met with no response...I attempt to open the door again...)"

    J"Mother...Father...I'm stuck.. Can anyone open the closet door! I think it is jammed..."

    J"HELP PLEASE! "

    #(There is no response)

    J"(I slumped down next to the door.)"

    J"What...does this mean..."

    J"""Seconds passed into minutes, and the door was still stuck)

    (Does my family not want me?...was coming back here a mistake?) """

    J"(I sobbed until I get tired...this didn't take long.. I was starving...a dwindled lethargic...)"

    #reality/flashback
    J"(after a long while, the door opens suddenly)"

    J"(I lose balance and fall into Lenorra's arms)"

    J"(I was greeted by her wide smile.)"

    LQ"Julia, welcome back."

    jump badend





label js42fs:
    show screen display_hp
    J"(Four agents approched us)"
    if haveAndrew == True:
        jump js42fsa
    else:
        jump js42fsb

label js42fsa:
    J"""(Without hesitation, Renee sprang into action, her movements swift and precise as she lunged towards one of the agents.)
    
    (In a blur of motion, Quol followed suit, her agility and strength on full display as she engaged another agent.)

    (Layon looked at the two, shrugged, and pulled up his sleeves as he dashes towards the third agent)

    (My heart raced as I realized that there is one agent left, their attention now squarely focused on me.

    How should I approach this?"""
    menu:
        J"How should I approach this?"
        "Go for the kill":
            jump js42fsi
        "Play it defensively":
            jump js42fsj

label js42fsb:
    show Julia exhausted at textbox_over with Dissolve(0.3)

    J"""(Without hesitation, Renee sprang into action, her movements swift and precise as she lunged towards one of the agents.)
    
    (In a blur of motion, Quol followed suit, her agility and strength on full display as she engaged another agent.)
    
    (My heart raced as I realized that two agents still remained, their attention now squarely focused on me. )
    
    (Fear mingled with determination within me as I braced myself for the impending confrontation.)
    
    (One of the agents, slightly taller than the others, took a strong stance.)

    (He confidently threw his baton on the floor and came charging at me in full speed.)
    
    (Who should I focus on first?)"""
    
    menu:
        J"(Who should I focus on first?)"
        "Agent with a baton":
            jump js42fsc
        "Agent without a baton":
            jump js42fsd

label js42fsc:
    show Julia nervious at textbox_over
    J"(As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them.)"
    
    show screen timerDown(3, "misseditJS42FSc1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc1", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc1", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc1:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        show Julia traumatized at textbox_over
        J"(I got hit in the arm because I was not quick enough to react.)"
        jump finishedJS42FSc1
    
    label choice1JS42FSc1:
        J"(I swung left, and it blocked the baton.)"
        jump finishedJS42FSc1
    
    label choice2JS42FSc1:
        J"(I swung right, and it blocked the baton.)"
        jump finishedJS42FSc1
    
    label finishedJS42FSc1:
        J"(The agent is temportarily off guard.)"
        
    show screen timerDown(3, "misseditJS42FSc2")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc2", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJS42FSc2:
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit on the waist, then came to my senses and attacked his head out of reflexes.)"
        
        J"(They immedately fell on the ground motionless)"
        show Julia exhausted at textbox_over
        jump finishedJS42FSc2
    
    
    label choice1JS42FSc2:
        show Julia exhausted at textbox_over
        J"(I striked down on the Agent and they immediately fell on the ground motionless.)"
        jump finishedJS42FSc2
    
    label finishedJS42FSc2:
        J"""(He is down.)
        
        (My relief was short lived, as the other agent then tried to jump on me.)
        
        (What should I do?)"""
       
    menu:
        J"(What should I do?)"
        "Go for the kill":
            jump js42fsl
        "Play it defensively":
            jump js42fsm

label js42fsd:
    J"""(The agent without the baton approached rapidly, I see that he is trying to directly jump on me.()
    
    (I held tight my bat, and decided on my next move)"""
    
    menu:
        "Go for the kill":
            jump js42fsg
        "Play it defensively":
            jump js42fsh

label js42fsg:
    J"""(I decided to go for the kill)
    
    (I prepared my swing and gluped)
    
    (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
    
    (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
    
    jump game_over

label js42fsh:
    J"(I decided to get defensive and held my bat tight.)"
    
    show screen timerDown(3, "misseditJS42FSc5")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc5", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc5", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc5:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I stumbled backwards mildly.)"
        jump finishedJS42FSc5

    label choice1JS42FSc5:
        J"(I held my bat horizontally, and it blocked the baton.)"
        jump finishedJS42FSc5

    label choice2JS42FSc5:
        J"(I held my bat vertically, and it blocked the baton.)"
        jump finishedJS42FSc5

    label finishedJS42FSc5:
        J"""(I then swing towards his torso, making sure he fainted off.)

    (The other sees that I've knocked down his comrade, and approches me.)

    (As the agent with the baton closed in, I mustered all my strength and swung my weapon towards them.)"""

    show screen timerDown(3, "misseditJS42FSc3")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Swing left", "choice1JS42FSc3", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Swing right", "choice2JS42FSc3", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return

    label misseditJS42FSc3:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit in the arm because I was not quick enough to react.)"
        jump finishedJS42FSc3

    label choice1JS42FSc3:
        J"(I swung left, and it blocked the baton.)"
        jump finishedJS42FSc3

    label choice2JS42FSc3:
        J"(I swung right, and it blocked the baton.)"
        jump finishedJS42FSc3

    label finishedJS42FSc3:
        J"(The agent is temportarily off guard.)"
        
    show screen timerDown(3, "misseditJS42FSc4")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Strike downwards", "choice1JS42FSc4", 0.5, 0.3),  # xpos and ypos for choice 1
    ])
    return

    label misseditJS42FSc4:
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I got hit on the waist, then came to my senses and attacked his head out of reflexes.)"
        
        J"(They immedately fell on the ground motionless)"
        jump finishedJS42FSc4


    label choice1JS42FSc4:
        J"(I striked down on the Agent and they immedately fell on the ground motionless.)"
        jump finishedJS42FSc4

    label finishedJS42FSc4:
        jump js42fsafter

    label js42fsi:
        J"""(I decided to go for the kill.)
        
        (I prepared my swing and gluped.)
        
        (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
        
        (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
        
        jump game_over

label js42fsj:
    J"(I decided to get defensive and held my bat tight.)"
    
    show screen timerDown(3, "misseditJS42FSc6")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block Horizontally", "choice1JS42FSc6", 0.2, 0.5),  # xpos and ypos for choice 1
        ("Block Vertically", "choice2JS42FSc6", 0.8, 0.5)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJS42FSc6:
        $ hp -= 1
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        J"(I stumbled backwards mildly.)"
        jump finishedJS42FSc6
    
    label choice1JS42FSc6:
        J"(I held my bat horizontally, and it blocked the baton.)"
        jump finishedJS42FSc6
    
    label choice2JS42FSc6:
        J"(I held my bat vertically, and it blocked the baton.)"
        jump finishedJS42FSc6
    
    label finishedJS42FSc6:
        J"""(I then swing towards his torso, making sure he fainted off.)

        Another agent who was combating Andrew decided to run towards me to attempt to strike me
        
        But Andrew swipes his leg under him in time to trip him down.
        
        He then ends it by stomping on his face and then walking over him."""
        show Andrew at center_lower with Dissolve(0.3)
        A"You seem fine now right, Julia?"

        J"He giggles"
        hide Andrew with Dissolve(0.3)

        jump js42fsafter

label js42fsl:
    J"""(I decided to go for the kill.)
    
    (I prepared my swing and gluped.)
    
    (However, I lost my train of thought and when I came to my senses was when my back hits the ground.)
    
    (The agent has swiftly took my bat away from my hands and threw it away, while pinning me to the ground.)"""
    
    jump game_over

label js42fsm:
    $ hp -= 1
    if hp <= 0:
        # If hp is 0, jump to the game_over label
        jump game_over
    J"""(I held my bat horizontally to block the agent as he jumps on me.)
    
    (He hits my shoulder mildly, but I manage to swing him off and throw him on the ground.)
    
    (I then swing towards his torso, making sure he fainted off.)"""
    
    jump js42fsafter

label js42fsafter:
    hide screen display_hp
    J"(All the agents have passed out, and we all had a sigh of relief.)"
    jump cliff



label jhfs5:
    show Julia traumatized at textbox_over
    show screen display_hp
    J"""(As I reach the front stage, a sinking feeling settles in the pit of my stomach.) 
    
    (I glance behind me and discover that two agents have been tailing me, closing in on the stage. )
    
    (I looked around nerviously and came to a conclusion:)
    
    (I cannot go back now)
    
    (Quol and Renee looked towards me and recongizes the issue)"""
    hide Julia
    show Quol Angry at left_center_lower with Dissolve(0.3)
    Q "We can take down all of them! They can't just keep coming at us forever!"
    
    show Renee worried at right_center_lower with Dissolve(0.3)

    R "No..no! we have to back up! Lets not get oursleves too hurt!"
    
    J"""(Caught between these conflicting viewpoints, my mind races.)
    
    (But I know I can make a decision for us)"""

    hide Quol with Dissolve(0.3)
    hide Renee with Dissolve(0.3)

    show Julia nervious at textbox_over
   
    menu:
        J"(What should I do?)"
        "Fight them":
            jump jhfs5a
        "Make an escape for it":
            jump jhfs5b

label jhfs5a:
    J"(I decided that we have to fight them)"

    show Renee bag at Transform(xalign=0.5, yalign=0.4) with Dissolve(0.3)
    
    J"""(In the midst of the chaos, I catch sight of my weapon—a bat sticking out of Renee's bag, carefully placed behind the drum set.)

    (Without hesitation, I dash towards the bag, swiftly grabbing it.)"""
    
    hide Renee bag

    J"(I notice that the two agents behind are preparing to strike)"
    
    show screen timerDown(3, "misseditJHFS5a1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Go offensive", "choice1JHFS5a1", 0.2, 0.3),  # xpos and ypos for choice 1
        ("Go defensive", "choice2JHFS5a1", 0.8, 0.7)   # xpos and ypos for choice 2
    ])
    return
    
    label misseditJHFS5a1:
        J"""(I faltered and couldn't decide)
        
        (One of the agents swing towards me and I got hit)"""
        $ hp -= 4
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5a1
    
    label choice1JHFS5a1:
        J"""(With a surge of adrenaline, I decide to go on the offensive.) 
        
        (I swiftly pivot on my heel, channeling my momentum into a powerful swing of the bat.) 
        
        (The first agent lunges forward, and I time my strike perfectly, hitting his arm.) 
        
        (The crack of impact fills the air as the agent staggers backward, momentarily stunned.)
        
        (But he quickly regains his composure.)"""
        jump finishedJHFS5a1
    
    label choice2JHFS5a1:
        J"""(Feeling a pang of caution, I opt for a defensive strategy.) 
        
        (As the first agent lunges, I quickly sidestep their attack, narrowly evading their grasp.) 
        
        (With a calculated move, I position myself for a swift counter.) 
        
        (The second agent moves in, but I remain focused on evasion, waiting for the opportune moment to strike.)"""
        
        jump finishedJHFS5a1
    
    label finishedJHFS5a1:
        J"(I quickly access the situation and do my next move.)"
        
        show screen timerDown(3, "misseditJHFS5a2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Strike", "choice1JHFS5a2", 0.2, 0.3),  # xpos and ypos for choice 1
            ("Retreat", "choice2JHFS5a2", 0.8, 0.7)   # xpos and ypos for choice 2
        ])
        return
    
    label misseditJHFS5a2:
        J"""(I faltered and couldn't decide)
        
        (One of the agents swing towards me and I got hit)"""
        $ hp -= 4
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5a2
    
    label choice1JHFS5a2:
        J"""(Seizing the opportunity, I decide to press the advantage.) 
        
        (With a surge of confidence, I prepare to deliver a powerful strike to the agent.)
        
        (Unfortunately I missed my swing and the agents are unharmed.)
        
        (I leaped backwards and tried to give myself some space.)"""
        jump finishedJHFS5a2
    
    label choice2JHFS5a2:
        J"""(I choose to prioritize my safety.)
        
        (Recognizing that the second agent is closing in, I decide to disengage temporarily and create some distance.)
        
        (I leaped backwards and tried to regroup with my team.)"""
        jump finishedJHFS5a2
    
    label finishedJHFS5a2:
        J"""(I scanned around the stage to see that my comrades are all each fighting aganist an agent, whilst I am fending off two)
        
        (What should I do?)"""
    
    menu:
        "Keep fighting them":
            jump jhfs5d
        "Call for help":
            jump jhfs5e


label jhfs5b:
    J"""lets make the run to it!
    
    I started to dash towards the entrance. 
    
    Renee and Quol notices and follows suit
    
    The agents reacted to our escape attempt and tries to intercept us."""
    show screen timerDown(3, "misseditjhfs5b1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Dodge left", "choice1jhfs5b1", 0.2, 0.5),  # xpos and ypos for choice 1
    ])
    return

    label misseditjhfs5b1:
        $ hp -= 2
        "I bumped into an agent mildly and kept running"
        jump finishedjhfs5b1

    label choice1jhfs5b1:
        "I swiftly dodged one of the agents"
        jump finishedjhfs5b1

    label finishedjhfs5b1:
        "Another agent comes from the right, tring to swing down at me"
        show screen timerDown(3, "misseditjhfs5b2")  # seconds, label to jump on fail
        call screen qte_choice([
        ("Block", "choice1jhfs5b2", 0.8, 0.5),  # xpos and ypos for choice 1
        ])
        return

    label misseditjhfs5b2:
        "I got hit heavily."
        $ hp -= 5
        "I sluggishly try to keep going."
        jump finishedjhfs5b2

    label choice1jhfs5b2:
        "I block the attack and continuse running."
        jump finishedjhfs5b2

    label finishedjhfs5b2:
        "When i looked back forward, I see an agent right in front of my path, I dash towards him and.."
        show screen timerDown(3, "misseditjhfs5b3")  # seconds, label to jump on fail
        call screen qte_choice([
        ("Hit him", "choice1jhfs5b3", 0.5, 0.3),  # xpos and ypos for choice 1
        ])
        return

    label misseditjhfs5b3:
        "I smash right into the Agent as I mess up my swing."
        $hp -= 5
        jump finishedjhfs5b3

    label choice1jhfs5b3:
        "I swing right on his head, bringing him down with a powerful blow."
        jump finishedjhfs5b3

    label finishedjhfs5b3:
        "We were halfway to our distination"
        jump cliff

label jhfs5d:
    J"""I am strong, I can fend them all!
    
    (As the two agents rapidly approach, I tighten my grip on the bat, ready to face them head-on.)
    
    (I have to choose who I should target first.)"""
    
    menu:
        "The one on the right":
            jump jhfs5i
        "The one on the left":
            jump jhfs5j

label jhfs5e:
    J"""(I decided that i should call my teammates for help)
    
    (who should I call?)"""
    menu:
        "Quol":
            jump jhfs5l
        "Renee":
            jump jhfs5m

label jhfs5i:
    J"""(I choose to strike the agent on the right, aiming to catch them off guard.)
    
    (but to my surprise, they skillfully block my attack.)"""
    
    show screen timerDown(3, "misseditJHFS5i1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block", "choice1JHFS5i1", 0.2, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5i1:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i1
    
    label choice1JHFS5i1:
        "(I block the agent.)"
        jump finishedJHFS5i1
    
    
    label finishedJHFS5i1:
        show screen timerDown(3, "misseditJHFS5i2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Parry", "choice1JHFS5i2", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5i2:
        "(I get striked by the Agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i2
    
    label choice1JHFS5i2:
        "(I parry the agent's strike.)"
        jump finishedJHFS5i2
    
    
    label finishedJHFS5i2:
        show screen timerDown(3, "misseditJHFS5i3")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Dodge", "choice1JHFS5i3", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5i3:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5i3
    
    label choice1JHFS5i3:
        "(I dodge the agent's strike.)"
        jump finishedJHFS5i3
    
    
    label finishedJHFS5i3:
        """(Amidst the flurry of blows, I spot a brief opening—a split second where the agent's guard wavers.)
        
        S(eizing the opportunity, I deliver a powerful swing, channeling all my strength into the strike. )
        
        T(he bat connects with a resounding impact, sending the agent sprawling to the ground.)
        
        (As I try to turn my attention to the Second Agent, I found out Quol has already taken care of him)"""
    jump jhfs5k

label jhfs5j:
    """(I choose to strike the agent on the left, aiming to catch them off guard.)
    
    (The bat strikes the Agent, and he seems to be stunned)
    
    (He swings at me sluggishly, trying to hit me down)"""
    
    show screen timerDown(3, "misseditJHFS5j1")  # seconds, label to jump on fail
    call screen qte_choice([
        ("Block", "choice1JHFS5j1", 0.2, 0.3),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5j1:
        "(I get striked by the agent)"
        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
        jump finishedJHFS5j1
    
    label choice1JHFS5j1:
        "(I block the agent.)"
        jump finishedJHFS5j1
    
    
    label finishedJHFS5j1:
        show screen timerDown(3, "misseditJHFS5j2")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Swing", "choice1JHFS5j2", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5j2:
        J"(I miss the swing.)"
        jump finishedJHFS5j2
    
    label choice1JHFS5j2:
        J"(I striked the Agent and he falls down on the floor.)"
        jump finishedJHFS5j3
    
    
    label finishedJHFS5j2:
        show screen timerDown(3, "misseditJHFS5j3")  # seconds, label to jump on fail
        call screen qte_choice([
            ("Swing again", "choice1JHFS5j3", 0.2, 0.3),  # xpos and ypos for choice 1
        ])
        return
    
    label misseditJHFS5j3:
        J"(I get striked by the agent)"

        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over
         
        """(From a distance, a thin string appears in front of my eyes, violently hitting the agent down)
         
        (Renee assisted me in taking him down)"""
        jump finishedJHFS5j3
    
    label choice1JHFS5j3:
        J"(I striked the Agent and he falls down on the floor.)"
        jump finishedJHFS5j3
    
    
    label finishedJHFS5j3:
        J"(I try to turn my attention to the Second Agent, I found out Renee has already taken care of him)"
    
    jump jhfs5k

label jhfs5k:
    show Julia exhausted at textbox_over
    hide screen display_hp
    J"We have managed to knock out all the agents in the venue"
    jump cliff

label jhfs5l:
    J"""(I call out for Quol)
    
    Quol! Please help!
    
    (Quol, ever vigilant and quick to respond, turns their attention toward me.)"""

    hide Julia with Dissolve(0.3)
    Q"Coming!"
    
    show Quol Angry at center_lower with Dissolve(0.3)
    J"""(Their eyes meet mine, and without hesitation, they rush to my aid.) 
     
    (With a swift and powerful roundhouse kick, Quol unleashes an force upon the agent, targeting their head with precision.) 
    
    (The impact reverberates through the air as the agent's body crumples under the sheer force of the blow.)"""
    
    Q"Finish off the last one, Julia. I have my own agent to beat up."
    
    hide Quol with Dissolve(0.3)

    jump jhfs5o

label jhfs5o:
    J"(Taking the hint, I raised my bat high.)"
    
    show screen timerDown(3, "misseditJHFS5o")  # seconds, label to jump on fail
    call screen qte_choice([
        ("SLAM", "choice1JHFS5o", 0.5, 0.5),  # xpos and ypos for choice 1
    ])
    return
    
    label misseditJHFS5o:
        show Julia traumatized at textbox_over
        J"""I hesitated and missed my shot.

        The agent hits my shoulder"""

        $ hp -= 3
        if hp <= 0:
            # If hp is 0, jump to the game_over label
            jump game_over

        J"""Renee notices and swings her whip towards the agent's legs, while Quol does the final blow
        
        Their eyes gleam with a mix of understanding and dissappointment."""
        jump finishedJHFS5o
    
    label choice1JHFS5o:
        J"I striked down at the last agent, delivering a fatal blow."
        jump finishedJHFS5o
    
    label finishedJHFS5o:
    jump jhfs5k

label jhfs5m:
    J"""(I call out for Renee)
    
    Renee! Please help!
    
    (Without hesitation, Renee responds to my plea, her eyes locking onto the remaining agent.) """
    hide Julia with Dissolve(0.3)
    R "Alright! Stay back!"
    show Renee at center_lower with Dissolve(0.3)
    J"""(She swiftly maneuvers her whip, seamlessly striking with precision.)
    
    (With a deft flick of her wrist, the whip cracks through the air, its tip finding its mark.) 
     
    (In a dazzling display of skill, Renee incapacitates the agent, rendering them unable to continue their assault.) 
    
    (The agent's movements falter, and they crumble to the ground, immobilized by the force of the whip.)"""
    
    R "I'll help you more later, I'm taking on another agent as well! Try manage the last one yourself!"

    hide Renee with Dissolve(0.3)
    
    jump jhfs5o

label cliff:
    J"""We all stared at our target- the entrance of the concert
    
    As quick as our legs can take us, we sprinted towards it."""

    hide Julia

    show Lenorra at center_lower with Dissolve(0.3)

    LQ"Not so fast, traitors."

    J"We immediately halted and braced oursleves for combat."

    "..."
    hide Lenorra with Dissolve(0.3)
    show bg black with fade
    "..."

    Z"""I haven't finished writing the best part yet!
    
    You guys are here too early!
    
    oh well credits roll."""
    window hide
    call screen credits
    return



label game_over:
    hide Julia
    hide Quol
    hide Renee
    hide Lenorra
    hide Andrew
    hide Agent1
    show bg black with fade
    show text "{size=100}{color=#ff0000}BAD END{/color}{/size}\n{size=30}{color=#ffffff}you died{/color}{/size}" at truecenter with dissolve
    pause 5.0
    hide text with dissolve
    Z"""Huh, you're down
    
    that wasn't fun.

    Not a great way to end a story, is it?

    let's try this again."""
    $ hp == 15
    return


label badend:
    show bg black with fade
    show text "{size=100}{color=#ff0000}BAD END{/color}{/size}\n{size=30}{color=#ffffff}you were caught{/color}{/size}" at truecenter with dissolve
    pause 5.0
    hide text with dissolve

    Z"""Ah, what a tragedy.
    
    However.. it's quite a brillant show.

    What a shame it ends this way.
    
    Let's restart this play, shall we?"""

    return
