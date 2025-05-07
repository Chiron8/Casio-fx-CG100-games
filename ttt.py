from turtle import *

pos = [[0, 0], [-100, -60], [-20, -60], [75, -60], [-100, -10], [-20, -10], [75, -10], [-100, 40], [-20, 40], [75, 40]]
turn = 0
won = False
key= 0
speed(10000)
for i in [-50, 50]:
  penup()
  setposition(i, 75)
  pendown()
  goto(i, -75)

for j in [-25, 25]:
  penup()
  setposition(-125, j)
  pendown()
  goto(125, j)

penup()
while won == False:
	key = input("Enter Key: ")
    setposition(pos[key])
    pendown()
    goto(xcor()+10, ycor()+10)
    
