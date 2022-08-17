from collections import deque

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        current_node = queue.popleft()
        for adj_node in graph[current_node]:        # current_node와 연결되어 있는 node들을 확인
            if not visited[adj_node]:               # current_node와 연결되어 있는 node들 중 아직 방문하지 않은 노드들을 queue에 넣고 visited를 True로 바꿔주기
                queue.append(adj_node)
                visited[adj_node] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0       # 연결요소의 개수
for _ in range(m):
    inp_node1, inp_node2 = map(int, input().split())
    graph[inp_node1].append(inp_node2)
    graph[inp_node2].append(inp_node1)

for i in range(1, n+1):
    if visited[i] == False:         # i를 방문하지 않았을 때
        if not graph[i]:            # graph[i]값이 비어있을 때 (그냥 하나의 연결요소가 더 생기는 거임)
            count += 1
            visited[i] = True
        else:                       # 값이 있을 땐, bfs를 돌리고 연결요소의 개수를 하나 증가
            bfs(i)                  # bfs를 한 번 이라도 돌리고 난 후면
            count += 1              # 하나의 연결요소 찾은거라 +1

print(count)