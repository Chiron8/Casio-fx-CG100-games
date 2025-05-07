from turtle import *
#variables
pos = [[0, 0], [-100, -60], [-20, -60], [75, -60], [-100, -10], [-20, -10], [75, -10], [-100, 40], [-20, 40], [75, 40]]
plays = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
turn = 0
won = 2
key= 0

#turtle config
speed("fastest")
pencolor("black")
width(3)
hideturtle()

#grid
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

#pause
penup()
for i in range(1, 10):
    goto(-100, -100)
    goto(100, 100)

#main loop
while won == 2:
  penup()
  pencolor("black")
  for i in range(1, 10):
    goto(-100, -100)
    goto(100, 100)
  key = int(input("Enter Key: "))
  if plays[key] == 2:
    setposition(pos[key][0], pos[key][1])
    pendown()
    if turn == 1:
      pencolor("orange")
      goto(xcor()+10, ycor()+10)
      penup()
      setposition(xcor()-10, ycor())
      pendown()
      goto(xcor()+10, ycor()-10)
      turn = 0
      plays[key] = 1
      penup()
    elif turn == 0:
      pencolor("blue")
      goto(xcor()+10, ycor())
      goto(xcor(), ycor()+10)
      goto(xcor()-10, ycor())
      goto(xcor(), ycor()-10)
      turn = 1
      plays[key] = 0
      penup()

    pencolor("red")
    for i in range(1, 9):
      if i == 1 or i == 4 or i == 9:
        if plays[i] == plays[i+1] == plays[i+2] and plays[i] != 2:
          won = plays[i]
          setposition(pos[i][0]+5, pos[i][1]+5)
          pendown()
          goto(pos[i+2][0]+5, pos[i+2][1]+5)
          penup()
      if i == 7 or i == 8 or i == 9:
        if plays[i] == plays[i-3] == plays[i-6] and plays[i] != 2:
          won = plays[i]
          setposition(pos[i][0]+5, pos[i][1]+5)
          pendown()
          goto(pos[i-6][0]+5, pos[i-6][1]+5)
          penup()
      if i == 1:
        if plays[i] == plays[i+4] == plays[i+8] and plays[i] != 2:
          won = plays[1]
          setposition(pos[i][0]+5, pos[i][1]+5)
          pendown()
          goto(pos[i+8][0]+5, pos[i+8][1]+5)
          penup()
      if i == 7:
        if plays[i] == plays[i-2] == plays[i-4] and plays[i] != 2:
          won = plays[7]
          setposition(pos[i][0]+5, pos[i][1]+5)
          pendown()
          goto(pos[i-4][0]+5, pos[i-4][1]+5)
          penup()
  else:
    print("Already played, try again")

for i in range(1, 10):
    goto(-100, -100)
    goto(100, 100)

if won == 0:
  print("Noughts has won!")
else:
  print("Crosses has won!")
x = input()
    
    
