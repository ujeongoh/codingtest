import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    max = 100001
    visited = [0] * max

    def bfs():
        q = deque([n]) # 출발
        while q:
            loc = q.popleft()
            if loc == k:
                print(visited[k])
                break
            for i in (loc - 1, loc + 1, loc * 2):
                if 0 <= i < max and not visited[i]:
                    visited[i] = visited[loc] + 1
                    q.append(i)
        return
    if n == k:
        print(0)
    else:
        bfs()