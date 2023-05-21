import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    numsets = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))
    
    for _ in range(n):
        answer, s, b = input().split()
        
        index = 0
        while index < len(numsets):
            numset = numsets[index]
            s_cnt, b_cnt = 0, 0
            for i in range(len(answer)):
                if answer[i] in numset:
                    if answer[i] == numset[i]:
                        s_cnt += 1
                    else:
                        b_cnt += 1

            if int(s) != s_cnt or int(b) != b_cnt:
                numsets.remove(numset)
            else:
                index += 1
            
    print(len(numsets))