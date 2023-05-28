import math

def shuffle_cards(card, range_val, cnt):
    newCard = [0] * len(card)
    idx = 0
    for i in range(range_val - cnt, range_val):
        newCard[idx] = card[i]
        card[i] = 0
        idx += 1
    for i in range(len(card)):
        if card[i] != 0:
            newCard[idx] = card[i]
            idx += 1
    card[:] = newCard

def solve(card, k):
    range_val = n
    for i in range(1, k + 2):
        cnt = int(math.pow(2, k - i + 1))
        shuffle_cards(card, range_val, cnt)
        range_val = cnt

n = int(input())
result = list(map(int, input().split())) #최종 결과값

for k1 in range(1, n + 1):
    if math.pow(2, k1) > n:
        break
    for k2 in range(1, n + 1):
        if math.pow(2, k2) > n:
            break
        card = list(range(1, n + 1))
        solve(card, k1)
        solve(card, k2)
        if result == card:
            print(k1, k2)
            exit()

print(-1, -1)