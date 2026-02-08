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

'''
3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
Tips 1: vad händer om man varierar värdet på range? 
Tips 2: 360 grader motsvarar ett helt varv.
'''

# for x in range(5):
#     draw_square(100)
#     move_right(120)

for x in range(360):
    t.forward(2)
    t.right(1)


t.mainloop()