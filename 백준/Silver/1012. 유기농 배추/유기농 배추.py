import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    def bfs(a, b):
        q = [(a, b)]
        while q:
            x, y = q.pop()
            land[x][y] = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and ny >= 0 and nx < M and ny < N and land[nx][ny] == 1:
                    q.append([nx, ny])
                    land[nx][ny] = 0 

    for _ in range(T):
        M, N, K = map(int, input().split())
        land = [[0]*(N) for _ in range(M)]
        count = 0
        for _ in range(K):
            i, j = map(int, input().split())
            land[i][j] = 1

        for i in range(M):
            for j in range(N):
                if land[i][j] == 1:
                    bfs(i, j)
                    count += 1

        print(count)