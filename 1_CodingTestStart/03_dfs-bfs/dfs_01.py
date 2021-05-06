# 실전 문제 3
#  n, m 크기의 얼음 틀 구멍이 있는 곳 0, 칸막이 1 -> Input
#  만들어지는 얼음의 수

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
