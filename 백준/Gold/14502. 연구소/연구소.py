from itertools import combinations
from collections import deque

n, m = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(n)] #연구소의 배열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lab, walls):
    #조합에서 나온 좌표에 벽을 먼저 세워 줌
    for x, y in walls:
        lab[x][y] = 1

    q = deque() #바이러스가 있는 위치를 큐에 추가 (바이러스들의 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i, j))

    #BFS를 수행
    while q:
        x, y = q.popleft()
        for i in range(4): #네 구역을 돌면서
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:  #상하좌우의 칸이 0일 때 바이러스가 확산됨. 대신 이동한 위치가 범위에서 벗어나서는 안 됨.
                lab[nx][ny] = 2
                q.append((nx, ny))
    safe_cnt = sum(lab[i].count(0) for i in range(n))
    return safe_cnt



result = 0
#0에 벽을 놓을 수 있기 때문에 임의의 세 개의 0의 좌표를 combinations를 통해 구한다.
#그리고 이 구한 조합을 for문을 통해서 bfs 구문에 보내며 안전 지대가 최대인 값을 찾는다.
for walls in combinations([(i, j) for i in range(n) for j in range(m) if labs[i][j] == 0], 3):
    safe_cnt = bfs([row[:] for row in labs], walls)
    result = max(result, safe_cnt)

print(result)