# Variables
define persistent.firstrun = True

define persistent.talk = False 
define persistent.intro = False
define persistent.lake = False
define persistent.green = False
define persistent.first = False

define persistent.where = False
define persistent.fresh = False

default marion_surname = "Wheeler"

##########################################################
# characters 
##########################################################

define marion = Character("Marion [marion_surname]", what_prefix="\"", what_suffix="\"", who_alt="Marion says, ")
define marion_t = Character("Marion [marion_surname]", what_italic=True, who_alt="Marion thinks, ")
define o5_8 = Character("O5-8", what_prefix="\"", what_suffix="\"", who_alt="O five eight says, ")
define kim = Character("Paul Kim", what_prefix="\"", what_suffix="\"", who_alt="Kim says, ")
define kim_t = Character("Paul Kim", what_italic=True, who_alt="Kim thinks, ")
define adam = Character("Adam Wheeler", what_prefix="\"", what_suffix="\"", who_alt="Adam says, ")

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

define marion_p = Character("Past Marion", what_prefix="\"", what_suffix="\"", who_alt="Past Marion says, ")

# story 5: first 

define scp3125 = Character("SCP-3125", what_prefix="\"", what_suffix="\"", who_alt="SCP three one two five says, ")
define scp3125_a = Character("Infected Not-Person", what_prefix="\"", what_suffix="\"", who_alt="An Infected Not-Person says, ")

# story 6: where 

define gauss = Character("Alex Gauss", what_prefix="\"", what_suffix="\"", who_alt="Gauss says, ")

##########################################################
# images 
##########################################################

image marion = Placeholder('girl')
image kim = Placeholder('boy')
image o5_8 = Placeholder('boy')
image adam = Placeholder('boy')

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