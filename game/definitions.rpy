# Variables
define persistent.firstrun = True

define persistent.talk = False 
define persistent.intro = False
define persistent.lake = False
define persistent.green = False
define persistent.first = False

define persistent.where = False

##########################################################
# characters 
##########################################################

define wheeler = Character("Marion Wheeler", what_prefix="\"", what_suffix="\"", who_alt="Wheeler says, ")
define wheeler_t = Character("Marion Wheeler", what_italic=True, who_alt="Wheeler thinks, ")
define o5_8 = Character("O5-8", what_prefix="\"", what_suffix="\"", who_alt="O five eight says, ")
define kim = Character("Paul Kim", what_prefix="\"", what_suffix="\"", who_alt="Kim says, ")
define kim_t = Character("Paul Kim", what_italic=True, who_alt="Kim thinks, ")
define unknown = Character("???", what_prefix="\"", what_suffix="\"", who_alt="The stranger says, ")
define note = Character(None, kind=nvl)

# story 1: talk

define receptionist = Character("Receptionist", what_prefix="\"", what_suffix="\"", who_alt="The receptionist says, ")
define clay = Character("Clay", what_prefix="\"", what_suffix="\"", who_alt="Clay says, ")

# story 2: intro

define  grey = Character("Alastair Grey", what_prefix="\"", what_suffix="\"", who_alt="Alastair Grey says, ")

# story 3: lake

define marness = Character("Lyn Marness", what_prefix="\"", what_suffix="\"", who_alt="Marness says, ")

# story 4: green

define wheeler_p = Character("Past Marion Wheeler", what_prefix="\"", what_suffix="\"", who_alt="Past Wheeler says, ")

# story 5: first 

define scp3125 = Character("SCP-3125", what_prefix="\"", what_suffix="\"", who_alt="SCP three one two five says, ")
define scp3125_a = Character("Infected Not-Person", what_prefix="\"", what_suffix="\"", who_alt="An Infected Not-Person says, ")

##########################################################
# images 
##########################################################

image wheeler = Placeholder('girl')
image kim = Placeholder('boy')
image o5_8 = Placeholder('boy')

image bg black = "#000"

# story 1: talk

image receptionist = Placeholder('girl')
image clay = Placeholder('boy')

# story 2: intro

image grey = Placeholder('boy')
image instructor = Placeholder('girl')
image cg scp4739 pt1 = Placeholder('bg')
image cg scp4739 pt2 = Placeholder('bg')

# story 3: lake 

image marness = Placeholder('boy')

##########################################################
# transforms
##########################################################

transform centerleft:
    xalign 0.35

transform centerright:
    xalign 0.7

transform offleft: 
    xalign 0.15

transform offright: 
    xalign 0.85