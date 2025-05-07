from turtle import *

speed(fastest)
for i in range(-100, 100, 100):
  penup()
  setposition(i, 100)
  pendown()
  goto(i, -100)
