''' The below python code draws up my initials that is N and K by using python graphics module. As there are 2 initials
 i have created 2 methods for them each. In first method it draws N and in second it draws K.'''

import turtle #This line imports the turtle module from python library


def draw_n():
    window=turtle.Screen() #this line creates a screen or canvas for drawing
    window.bgcolor('red') #this sets the background color of the screen to red
    brad=turtle.Turtle()  #this line creates our instance of class Turtle
    brad.shape('turtle')  #this line sets the shape of turtle to actual turtle, default shape is arrow
    brad.right(90)        #right and left method take angle as an argument either in degrees or in radians
                          # by default it's in degrees,forward method takes distance as an argument
    brad.forward(100)
    brad.right(90)
    brad.right(90)
    brad.forward(100)
    brad.right(135)
    brad.forward(150)
    brad.left(135)
    brad.forward(110)
    draw_k()           #we have to call draw_k() from the span of draw_n() otherwise it gives an error, i haven't
                        # found the reason yet,but will update the file after finding it.


def draw_k():
    window=turtle.Screen()
    window.bgcolor('red')
    amol=turtle.Turtle()
    amol.shape('turtle')
    amol.up()          #this up() method is really intresting, it moves your turtle without drawing on the screen.
                        # in python you actually draw with a pen,so,when you call up method, you,basically lift the pen
                        # from the screen and become invisible.
    amol.goto(130,0)   #goto method takes x and y co-ordinates as input and moves your turtle to position specified
    amol.down()     #Before, we have lifted the pen up so now we put it down to start drawing again. It's really amazing
                    #how this method works.!!!
    amol.right(90)
    amol.forward(100)
    amol.back(50)   #back() method goes backwards by taking distance as an argument.
    amol.left(135)
    amol.forward(70)
    amol.back(70)
    amol.right(90)
    amol.forward(70)

    window.exitonclick() #this will close the window upon clicking with a mouse for once.

draw_n()
