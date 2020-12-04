with open('input', 'r') as f:
    map = [list(line.strip()) for line in f]

angles = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]
results = []
product = 1
for dx, dy in angles:
    x, y = 0, 0
    trees = 0
    while y < len(map):
        cell = map[y][x % len(map[y])]
        if cell == '#':
            trees += 1
        x += dx
        y += dy
    print(dx, dy, trees)
    product *= trees
    results.append(trees)
print(product)
