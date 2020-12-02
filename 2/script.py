#!/bin/python3
with open('input', 'r') as f:
  input = list(f)

valid = 0
for entry in input:
  parts = entry.split(' ')
  range = parts[0].split('-')
  first, second = int(range[0]) - 1, int(range[1]) - 1

  char = parts[1][0]
  password = parts[2][:-1]

  first = password[first] == char
  second = password[second] == char

  is_valid = (first and not second) or (second and not first)
  if is_valid:
    valid += 1

print(valid)
