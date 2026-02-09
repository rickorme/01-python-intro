'''
5 Turtle graphics
Python har ett paket med inbyggda, enkla funktioner för grafik: turtle.
Tänk dig att du har en robotarm som håller en penna mot ett papper.
Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
backward - gå bakåt
left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
dot - sätt ut en prick med en viss storlek
speed - normal=6, fast=10, maximal=0
'''
import turtle as t
import math

def example_code():
    # Upprepa 3 gånger
    for x in range(3):
        t.forward(100)
        t.left(120)

    # Lyft pennan för att flytta utan att rita
    t.penup()
    t.forward(200)
    t.pendown()
    t.dot(10, "red")
    t.color("blue")
    t.forward(50)

    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()

'''
1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
'''
def draw_square(side_length: int):

    t.pendown()
    for x in range(4):
        t.forward(side_length)
        t.left(90)
    # t.mainloop()

'''
2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. 
Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
for x in range(5):
    t.square()
    t.move_next()
'''
def move_right(distance):
    t.penup()
    t.setheading(0)
    t.forward(distance)

def draw_5_squares():
    for x in range(5):
        draw_square(100)
        move_right(120)

'''
3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
Tips 1: vad händer om man varierar värdet på range? 
Tips 2: 360 grader motsvarar ett helt varv.
'''
def draw_circle():
    t.goto(0,0)
    t.pendown()
    t.speed(200)
    for x in range(360):
        t.forward(2)
        t.right(1)

"""
4
"""
# Setup
screen = t.Screen()
# t = t.Turtle()
t.speed(3)
t.pensize(5)

# Constants for our "Grid"
LETTER_WIDTH = 60
LETTER_HEIGHT = 100
X_OFFSET = 100  # Distance between the start of each letter
START_Y = 0     # Constant baseline


def reset_position(x, y):
    """Lifts pen and moves turtle to an absolute coordinate."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)  # Always face right to start
    t.pendown()


def draw_P(x, y):
    reset_position(x, y)
    t.setheading(90)
    t.forward(LETTER_HEIGHT)
    t.right(90)
    t.circle(-25, 180)


def draw_Y(x, y):
    reset_position(x, y + LETTER_HEIGHT)  # Start top left
    t.goto(x + (LETTER_WIDTH // 2), y + (LETTER_HEIGHT // 2))  # To middle
    t.goto(x + LETTER_WIDTH, y + LETTER_HEIGHT)  # To top right
    reset_position(x + (LETTER_WIDTH // 2), y + (LETTER_HEIGHT // 2))
    t.goto(x + (LETTER_WIDTH // 2), y)  # Down to bottom center


def draw_T(x, y):
    reset_position(x + (LETTER_WIDTH // 2), y)
    t.goto(x + (LETTER_WIDTH // 2), y + LETTER_HEIGHT)
    reset_position(x, y + LETTER_HEIGHT)
    t.goto(x + LETTER_WIDTH, y + LETTER_HEIGHT)


def draw_H(x, y):
    reset_position(x, y)
    t.setheading(90);
    t.forward(LETTER_HEIGHT)
    reset_position(x, y + (LETTER_HEIGHT // 2))
    t.setheading(0);
    t.forward(LETTER_WIDTH)
    reset_position(x + LETTER_WIDTH, y)
    t.setheading(90);
    t.forward(LETTER_HEIGHT)


def draw_O(x, y):
    """Creates a perfect, upright oval using shapesize and stamp."""
    t.penup()
    # Move to the center of the bounding box
    center_x = x + (LETTER_WIDTH // 2)
    center_y = y + (LETTER_HEIGHT // 2)
    t.goto(center_x, center_y)

    # Change to circle and stretch
    # shapesize(stretch_wid, stretch_len, outline)
    # Default is 20px, so we divide our target size by 20
    t.shape("circle")
    t.fillcolor("white")
    t.shapesize(LETTER_HEIGHT / 20, LETTER_WIDTH / 10, 5)

    # Use stamp to 'draw' the shape onto the canvas
    t.stamp()

    # Reset turtle for the next letter
    t.shapesize(1, 1)
    t.shape("classic")
    t.pendown()


def draw_N(x, y):
    reset_position(x, y)
    t.setheading(90);
    t.forward(LETTER_HEIGHT)
    t.goto(x + LETTER_WIDTH, y)
    t.forward(LETTER_HEIGHT)


def draw_python(start_x):
    """Draws PYTHON by calculating the X for each letter."""
    print("Made with vibe-coding!")
    letters = [draw_P, draw_Y, draw_T, draw_H, draw_O, draw_N]

    current_x = start_x
    for letter_func in letters:
        letter_func(current_x, START_Y)
        current_x += X_OFFSET  # Increment X for the next letter
    t.mainloop()

draw_square(300)
t.clear()
draw_5_squares()
t.clear()
draw_circle()
t.clear()
draw_python(-300)