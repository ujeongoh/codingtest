import sys
from itertools import combinations
input = sys.stdin.readline
    
if __name__ == "__main__":  
    n = int(input())
    board = [ list(input().strip()) for _ in range(n) ]
    answer = 0
    
    def is_adjacent(a, b):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            if (a[0] + d[0], a[1] + d[1]) == b:
                return True
        else:
            return False

    combi_list = list(filter(lambda e: is_adjacent(e[0], e[1]), combinations([ (i, j) for i in range(len(board)) for j in range(len(board[i]))], 2)))
    
    for combi in combi_list:
        count = 1
        ai, aj, bi, bj = combi[0][0], combi[0][1], combi[1][0], combi[1][1]        
        board[ai][aj], board[bi][bj] = board[bi][bj], board[ai][aj]

        # 연속된 문자 카운트
        # 가로 + 세로
        rows = board + list(map(list, zip(*board)))
        cur = rows[0][0]
        for row in rows:
            sub_count = 0
            for j, char in enumerate(row):
                if j == 0:
                    cur = char
                if char == cur:
                    sub_count += 1
                else:
                    sub_count = 1
                    cur = char
                count = max(count, sub_count)
        
        board[bi][bj], board[ai][aj] = board[ai][aj], board[bi][bj]
        answer = max(answer, count)

    print(answer)