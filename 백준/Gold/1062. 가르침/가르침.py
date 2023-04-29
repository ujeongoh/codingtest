import sys
import itertools

# 필수 글자를 제외한 알파벳과 필수 알파벳을 저장한 변수
candidiate = "bdefghjklmopqrsuvwxyz"
need = "actin"

# 각 알파벳의 비트마스킹 값을 미리 계산해 저장한 변수
bit_values = {}
for c in candidiate + need:
    bit_values[c] = 1 << (ord(c) - ord("a"))

n, m = map(int, sys.stdin.readline().split())

# words : 각 단어의 비트마스킹한 정수를 저장한 리스트
words = []
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    # word 변수에 각 문자의 비트마스킹 값을 누적
    word = 0
    for x in temp:
        word |= bit_values[x]
    words.append(word)

# 만일 m이 5미만이면 필수 글자를 다 배울 수 없기 때문에 한 단어도 읽지 못한다
if m < 5:
    print(0)
else:
    ans = 0
    for i in itertools.combinations(candidiate, m - 5):
        each = 0
        res = 0
        # 각 조합에 대한 비트마스킹
        for j in need:
            each |= bit_values[j]
        for j in i:
            each |= bit_values[j]

        # 단어와 각 조합의 비교
        for j in words:
            if each & j == j:
                res += 1

        # 최대값 갱신
        ans = max(ans, res)
    print(ans)
