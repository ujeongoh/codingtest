import sys

input = sys.stdin.readline

_dict = dict()

cnt = 0

while True:
    s = input().rstrip()
    if not s:
        break
    _dict[s] = _dict.get(s,0) +1
    cnt+=1

for k,v in sorted(_dict.items()):
    ratio = round(v/cnt*100,4)
    print('%s %.4f' % (k,ratio))