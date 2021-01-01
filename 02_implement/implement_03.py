# Movement of Knights in Chess

input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1


moves = [(2, -1), (2, 1), (-2, -1), (-2, 1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0

for move in moves:
    next_column = column + move[1]
    next_row = row + move[0]

    if next_column >= 1 and next_column <= 8 and next_row >= 1 and next_row <= 8:

        result += 1

print(result)
