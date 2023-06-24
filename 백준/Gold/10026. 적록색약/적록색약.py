import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    image = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    area = 0
    rg_area = 0
    
    def bfs(coord, color, is_rg):
        q = deque([coord])
        
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if is_rg and image[nx][ny] == 'G':
                        image[nx][ny] = 'R'
                    if not visited[nx][ny] and image[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        
    for i in range(N):
        for j in range(N): 
            if not visited[i][j]:
                bfs((i, j), image[i][j], False)
                area += 1
                
    visited = [[False] * N for _ in range(N)]            
    for i in range(N):
        for j in range(N): 
            if not visited[i][j]:
                if image[i][j] == 'G':
                    image[i][j] = 'R'
                bfs((i, j), image[i][j], True)
                rg_area += 1

    print(area, rg_area)
                
                
            


