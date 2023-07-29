import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for f in range(M)] for ff in range(N)]

movin = [[1,0], [0,1], [-1,0], [0,-1]]
q = deque()
q.append((0,0,0))
visited[0][0] = True
result = float('inf')

while q:
  x, y, d = q.popleft()

  if x == N-1 and y == M-1:
    result = min(result, d)
    break

  if d+1 > T:
    break

  for mov in movin:
    nx, ny = x+mov[0], y+mov[1]
    if (-1<nx<N and -1<ny<M) and not visited[nx][ny]:  # 경계점 아니고 미 방문시
      if not maps[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny, d+1))
      elif maps[nx][ny] == 1:  # 벽이면
        continue
      elif maps[nx][ny] == 2:  # 그람 찾음
        temp = d + 1  # 그람까지 온 거리
        temp += abs(N-1 -nx) + abs(M-1 - ny)
        visited[nx][ny] = True
        if temp <= T:
          result = temp

if result > T:
  print("Fail")
else:
  print(result)