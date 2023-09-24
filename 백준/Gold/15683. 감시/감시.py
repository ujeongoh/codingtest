import sys
import copy

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    office = []
    cctv_list = []
    for i in range(N):
        row = list(map(int, input().split()))
        office.append(row)
        for j, num in enumerate(row):
            if 1 <= num <= 5:
                cctv_list.append([num, i, j])
    modes = {
        1: [[0], [1], [2], [3]],
        2: [[0, 2], [1, 3]],
        3: [[0, 1], [1, 2], [2, 3], [0, 3]],
        4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        5: [[0, 1, 2, 3]],
    }
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    min_value = N * M
    
    def fill(map, d_list, x, y):
        for d in d_list:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    break
                if map[nx][ny] == 6:
                    break
                elif map[nx][ny] == 0:
                    map[nx][ny] = 7
                                    
    def dfs(depth, graph):
        global min_value
        
        if depth == len(cctv_list):
            space_count = 0
            for i in range(N):
                space_count += graph[i].count(0)
            min_value = min(min_value, space_count)
            return
        
        temp_graph = copy.deepcopy(graph)
        num, x, y = cctv_list[depth]
        for mode in modes[num]:
            fill(temp_graph, mode, x, y)
            dfs(depth + 1, temp_graph)
            temp_graph = copy.deepcopy(graph)
        
    dfs(0, office)
    print(min_value)
