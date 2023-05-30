# -*- coding: utf-8 -*-
"""Generating 3x3 Magic Squares.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Zi7jwSX7hC-gwNq1lg7FTqfQt1iyyqf
"""

square = []


for i in range(3):
  square.append([])

for i in range(3):
  for j in range(3):
    square[i].append([])  



mid = 3//2 

k = 1
i = 0
j = mid
while True:
  if k == 10:
    break
  else:
    if i<0 and j==3:
      i = i+2
      j = j-1
      square[i][j].append(k)
      i = i-1
      j = j+1
  
    elif i<0:
      i = 2
      square[i][j].append(k)
      i = i-1
      j = j+1


    elif j>2:
      j = 0
      square[i][j].append(k)
      i = i-1
      j = j+1

    elif square[i][j] != []:
      i = i+2
      j = j-1
      square[i][j].append(k)
      i = i-1
      j = j+1

    else:
      square[i][j].append(k)
      i = i-1
      j = j+1

  k  = k+1

print("Magic Square 1:")
for i in square:
  for j in i:
    print(j[0], end=' ')
  print()

print()
print("Magic Square 2:")
square[0],square[2] = square[2],square[0]
for i in square:
  for j in i:
    print(j[0], end=' ')
  print()

print()
print("Magic Square 3:")
for j in range(3):
  square[j][0],square[j][2] = square[j][2], square[j][0]
for i in square:
  for j in i:
    print(j[0], end=' ')
  print()

print()
print("Magic Square 4:")
square[0],square[2] = square[2],square[0]
for i in square:
  for j in i:
    print(j[0], end=' ')
  print()