import sys

k, n = map(int, sys.stdin.readline().split())
lines = [int(input()) for _ in range(k)]

answer = 0
left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2    
    lan_cnt = 0
    for line in lines:
        lan_cnt += line // mid

    if lan_cnt >= n:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)