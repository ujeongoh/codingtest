s = int(input())
cnt = 0
n = 1

while True:
    cnt += n
    if cnt > s:
        break
    n += 1
        
print(n - 1)