from collections import deque

def bfs_count(start_node):
    c = 0
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for adj_node in graph[current_node]:        # current_node와 연결되어 있는 node들을 확인
            if not visited[adj_node]:               # current_node와 연결되어 있는 node들 중 아직 방문하지 않은 노드들을 queue에 넣고 visited를 True로 바꿔주기
                queue.append(adj_node)
                visited[adj_node] = True
                c += 1                              # start_node부터 bfs로 탐색할 수 있는 노드들의 개수를 세주기
    return c

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    inp_node1, inp_node2 = map(int, input().split())
    graph[inp_node1].append(inp_node2)
    graph[inp_node2].append(inp_node1)

print(bfs_count(1))                                 # 시작은 1번 노드부터