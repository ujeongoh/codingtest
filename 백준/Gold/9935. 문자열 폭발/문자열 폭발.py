import sys
input = sys.stdin.readline


def solution():
    data = input().rstrip()
    boom = input().rstrip()
    stack = []
    

    for i in range(len(data)):
        stack.append(data[i])
        
        if stack and len(stack) >= len(boom) and ''.join(stack[-1*len(boom):]) == boom:
            for j in range(len(boom)):
                stack.pop()
    
    if stack:
        print(''.join(stack))
    else:
        print("FRULA")
        
    return
    
        
solution()