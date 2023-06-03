import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(coord):
        q = deque([coord])
        while q:
            c = q.popleft()
            land[c[0]][c[1]] = 0
            for x, y in D:
                dx, dy = c[0]+x, c[1]+y
                if dx >= 0 and dy >= 0 and dx < M and dy < N and land[dx][dy] == 1:
                    q.append([dx, dy])
                    land[dx][dy] = 0 

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
                    bfs([i, j])
                    count += 1

        print(count)