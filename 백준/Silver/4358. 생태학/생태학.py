import sys
from collections import defaultdict
input = sys.stdin.readline

trees = defaultdict(int) # 기본 값이 0인 딕셔너리
tree_num = 0 # 나무의 총 개수

while True:
    tree = input().rstrip()
    if tree == '':
        break

    tree_num += 1
    trees[tree] += 1

trees_list = sorted(trees.keys())

for tree in trees_list:
    print('%s %.4f' %(tree, (trees[tree]/tree_num)*100))