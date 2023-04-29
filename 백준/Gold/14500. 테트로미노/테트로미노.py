n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

# 테트로미노 모양
tetrominoes = [
    [(0, 0), (0, 1), (1, 0), (1, 1)], # ㅡ
    [(0, 0), (0, 1), (0, 2), (0, 3)], # ㅣ
    [(0, 0), (1, 0), (2, 0), (3, 0)], # ㅁ
    [(0, 0), (1, 0), (1, 1), (2, 1)], # h
    [(1, 0), (0, 1), (1, 1), (2, 0)], # h 회전
    [(1, 0), (1, 1), (0, 1), (0, 2)], # ...
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], # L
    [(0, 1), (1, 1), (2, 0), (2, 1)], # ...
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1)] # ㅓ
]

def get_tetromino_sum(x, y, tetromino):
    # 테트로미노의 합을 계산하는 함수
    result = 0
    for dx, dy in tetromino:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            result += paper[nx][ny]
        else:
            return -1
    return result

answer = 0
for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            # 가능한 모든 테트로미노를 만들어 보면서 최대값을 찾음
            sum_value = get_tetromino_sum(i, j, tetromino)
            answer = max(answer, sum_value)

print(answer)
