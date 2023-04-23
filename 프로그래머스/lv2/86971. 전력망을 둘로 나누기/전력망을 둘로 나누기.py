from collections import defaultdict, deque


def get_node_count(del_line, n, wire_dict): 
    count = 1 
    visited = [False] * (n + 1) 
    visited[del_line[0]] = True  
    queue = deque([del_line[0]])

    while queue: 
        curr = queue.popleft()
        for i in wire_dict[curr]: 
            if visited[i] or i == del_line[1]:  
                continue
            count += 1
            queue.append(i)
            visited[i] = True
    return count


def solution(n, wires):
    answer = float("inf")
    data = defaultdict(set)  
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)

    for w in wires:
        node_count = get_node_count(w, n, data)
        answer = min(answer, abs(node_count - (n - node_count)))
    return answer