from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([[0, 0, 1]])

    while q:
        x, y, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문한 위치를 0으로 변경하여 체크
                q.append([nx, ny, cnt + 1])

    return -1