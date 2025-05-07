from turtle import *

speed(10000)
for i in range(-75, 75, 75):
  penup()
  setposition(i, 75)
  pendown()
  goto(i, -75)

for j in range(-10, 65, 30):
  penup()
  setposition(-125, j)
  pendown()
  goto(75, j)

penup()
