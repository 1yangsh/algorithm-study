from collections import deque
graph = [
    [],
    [2, 3, 8], ## 1번 노드와 연결된 노드
    [1, 7],   ## 2번 노드와 연결된 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현
visited = [False] * 9

# BFS
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)