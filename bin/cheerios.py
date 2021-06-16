"""
A program to determine how a mole of Cherrios(TM) would destroy all life.

Works by determining how many Cheerios it would take to cover the Earth
(adding more to the radius to account for existing Cheerios) over and over
again until it can't anymore, then converts from centimeters to kilometers.

Assumptions: 
- cheerio dimensions: 
	- radius: 0.75 cm
	- height: 0.5 cm
- Earth radius: 6,371 km
- packing cheerios: 
	- make a "box" around each cheerio
	- the box will have a radius of 2 * radius of cheerio
"""

from textwrap import dedent # used for formatting later
from math import pi

# ---------------- Constants ----------------
# I will refer to this as "r" in comments:
CHEERIO_RADIUS = 1.5 / 2  # I measured the diameter

# I will refer to this as "h" in the comments
CHEERIO_HEIGHT = 0.5  # Also tasted -- I mean, measured (I mean both):

# I Googled this value (and will refer to it as "R" in comments):
EARTH_RADIUS = 6_371 * (10 ** 5) # n km -> cm = n * 10^5 cm

MOL = 6.022 * (10 ** 23)

# Since Cheerios are circular, we will fit it in the smallest possible box
# (ie, a length and width of the diameter of a cheerio). The area of this
# box will be d^2 = (2r)^2 = 4r^2.
CHEERIO_BOX = 4 * (CHEERIO_RADIUS ** 2)
# -------------------------------------------

def get_cheerios_to_blanket_earth (layer: int) -> float: 
	"""
    Divides Earth (+ layer) surface area by the disgnated box for a cheerio:

    4(pi)(R^2) (cm^2)           1 cheerio box
    -----------------    X    ----------------
           1                   4(r^2) (cm^2)

    Cancel out the 4, and square centimeters, and you get: 

     piR^2                                          pi * (R + (layer * h)^2
    ------    This changes by 1h for every layer:   ----------------------
     r^2                                                    r^2

	"""

	return pi * (EARTH_RADIUS + layer * CHEERIO_HEIGHT)**2 / CHEERIO_RADIUS**2

def convert_cm_to_km (num_cm: float) -> float: 
	"""
    We don't know the result yet, so we have to be general. Here we go...

    n cm      1 m      1 km         n 
    ----- *  -----  *  ------  =  ---- = n * 10^-5 km
      1      100cm     1,000m     10^5

    """
	return num_cm * (10 ** -5)

if __name__ == "__main__":
	cheerios_left = MOL
	layer = 0
	# Get the original number of cheerios needed to cover the Earth
	blanket_number = get_cheerios_to_blanket_earth (layer = layer)

	# Keep subtracting layers of cheerios from the total until we can't anymore
	while cheerios_left >= blanket_number: 
		cheerios_left -= blanket_number # deduct cheerios
		layer += 1 # add another layer
		blanket_number = get_cheerios_to_blanket_earth (layer = layer) # repeat

	# now let's convert 
	shell_in_cm = layer * CHEERIO_HEIGHT
	shell_in_km = convert_cm_to_km (shell_in_cm)

	# Print results
	print (dedent (f"""\
		Layers of Cheerios: {layer:,}
		Height of Cheerios: {shell_in_km} km
		Remaining Cheerios: {cheerios_left}
		Next layer would need: {blanket_number} Cheerios
		    Just needed {blanket_number - cheerios_left} more Cheerios!
	"""))