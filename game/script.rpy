﻿# The script of the game goes in this file.

# The game starts here.

label start:

    scene bg start

    "\"{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub\" by qntm, from the SCP Wiki. Source: {a=https://scp-wiki.wikidot.com/antimemetics-division-hub}https://scp-wiki.wikidot.com/antimemetics-division-hub{/a}. Licensed under {a=https://creativecommons.org/licenses/by-sa/3.0/}CC-BY-SA{/a}."

    """An {noalt}antimeme{/noalt}{alt}anti-meme{/alt} is an idea with self-censoring properties; an idea which, by its intrinsic nature, discourages or prevents people from spreading it.

    {b}{noalt}Antimemes{/noalt}{alt}anti-memes{/alt} are real.{/b} Think of any piece of information which you wouldn't share with anybody, like passwords, taboos and dirty secrets.

    Or any piece of information which would be difficult to share even if you tried: complex equations, very boring passages of text, large blocks of random numbers, and dreams…

    But anomalous {noalt}antimemes{/noalt}{alt}anti-memes{/alt} are another matter entirely.

    How do you contain something you can't record or remember? How do you fight a war against an enemy with effortless, perfect camouflage, when you can never even know that you're at war?"""


label hub:

    "Welcome to the {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division."

    "No, this is not your first day."

    menu:
        "{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub"

        "Background material: SCP-055":
            jump scp_055

        "We Need to Talk About {noalt}Fifty-Five{/noalt}{alt}fifty five{/alt}":
            jump talk

        "Introduction to {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt}":
            jump intro

        "Unforgettable, That's What You Are": 
            jump lake

        "Exit":
            return

label scp_055:

    "Coming soon"

    menu:
        "Up Next: We Need to Talk About {noalt}Fifty-Five{/noalt}{alt}fifty five{/alt}"

        "Next Story":
            jump talk

        "{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub":
            jump hub

    # This ends the game.

    return

label coming_soon: 

    "Coming soon"

    return