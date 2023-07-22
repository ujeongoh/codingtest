def solution(n):
    triangle = [ [0] * i for i in range(1, n + 1) ]
    num = 1
    x, y = -1, 0
    
    for i in range(n):
        for _ in range(i, n):
            # down
            if i % 3 == 0:
                x += 1
            # right
            elif i % 3 == 1:
                y += 1
            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1

    return sum(triangle, [])