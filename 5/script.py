def calc(size, chars):
    start = 1
    end = size
    for c in chars:
        low = c == 'F' or c == 'L'
        diff = end - start + 1
        if low:
            end = end - (diff / 2)
        else:
            start = start + (diff / 2)
    assert start == end
    return int(start - 1)


seats = [[' ' for i in range(8)] for i in range(128)]
seat_list = [' ' for i in range(1024)]
id_max = 0
with open('input', 'r') as file:
    for line in file:
        row = calc(128, line[:7])
        column = calc(8, line[7:10])
        id = row * 8 + column
        if id > id_max:
            id_max = id
        seats[row][column] = 'X'
        seat_list[id] = 'X'

print(id_max)


print('')
for id, seat in enumerate(seat_list):
    if seat_list[id + 1] == ' ':
        print(id + 1)

# for row in range(128):
#     print(f'{row} ', sep='')
#     for column in range(8):
#         print(seats[row][column], sep='')
#     print('')

