import heapq
import sys

# print("input== readline")
input = sys.stdin.readline
INF = int(1e9)

# print("input== map")
n, m = map(int, input().split())
start = int(input)

graph = [[] for _ in range(n+1)]


distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split)
    graph[a].append((b, c))


def dijkstra(start):
    # q 라는 배열을 먼저 선언을 한다음에
    q = []

    # heapq.heappush(q 배열, )
    heapq.heappush(q, (0, start))
    distance(start) = 0

    # 배열 q 이기 때문에 일단 항상 참이라고 생각하고, 진행되다가
    while q:
        # heappop 으로 q의 배열을 계속 지우면서 q가 없어지는데, 다 없어질때 까지 진행되는 것이라고 볼 수 있다.
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# Note for dijkstra algo
# dijkstra algo -> 그래프에서 여러개의 노드가 있을때,
# 특정한 노드에서 출발, 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
# dijkstra algo 는 '음의 간선' 이 없을때 정상적으로 동작한다.
# [음의 간선이란 0보다 작은 값을 가지는 간선을 의미 한다.]
# 기본적으로 그리디 알고리즘으로 분류됨. 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복하기 때문이다.
# ===============================
#  1. 출발 노드를 설정
#  2. 최단 거리 테이블을 초기화 한다.
#  3. 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택한다.
#  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
#  5. 3번과 4번을 반복한다.
# ===============================
#
# 각 노드에 대한 현재까지의 최단 거리 정보를 항상 [1 차원 리스트] 에 저장하며 리스트를 계속 갱신 한다는 특징이 있다.
