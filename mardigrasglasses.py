"""
Take your Adafruit Led Glasses Starter Kit to Mardi Gras!
https://www.adafruit.com/product/5255

and just grab on of these little guys for plenty of power: 
https://www.adafruit.com/product/4236
"""
import time
import board
import random
import adafruit_is31fl3741
from adafruit_is31fl3741.adafruit_ledglasses import LED_Glasses

i2c = board.I2C()

# Initialize the IS31 LED driver, buffered for smoother animation
glasses = LED_Glasses(i2c, allocate=adafruit_is31fl3741.MUST_BUFFER)
glasses.show()  # Clear any residue on startup
glasses.global_current = 100


# Yay sloppy globals
# TODO: fix sloppy globals
purple = 0x9000b0
green  = 0x009000
gold   = 0x909000
colors = (purple, green, gold)

# edit these for your local parade!
messages = [
    'HAPPY MARDI GRAS',
    'THROW ME SOMETHING MISTER',
    'HAIL ENDYMION',
    'MID-CITY >'
]
old_msg = []

# TODO: moar letters!
letters = {
    'A': (((1,2,3,4),(0,2),(0,2),(1,2,3,4)), 4),
    'B': (((0,1,2,3,4),(0,2,4),(0,2,4),(1,3)), 4),
    'C': (((1,2,3),(0,4),(0,4),(1,3)), 4),
    'D': (((0,1,2,3,4),(0,4),(0,4),(1,2,3)), 4),
    'E': (((0,1,2,3,4),(0,2,4),(0,2,4),(0,4)), 4),
    'F': (((0,1,2,3,4),(0,2),(0,2),(0,)), 4),
    'G': (((1,2,3),(0,4),(0,2,4),(2,3)), 4),
    'H': (((0,1,2,3,4),(2,),(2,),(0,1,2,3,4)), 4),
    'I': (((0,4),(0,1,2,3,4),(0,4)), 3),
    'J': (((3,),(4,),(4,),(0,1,2,3)), 4),
    'K': (((0,1,2,3,4),(2,),(1,3),(0,4)), 4),
    'L': (((0,1,2,3,4),(4,),(4,)), 3),
    'M': (((0,1,2,3,4),(0,),(1,2),(0,),(0,1,2,3,4)), 5),
    'N': (((0,1,2,3,4),(1,),(2,),(0,1,2,3,4)), 4),
    'O': (((1,2,3),(0,4),(0,4),(1,2,3)), 4),
    'P': (((0,1,2,3,4),(0,2),(0,2),(1,)), 4),
    'Q': (((1,2,3),(0,4),(0,3),(1,2,4)), 4),
    'R': (((0,1,2,3,4),(0,2),(0,2,3),(1,4)), 4),
    'S': (((1,4),(0,2,4),(0,2,4),(0,3)), 4),
    'T': (((0,),(0,1,2,3,4),(0,)), 3),
    'U': (((0,1,2,3),(4,),(4,),(0,1,2,3)), 4),
    'V': (((0,1,2),(3,),(4,),(3,),(0,1,2)), 5),
    'W': (((0,1,2,3,4),(4,),(2,3),(4,),(0,1,2,3,4)), 5),
    'X': (((0,4),(1,3),(2,),(1,3),(0,4)), 5),
    'Y': (((0,),(1,),(2,3,4),(1,),(0,)), 5),
    'Z': (((0,3,4),(0,2,4),(0,1,4)), 3),
    ' ': (((),()), 2),
    '-': (((2,),(2,),(2,)),3),
    '>': (((1,2),(0,3),(1,4),(0,3),(1,2)), 5), # heart
    }

def draw_letter(data, pos, grid, color):
    """
    Paint the letter on the screen at its position.
    """
    for (column,data) in enumerate(data):
        for row in data:
            grid.pixel(column+pos, row, color)

