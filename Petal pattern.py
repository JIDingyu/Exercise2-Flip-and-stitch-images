from turtle import *
screensize(1000,1000,"black")
pensize(10)
speed(10)
pencolor("white")
fillcolor("white")
hideturtle()
penup()
goto(-310,310)
pendown()
for i in range(4):
    fd(630)
    right(90)
pensize(7)
circle(-300,90)
right(90)
circle(-300,90)
right(135)
fd(418)
left(44)
penup()
fd(26)
#left(100)
pendown()
circle(300,90)
left(90)
circle(300,90)
left(135)
fd(419)
penup()
right(133.5)
fd(620)
right(135)
pendown()
fd(418)
right(45)
circle(-300,-90)
right(90)
circle(300,90)
penup()
fd(26)
left(44)
fd(418)
right(180)
pendown()
fd(418)
right(45)
circle(-300,-90)
right(90)
circle(300,90)
penup()
right(180)
fd(300)
right(90)
fd(100)
right(120)
pendown()
circle(-140,118)
penup()
left(149)
fd(631)
right(30)
pendown()
circle(140,-118)
ts=getscreen()
ts.getcanvas().postscript(file="纹样花瓣.eps")

