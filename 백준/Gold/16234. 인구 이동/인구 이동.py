import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(coord):
        adj = []
        sum = 0
        q = deque([coord])
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            adj.append((x, y))
            sum += countries[x][y]
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(countries[x][y] - countries[nx][ny]) <= R and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    
        if len(adj) > 1:    
            avg = int(sum / len(adj))        
            for a in adj:
                countries[a[0]][a[1]] = avg
            return 1
        else:
            return 0 

    while True:
        visited = [[0] * N for _ in range(N)]
        move_count = 0
        for i in range(N):
            for j in range(N): 
                if not visited[i][j]:
                    move_count += bfs((i, j))
        if move_count == 0:
            break
        else:
            answer += 1

    print(answer)
                
                
            


