from turtle import *

speed(10000)
for i in range(-75, 75, 75):
  penup()
  setposition(i, 75)
  pendown()
  goto(i, -75)

for i in range(-50, 50, 50):
  penup()
  setposition(-100, i)
  pendown()
  goto(100, i)

penup()
