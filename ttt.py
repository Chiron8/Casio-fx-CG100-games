from turtle import *

pos = [[0, 0], [-100, -60], [-20, -60], [75, -60], [-100, -10], [-20, -10], [75, -10], [-100, 40], [-20, 40], [75, 40]]
plays = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

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
	if plays[key] == 2:
		  	setposition(pos[key])
  			pendown()
		if turn == 1:
  			goto(xcor()+10, ycor()+10)
			penup()
			setposition(xcor()-10, ycor())
			pendown()
			goto(xcor()+10, ycor()-10)
			turn = 0
		if turn == 0:
			goto(xcor()+10, ycor())
			goto(xcor(), ycor()+10)
			goto(xcor()-10, ycor())
			goto(xcor(), ycor()-10)
			turn = 1
	else:
		print("Already played, try again")
	
    
