#!/bin/python3

with open('input', 'r') as file:
  input = [line.strip() for line in file]

count = 0
group = []
new = True
for line in input:
  if len(line) > 0:
    group.append(set(line))
  else:
    # Finished group
    result = None
    for p in group:
      if result is None:
        result = p
      else:
        result = result.intersection(p)
    count += len(result)
    group = []

print(count)
