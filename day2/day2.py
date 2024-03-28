from turtle import *

#we want to paint a house

#step 1: draw a square

speed(5)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door


speed(5)

forward(70)
color("red")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()
color("Red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#second house

width(9)
speed(6)
penup()
goto(-50, -50)
forward(250)
pendown()
left(45)
right(100)
right(94)
forward(200)
right(90)
forward(200)
right(90)
forward(100)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(35)
color("Brown")
begin_fill()
forward(150)
right(102)
forward(168)
end_fill()
penup()
goto(-100, -365)
pendown()
left(138)
forward(100)
right(90)
forward(50)
right(90)
forward(100)

penup()
goto(400, 350)
color("Orange")
begin_fill()
pendown()
circle(100)
end_fill()


penup()
goto(-300, -150)
width(25)
color("Brown")
begin_fill()
pendown()
forward(180)
right(180)
forward(180)
right(90)
color("green")
circle(100)

end_fill()


exitonclick()
