from turtle import *

pos = [[0, 0], [-100, -60], [-20, -60], [75, -60], [-100, -10], [-20, -10], [75, -10], [-100, 40], [-20, 40], [75, 40]]
plays = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

turn = 0
won = False
key= 0
speed(10000)

hideturtle()

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
for i in range(1, 10):
    goto(-100, -100)
    goto(100, 100)

while won == False:
  key = int(input("Enter Key: "))
  if plays[key] == 2:
    setposition(pos[key][0], pos[key][1])
    pendown()
    if turn == 1:
      goto(xcor()+10, ycor()+10)
      penup()
      setposition(xcor()-10, ycor())
      pendown()
      goto(xcor()+10, ycor()-10)
      turn = 0
      plays[key] = 1
      penup()
    if turn == 0:
      goto(xcor()+10, ycor())
      goto(xcor(), ycor()+10)
      goto(xcor()-10, ycor())
      goto(xcor(), ycor()-10)
      turn = 1
      plays[key] = 0
      penup()
    for i in range(1, 10):
        goto(-100, -100)
        goto(100, 100)
  else:
    print("Already played, try again")
  
    
    
