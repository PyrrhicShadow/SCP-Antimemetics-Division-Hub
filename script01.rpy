###########################################################
# We Need To Talk About Fifty-Five
# https://scp-wiki.wikidot.com/we-need-to-talk-about-fifty-five
# story by qntm on SCP-wiki
# (https://scp-wiki.wikidot.com/qntm-s-author-page)
##########################################################

# Unique characters 
define receptionist = Character("Receptionist", what_prefix="\"", what_suffix="\"", who_alt="The receptionist says, ")
define clay = Character("Clay", what_prefix="\"", what_suffix="\"", who_alt="Clay says, ")

# Story Starts

label talk:

    scene bg start

    "Part 1: There is No {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division"

    "We Need to Talk About {noalt}Fifty-Five{/noalt}{alt}fifty five{/alt}"

    scene bg admin reception

    show marion at offleft
    show receptionist at offright

    marion "Can I smoke?"

    "This time the receptionist narrows her eyes at Marion."

    receptionist """No.

    You— No, you can't smoke anywhere on Site 200.

    Just because it's an administration building doesn't mean we don't have lungs.

    Or labor law."""

    "Marion notices the exasperation on the young woman's face."

    marion "I've asked you that before, haven't I?"

    receptionist "Twice in the last quarter-hour. You must really need a smoke."

    "She's genuinely puzzled at the repeated question, and she's doing a bad job of concealing her puzzlement."

    marion """You think this is like {i}Memento{/i}, don't you?

    You think I have no long-term memory, and if I stay in one place for too long I forget why I'm there."""

    "The receptionist is only just old enough to remember that film."

    receptionist "I… guess?"

    "Marion smiles sympathetically and shakes her head. It's nothing so simple."

    hide receptionist
    show marion at center

    """Minutes pass. She toys obsessively with her lighter.

    She is turning fifty this year and slowly greying, well on her way out of \"petite\" towards \"little old lady\".

    In her bag her phone beeps because it's time for a pill, but she tells it to remind her later.

    There is a slight tremble in her fingers, but that's not age-based infirmity, that's just ordinary nerves.

    She's nervous because she's here to meet an O5, and {noalt}O5s{/noalt}{alt}O fives{/alt} are scary.

    {noalt}O5s{/noalt}{alt}O fives{/alt} never want to see you for a small thing. It's the end of the world, or nothing."""

    """Finally, forty minutes late, the door to the inner office opens. Four or five high-ranked Foundationers spill out, carrying laptops or briefcases.

    As a group, they head straight past reception and out to cars which are waiting.  Marion recognises a few of the faces— the Site 19 site director, the head recruiter for Western Europe.

    None of them glance in her direction."""

    show clay at right

    """Once they're gone, {noalt}O5-8's{/noalt}{alt}O five eight's{/alt} assistant pokes his head around the door.

    He's twenty-something, improbably youthful, like a teenager stuffed into one of his dad's business shirts. His haircut is barely regulation.

    In one hand he holds a tablet computer showing his boss's day planner. It's packed. The man evidently does not sleep."""

    clay "Marion? You can come through now."

    scene bg admin office

    """The office door closes behind them with an unusually heavy mechanical clunk, as if the whole thing is part of a machine built into the office walls.

    While Marion takes the indicated chair and sets her bag down, the assistant turns and does some confusing additional things to the door, causing it to make several further strange noises.

    {noalt}O5s{/noalt}{alt}O fives{/alt} have non-trivial privacy and security requirements."""

    """The office is spacious, but somehow contrives to be dark despite two big corners of window and broad daylight outside.

    The walls are all bookshelves and dark wood panelling; perfectly stylish, but a style from the Nineties, a little worn, and not yet old enough to be fashionable again."""

    "As for the fellow behind the desk, well, an O5 never looks like you imagine."

    show marion at center
    show o5_8 at offright

    "Marion takes a deep breath."

    marion "So what's the topic? All I got was the meeting invitation, no agenda or subject."

    marion "I mean, an O5 says 'jump', you jump, but—"

    show clay at centerleft

    """Looking to her right, she notices that the assistant, without saying anything or making any undue noise, has set his tablet down on a table, produced a gun and aimed it at her head.

    Marion stops talking.

    She sits still in her chair for a little while, absorbing the change of pace, letting her heart rate rise to a hummingbird's and then start to flatten again."""

    marion "Okay?"

    """She licks her lips and grips the arm rests, otherwise staying perfectly still, waiting for another prompt.

    The assistant's face is totally neutral now, like this is just how meetings go. Maybe it is, for people up here."""

    o5_8 "Who are you?"

    "Marion blinks."

    marion """What?

    Oh, God."""

    o5_8 """Let me rephrase. Marion Wheeler, forty-nine, with loving husband and two boys in tow.

    Likes camping, hiking and ornithology. Boring mother with perfect, airtight background and financials, as far back as we can examine.

    And you've got full Foundation credentials which we've never issued, including access to a list of installations and rooms which…

    some of these locations don't exist, or were torn down decades ago. At least one hasn't been built yet, yet you've got the front door key to it.

    That's before we get to your SCP access control lists, which I can only term as 'egregious'.

    So you're a spy, and your objectives are misaligned with ours, and Clay wanted to cut Xi-3 loose on you, but I was able to bring him around.

    I talked him into a face-to-face. I thought there was a slim chance that if we locked you in a bomb-proof room and asked politely, you'd have the good sense to spare yourself 'the rest'."""

    "Marion has long since stopped listening."

    marion "You dullard. I'm your chief of {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt}."

    clay "We don't have an {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division."

    marion "Yes, you do. We do."

    o5_8 "We have a Memetics Division, a {noalt}Telekontainment{/noalt}{alt}tele-containment{/alt} Division, Fire Services, Ops-A, Ops-B, Personnel, D-personnel and two dozen others."

    o5_8 "We don't have an {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division."

    marion "Do we have an Irony Division?"

    "Marion hesitates hopefully."

    marion "No? Alright. Well, try this: why do you think the {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division would show up in the listing?"

    clay "This is just a cover story."

    "Clay says this to {noalt}O5-8{/noalt}{alt}o five eight{/alt}, not taking his eyes off Marion."

    clay "It's a good one, but she's had it worked out in advance."

    o5_8 "Clay, lose the piece."

    show clay at left

    "Grudgingly, Clay does so. Marion relaxes fractionally."

    marion """There are SCPs with dangerous memetic properties. There are contagious concepts which require containment just like any physical threat.

    They get inside your head, and ride your mind to reach other minds. Right?"""

    o5_8 "Right."

    "He could name a score of {noalt}SCPs{/noalt}{alt}S C peas{/alt} fitting this description without even thinking."

    marion """There are SCPs with {noalt}antimemetic{/noalt}{alt}anti-memetic{/alt} properties. There are ideas which cannot be spread.

    There are entities and phenomena which harvest and consume information, particularly information about themselves.

    You take a Polaroid photo of one, it'll never develop.

    You write a description down with a pen on paper and hand it to someone— but what you've written turns out to be hieroglyphs, and nobody can understand them, not even you.

    You can look directly at one and it won't even be invisible, but you'll still perceive nothing there.

    Dreams you can't hold onto and secrets you can never share, and lies, and living conspiracies.

    It's a conceptual subculture, of ideas consuming other ideas and… sometimes… segments of reality. Sometimes, people. Which makes them a threat.

    That's all there is to it, really.

    {noalt}Antimemes{/noalt}{alt}anti-memes{/alt} are dangerous, and we don't understand them; therefore, they are part of the Problem. Hence my division.

    We can do the sideways thinking that's needed to combat something which can literally eat your combat training."""

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} stares back at her for a long moment."

    "Clay fidgets, disliking and distrusting the story, but the O5 seems more open to the concept."

    o5_8 "Name one. Name an {noalt}antimemetic{/noalt}{alt}anti-memetic{/alt} SCP."

    marion "SCP-055."

    clay "There is no SCP-055."

    marion "Again: Yes, there is."

    clay """There isn't.

    SCP numbers aren't assigned sequentially. There are gaps. That number hasn't been assigned.

    It's not superstition, we have enough to be concerned about without arbitrary numerological mysticism.

    We have SCP-666 and SCP-013. But there's no SCP-001.

    And there's no SCP-055."""

    o5_8 "Clay, you should look at this."

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} turns his monitor so Clay can see the file that he has just retrieved. Clay bends over and reads it from top to bottom."

    "Stunned, he scrolls back and reads it all a second time."

    clay "But…"

    o5_8 """The file's dated from 2008. It's got all the right flags and signatures. It's keyed and coded.

    It's real."""

    clay "You've seen this before?"

    o5_8 """Never in my life. As far as I can remember, anyway.

    On the other hand, if the content is accurate, both of us have probably seen it dozens of times."""

    "Clay glares at Marion."

    clay "This isn't possible."

    "Marion nearly spits."

    marion "For Christ's sake, Clay, how long have you been working here?"

    clay "But if this SCP is this powerful…"

    marion "Yes?"

    "The O5 finishes Clay's question for him."

    o5_8 """Who wrote the file?

    And for that matter, how was the interview conducted, and who is 'Bartholomew Hughes'?

    And most importantly, how do you, Mrs. Wheeler, retain knowledge of any of this?"""

    marion "Bart Hughes wrote the file. He's dead."

    o5_8 "What happened to him?"

    marion "You don't want to know."

    """There is a very long pause while both {noalt}O5-8{/noalt}{alt}o five eight{/alt} and his assistant react to this.

    In fact, they pass through a long, discrete sequence of reactions.

    Indignation at the seeming rudeness;

    confusion at Wheeler's incaution in front of sinister superiors;

    surprise at the magnitude of the claim;

    pure disbelief;

    comprehension;

    and finally, horror."""

    o5_8 "What… would happen if we did know?"

    marion """It would happen to you as well.

    …As for the rest of your questions: we manage that pharmaceutically.

    You know we have class-A amnestics, for people who very badly need to forget things?

    Of course you do. Who could forget about class-A amnestics?

    Well, in {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt}, we have a different pill, for people who need to remember things that would otherwise be impossible to remember.

    {noalt}Mnestic{/noalt}{alt}nestic{/alt}s, class W, X, Y and Z. Same Greek root as the word 'mnemonic'. The M is silent."""

    "In her bag, her phone beeps again."

    """With a nod of approval from the O5, Marion reaches into her bag and turns her phone off, acknowledging the prompt this time instead of postponing it.

    She pulls a blister pack from another pocket and pops a pill out. It's hexagonal, and green."""

    show cg nmestic w

    """She holds it up, and is satisfied to see a flicker of recognition on {noalt}O5-8's{/noalt}{alt}o five eight's{/alt} face. He's beginning to put it back together."""

    hide cg

    marion """These are class W {noalt}mnestics{/noalt}{alt}nestics{/alt}, the weakest, suitable for continual use. Two pills per day.

    Go down to the site pharmacy and ask. The pharmacist will claim they don't stock any such thing; they're misremembering, tell them to double-check."""

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} sighs."

    o5_8 "And now, I think, I get it. I see why we're having this conversation at all."

    marion "Yes."

    "She pops a second pill out and hands it over to him."

    marion """It's because you missed a dose.

    You're supposed to be on these, the same as me and everybody on my staff. It's the only way we can work.

    You forgot to take a pill, and then you forgot all the information that the pills were helping you retain.

    You forgot why you were taking them, who gave them to you, where to get more.

    You forgot about me, and my entire department. And now I have to bring you up to speed."""

    o5_8 "And if I take this, I'll remember this whole conversation and we won't have to have it again?"

    marion "Hopefully not."

    clay "Uh, should I be taking those?"

    o5_8 """Sorry, kiddo.

    Need to know. Maybe when you're an O5 yourself."""

    "He swallows the pill. Marion swallows hers too."

    o5_8 "So what is SCP-055?"

    marion """SCP-055 is nothing.

    SCP-055 is, as described in the file, a powerful information autosuppressor.

    As far as experimentation has uncovered, it can only be defined in negative terms. We can only record what it isn't.

    We know it isn't Safe or Euclid. We know it isn't round, or square, or green or silver. We know it isn't stupid. And we know it isn't alone.

    But what we do know is that it's weak.

    It's weak because it's the only {noalt}antimemetic{/noalt}{alt}anti-memetic{/alt} agent in our possession which has a physical entry in the files.

    We have paper records of the thing. We have containment procedures.

    It's not Safe, which means it's dangerous… but it's contained."""

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} blinks."

    o5_8 "You have procedures? Where?"

    "Marion points at her head."

    o5_8 "Then how many other {noalt}antimemes{/noalt}{alt}anti-memes{/alt} are there? How much more dangerous do they get?"

    marion """Ten that I know of. Statistically, probably at least five more that I don't know of.

    This does not count the {noalt}antimemetic{/noalt}{alt}anti-memetic{/alt} entities freely roaming the halls, not under containment.

    There are at least two in this room with us right now. Don't look.

    I said don't look! It's pointless!"""

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} does an impressive job of controlling himself, keeping his attention focused on Marion."

    """Clay doesn't fare so well, and quickly sweeps the whole room, even checking behind his back.

    Making an ass of himself, essentially. He finds nothing. He looks baffled."""

    marion """There is an invisible monster which follows me around and likes to eat my memories. SCP-4987.

    Don't look it up, it's not there.

    I've learned to manage with it. It's like a demanding pet.

    I produce tasty memories on purpose so it doesn't eat something important, like my passwords or how to make coffee."""

    clay "And what's the other one?"

    show clay injured

    """With another nod from {noalt}O5-8{/noalt}{alt}o five eight{/alt}, Marion goes to her bag again.

    This time she pulls out a gun and shoots Clay twice in the heart.

    More aghast than in pain, Clay collapses sharply against the bookcase behind him.

    He pulls his head around to face Marion."""

    clay "How did you— {noalt}kn—{/noalt}{alt}know…{/alt}"

    show clay dead

    "Marion stands, aims more carefully and shoots him a third time, this time in the head."

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt}, again, does an impressive job of not reacting."

    o5_8 "That's Clay's gun. You stole it from him."

    marion "It's tricky to steal a firearm this heavy from someone without them noticing."

    hide clay 
    with dissolve

    "Marion unloads it and carefully sets it down."

    marion """But stealing a firearm and then stealing their memory of the theft is a little easier.

    Like I said: a pet. Some pets are dumb enough that they can be trained."""

    o5_8 """Yes. That much I'd guessed.

    But why?"""

    marion """Because you were supposed to be taking class-W {noalt}mnestics{/noalt}{alt}nestics{/alt}.

    You can't skip a dose of class-W {noalt}mnestic{/noalt}{alt}nestic{/alt}. I've tried.

    You can postpone a dose, but you can't forget unless someone actively prevents you from taking it.

    There's only one person who could get close enough to you to do that, and that's your assistant.

    And remember when I asked him how long he'd been working here?"""

    o5_8 "He didn't answer. I thought you were being rhetorical."

    marion """He doesn't work here. He's an {noalt}antimeme{/noalt}{alt}anti-meme{/alt}.

    Since when do you have an assistant? You don't have an assistant, Brent.

    Look at this office. It's got one desk.

    You've got a receptionist outside: she's the one who screens your calls and schedules your meetings.

    Where does Clay even sit? Where does he fit?

    Don't blame yourself. You're human, and these things are redaction incarnate.

    You need to think like a space alien to get around them."""

    "{noalt}O5-8{/noalt}{alt}o five eight{/alt} asks a question which, in any other workplace, would be absurd."

    o5_8 "Is he dead?"

    marion """Maybe.

    I can put his corpse in our research queue and we'll see what we can see when we open him up.

    There's a duality here, though. They're like parallel universes sharing the same space.

    It's conceptual versus concrete, figurative versus physical. It's very unusual for things to cross over.

    I don't know what Clay was, but he had a human body, which instantly makes him weird, even by our standards.

    As ever, the search for stalemate continues. I will let you know if we get any closer."""

    o5_8 "Any side effects of these pills?"

    marion """Nausea, and dramatically increased risk of pancreatic cancer.

    And very bad dreams."""

    scene bg end

    menu:
        "Up Next: Introductory {noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt}"

        "Next Story":
            jump intro

        "{noalt}Antimemetics{/noalt}{alt}anti-memetics{/alt} Division Hub":
            jump hub
