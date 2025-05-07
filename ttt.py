from turtle import *

speed(fastest)
for i in range(50, 150, 50):
  penup()
  setposition(i, 50)
  pendown()
  goto(i, 200)
