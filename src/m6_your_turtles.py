"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jun Fan.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

a = rg.SimpleTurtle('turtle')
a.pen = rg.Pen('red', 2)
a.speed = 20

b = rg.SimpleTurtle('turtle')
b.pen = rg.Pen('blue', 2)
b.speed = 20

b.pen_up()
b.forward(50)
b.pen_down()
a.right(15)
b.right(165)
for k in range(5):

    a.forward(60)
    a.right(150)

    b.forward(60)
    b.left(150)

    a.forward(60)
    a.left(150)

    b.forward(60)
    b.right(150)

size = 10
for j in range(30):

    b.left(30)
    b.forward(size)
    size = size+2

c = 5
for j in range(60):

    a.left(15)
    a.forward(c)
    c = c+1

window.close_on_mouse_click()


###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
