# from collections import deque

# n, m = map(int, input().split())

# graph = []

# for col in range(n):
#     graph.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     # 이 while문은 어떤 조건을 가지고 있는것일까? 실험해보기
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]

#             if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
#                 continue
#             if graph[new_x][new_y] == 0:
#                 continue
#             if graph[new_x][new_y] == 1:
#                 graph[new_x][new_y] = graph[x][y] + 1
#                 queue.append((new_x, new_y))
#     return graph[n-1][m-1]


# print(bfs(0, 0))
a = [1, 2, 3]
for i in range(len(a)):
    a.pop()

print(a)
