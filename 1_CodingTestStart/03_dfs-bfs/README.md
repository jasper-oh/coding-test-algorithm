### 인접리스트 방식 예제

### 먼저 리스트를 이해하자

#### Row -> 3개인 2차원 인접 리스트 표현

```python
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

# [[(1,7),(2,5)],[(0,7)],[(0,5)]]
```

#### DFS 예제

> 방문처리의 예시

```python

    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited)


    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현 ( 1차원 리스트 )
    visited = [False] * 9

    dfs(graph, 1, visited)

    # 1 2 7 6 8 3 4 5

```

#### BFS 예제

> 방문처리의 예시

```python

    from collections import deque

    def bfs(graph,start,visited):
        queue = deque([start])

        visited[start] = True

        while queue:

            v = queue.popleft()
            print(v, end=' ')

            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False] * 9

    bfs(graph, 1, visited)

#  1 2 4 8 7 4 5 6
```
