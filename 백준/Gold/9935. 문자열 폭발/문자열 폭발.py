s = list(input())
boom_s = list(input())
stack = []

for c in s:
    stack.append(c)
    if stack[len(stack)-len(boom_s):len(stack)] == boom_s:
        for _ in range(len(boom_s)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")