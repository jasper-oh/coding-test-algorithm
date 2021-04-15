n, m = map(int, input().split())

count_field = [[0 for col in range(n)]for row in range(m)]
x_pos, y_pos, direction = list(map(int, input().split()))
count_field[x_pos][y_pos] = 1


field = []
for i in range(n):
    field.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_count = 0
while True:
    turn_left()
    new_x_pos = x_pos + dx[direction]
    new_y_pos = y_pos + dy[direction]

    if count_field[new_x_pos][new_y_pos] == 0 and field[new_x_pos][new_y_pos] == 0:
        count_field[new_x_pos][new_y_pos] = 1
        x_pos = new_x_pos
        y_pos = new_y_pos

        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        new_x_pos = x_pos - dx[direction]
        new_y_pos = y_pos - dy[direction]

        if field[new_x_pos][new_y_pos] == 0:
            x_pos = new_x_pos
            y_pos = new_y_pos
        else:
            break
        turn_count = 0
print(count)
