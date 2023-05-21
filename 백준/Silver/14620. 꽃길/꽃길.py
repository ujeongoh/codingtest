import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    garden = [ list(map(int, input().split())) for _ in range(n) ]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    garden_dict = {}
    combi_list = []
    answer = float('inf')

    for i, row in enumerate(garden):
        for j, col in enumerate(garden):
            if not (i == 0 or i == n-1) and not (j == 0 or j == n-1):
                combi_list.append((i, j))
            garden_dict[(i, j)] = garden[i][j]

    combi = combinations(combi_list, 3)

    for c in combi:
        land = []
        overlapped = False
        cost = 0
        
        for coord in c:
            temp = [coord]
            for d in direction:
                if (coord[0]+d[0], coord[1]+d[1]) in land or coord in land:
                    overlapped = True
                    break
                temp.append((coord[0]+d[0], coord[1]+d[1]))
            if overlapped:
                break
            land += temp
        
        if overlapped:
            continue
        
        # land에 있는 좌표의 땅값 계산
        for l in land:
            cost += garden_dict[l]

        answer = min(answer, cost)

    print(answer)