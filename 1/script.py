#!/usr/bin/python3
with open('input', 'r') as f:
  input = [int(x) for x in f]

for x in input:
  for y in input:
    for z in input:
      if x + y + z == 2020:
        print(x, y, z)
        print(x * y * z)
