import sys
from collections import Counter

input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())

    dna_list = [ input().strip() for _ in range(n) ]
    answer = []
    hd = 0

    for i, dna in enumerate(zip(*dna_list)):
        counts = Counter(list(dna))
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        max_key = sorted_counts[0][0]
        count = sum([cnt for key, cnt in sorted_counts[1:]])

        answer.append(max_key)
        hd += count

    print(''.join(answer))
    print(hd)
        