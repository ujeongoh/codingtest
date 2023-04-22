import sys

n, m = map(int, sys.stdin.readline().split())  # 건물 n, 도로 m
INF = float('inf')

# 2차원 배열 만들기 - 인덱스 0을 버리는 형태로 만든다
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 거리 입력 - 모두 1로 동일하다고 문제에 나와있음
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신은 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 모든 정점에서 모든 정점으로 가는 최소 거리 구하기 (플로이드 워셜 알고리즘 점화식 사용)
for k in range(1, n + 1):
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 2개의 건물을 선택하여(예상 치킨집) 모든 집을 방문해서 걸리는 거리를 측정
min_sum = INF
result = []

# 건물 2개를 뽑는다.
for i in range(1, n):  
    for j in range(2, n + 1):
        sum = 0
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum += min(graph[k][i], graph[k][j]) * 2  # k -> i, k -> j 중 짧은 거리 더하기
        if sum < min_sum:
            min_sum = sum
            result = [i, j, sum]

print(*result)