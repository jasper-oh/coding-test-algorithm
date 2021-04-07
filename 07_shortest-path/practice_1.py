import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수, 간선의 갯수를 입력 받기 n = 노드의 갯수 / m = 간선의 갯수
n, m = map(int, input().split())

# 시작노드를 입력 받기
start = int(input())

# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for _ in range(n+1)]

# 방문한적 있는지 체크하는 목적의 리스트를 만들기
visited = [[False]*(n+1)]

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선정보를 입력 받기
for _ in range(m):
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 것을 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(n-1):
        now = get_smallest_node()
        visited(now) = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
