from turtle import *

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
