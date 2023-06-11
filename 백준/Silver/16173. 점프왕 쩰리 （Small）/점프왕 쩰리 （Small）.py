import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    game_map = [ list(map(int, input().split())) for _ in range(N) ]

    def bfs(x, y):
        rval = "Hing"
        q = deque([(x, y)])
        while q:
            f = q.popleft()
            i, j = f[0], f[1]
            if i >= N or j >= N:
                break
            visited[i][j] = True
            num = game_map[i][j]
            if num == -1:
                return "HaruHaru"
            if i + num < N and not visited[i+num][j]:
                q.append((i + num, j))
            if j + num < N and not visited[i][j+num]:
                q.append((i, j + num))
        return rval 
    
    print(bfs(0, 0))


