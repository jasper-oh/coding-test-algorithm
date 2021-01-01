n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            x_p = x + dx[i]
            y_p = y + dy[i]

    if x_p < 1 or y_p < 1 or x_p > n or y_p > n:

        continue
    x = x_p
    y = y_p
print(x_p, y_p)
