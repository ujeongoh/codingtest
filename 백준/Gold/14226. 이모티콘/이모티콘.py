import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    S = int(input())
    methods = ['c', 'v', 'd']
    # method, emoticons, clipboard, count
    q = deque([[1, 0, 0]])
    visited = {}
    visited[(1, 0)] = 0
    answer = 0 

    while q:
        emoticons, clipboard, count = q.popleft()
        if emoticons == S:
            answer = count
            break
        for m in methods:
            if m == 'c':
                new_emoticons, new_clipboard = emoticons, emoticons
            elif m == 'v':
                new_emoticons, new_clipboard = emoticons + clipboard, clipboard
            else:
                new_emoticons, new_clipboard = emoticons - 1, clipboard

            if new_emoticons >= 1001 or new_emoticons < 0 or new_clipboard >= 1001 or new_clipboard < 0 or (new_emoticons, new_clipboard) in visited:
                continue
        
            visited[(new_emoticons, new_clipboard)] = count + 1
            q.append([new_emoticons, new_clipboard, count + 1])
    
    print(answer)