def scroll_text(text, grid, color):
    """
    Text Scrolling Generator

    Pop letters off the string and move them across the screen till they're
    off the left side.
    """
    text = list(text)
    screen = []  # Letters on the screen
    while text or screen:
        if screen:
            if (screen[0]['pos'] + screen[0]['data'][1]) <= 1:
                # letter falls off left side
                screen.pop(0)
            if text and ((screen[-1]['pos'] + screen[-1]['data'][1]) < 15):
                # rightmost letter is all the way on the screen,
                # add another letter if any are left
                screen.append({'data': letters[text.pop(0)],
                               'pos': 15})
        else:  # nothing on the screen yet
            screen.append({'data': letters[text.pop(0)],
                           'pos': 15})
        for letter in screen:  # draw the screen
            draw_letter(letter['data'][0], letter['pos'], grid, color)
            letter['pos'] -= 1  # scroll to the left
        grid.show()
        grid.fill(0)
        yield

def colorfade(color, fade):
    """
    scale color towards black by fractional fade amount
    
    this may break if fade > 1
    TODO: make this not break if fade > 1
    """
    r = int(((color&0xff0000)>>16) * fade)
    g = int(((color&0x00ff00)>> 8) * fade)
    b = int( (color&0x0000ff)      * fade)
    return  (r<<16|g<<8|b)
    
def ringcw(ring, pos, fade=1):
    """
    spin a stretch of colors clockwise on the ring
    """
    while ring[pos] > 0:
        ring[(pos+1)%24] = colorfade(ring[pos], fade)
        pos = (pos - 1)%24
    ring[(pos+1)%24] = ring[pos]

def set_cw_color(ring, pos, color):
    """
    prime a fading line of a color on the ring
    """
    for x in range(5):
        ring[(pos-x)%24] = colorfade(color, 1/(2**x))

def ringccw(ring, pos, fade=1):
    """
    spin a stretch of colors widdershins on the ring
    """
    while ring[pos] > 0:
        ring[(pos-1)%24] = colorfade(ring[pos], fade)
        pos = (pos + 1)%24
    ring[(pos-1)%24] = ring[pos]

def set_ccw_color(ring, pos, color):
    """
    prime a fading line of a color on the ring in the other direction
    """
    for x in range(5):
        ring[(pos+x)%24] = colorfade(color, 1/(2**x))
    
def ring_loop(loops):
    """
    spin the mardi gras colors around the rings
    """
    lp = 0
    set_cw_color(glasses.left_ring, lp, purple)
    lg = 8
    set_cw_color(glasses.left_ring, lg, green)
    ly = 16
    set_cw_color(glasses.left_ring, ly, gold)
    rp = 0
    set_ccw_color(glasses.right_ring, rp, purple)
    ry = 8
    set_ccw_color(glasses.right_ring, ry, gold)
    rg = 16
    set_ccw_color(glasses.right_ring, rg, green)

    for count in range(loops*24):
        ringcw(glasses.left_ring, lp)
        ringcw(glasses.left_ring, lg)
        ringcw(glasses.left_ring, ly)
        lp = (lp+1)%24
        lg = (lg+1)%24
        ly = (ly+1)%24

        ringccw(glasses.right_ring, rp)
        ringccw(glasses.right_ring, rg)
        ringccw(glasses.right_ring, ry)
        rp = (rp-1)%24
        rg = (rg-1)%24
        ry = (ry-1)%24
        glasses.show()
        #time.sleep(.05)
        yield

    # fade out
    while glasses.left_ring[lp] > 0:
        ringcw(glasses.left_ring, lp, .8)
        ringcw(glasses.left_ring, lg, .8)
        ringcw(glasses.left_ring, ly, .8)
        lp = (lp+1)%24
        lg = (lg+1)%24
        ly = (ly+1)%24
        ringccw(glasses.right_ring, rp, .8)
        ringccw(glasses.right_ring, rg, .8)
        ringccw(glasses.right_ring, ry, .8)
        rp = (rp-1)%24
        rg = (rg-1)%24
        ry = (ry-1)%24
        glasses.show()
        yield

# Scroll some messages then do some spinny colors!
iter = None
while True:
    if iter == None:
        if messages:
            message = messages.pop(0)
            iter = scroll_text(message, glasses, random.choice(colors))
            old_msg.append(message)
        else:
            messages = old_msg
            old_msg = []
            iter = ring_loop()

    try:
        next(iter)
    except  StopIteration:
        iter = None
        glasses.left_ring.fill(0)
        glasses.right_ring.fill(0)
        glasses.show()