###########################################################
# "Antimemetics Division Hub" by qntm, from the SCP Wiki. Source: https://scp-wiki.wikidot.com/antimemetics-division-hub. Licensed under CC-BY-SA.
###########################################################

label start:

    scene bg start

    "\"{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub\" by {a=https://scp-wiki.wikidot.com/qntm-s-author-page}qntm{/a}, from the SCP Wiki. Source: {a=https://scp-wiki.wikidot.com/antimemetics-division-hub}https://scp-wiki.wikidot.com/antimemetics-division-hub{/a}. Licensed under {a=https://creativecommons.org/licenses/by-sa/3.0/}CC-BY-SA{/a}."

    """An {noalt}antimeme{/noalt}{alt}anti-meme{/alt} is an idea with self-censoring properties; an idea which, by its intrinsic nature, discourages or prevents people from spreading it.

    {b}{noalt}Antimemes{/noalt}{alt}anti-memes{/alt} are real.{/b} Think of any piece of information which you wouldn't share with anybody, like passwords, taboos and dirty secrets.

    Or any piece of information which would be difficult to share even if you tried: complex equations, very boring passages of text, large blocks of random numbers, and dreams…

    But anomalous {noalt}antimemes{/noalt}{alt}anti-memes{/alt} are another matter entirely.

    How do you contain something you can't record or remember? How do you fight a war against an enemy with effortless, perfect camouflage, when you can never even know that you're at war?"""

    "Welcome to the {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division."

    "No, this is not your first day."

    if persistent.firstrun: 
        jump quick_play

    menu hub_root:
        "{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub"

        "There is No Antimemetics Division" if !persistent.firstrun: 
            jump hub_division

        "Five Five Five Five" if !persistent.firstrun: 
            jump hub_five

    return

    menu hub_division: 
        "There is No Antimemetics Division"

        "We Need to Talk About {noalt}Fifty-Five{/noalt}{alt}fifty five{/alt}" if persistent.talk:
            call talk

        "Introduction to {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt}" if persistent.intro:
            call intro

        "Unforgettable, That's What You Are" if persistent.lake: 
            call lake

        "CASE COLOURLESS GREEN" persistent.green:
            call green

        "Your Last First Day" persistent.first: 
            call first

        "Back":
            jump hub_root

    jump hub_division

    menu hub_five: 

        "Five Five Five Five"

        "Where Have You Been All My Life" if persistent.where: 
            call coming_soon

        "Back": 
            jump hub_root

label coming_soon: 

    "Coming soon"

    return

label quick_play: 

    $persistent.firstrun = False

    call scp_055

    call talk

    call intro 

    call lake 

    call green 

    call first

    # This ends the game.

    return