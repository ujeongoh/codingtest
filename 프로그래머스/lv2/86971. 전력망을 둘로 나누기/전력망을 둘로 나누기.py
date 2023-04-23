from collections import defaultdict, deque

wire_dict = defaultdict(set)

def get_node_cnt_by_bfs(n:int, wire:list) -> int :
    """
    Parameters :
    1.n : 노드 수
    2.wire : 노드를 연결하는 간선의 양 끝에 있는 노드 두개의 리스트

    Return : 
    wire를 자른다고 가정했을 때 wire의 첫번째 노드쪽에 딸려있는 노드 갯수를 반환한다.
    """
    node_cnt = 1
    v1, v2 = wire[0], wire[1] 
    closed = [False] * (n + 1)
    closed[v1] = True
    q = deque([v1])
    
    while q:
        curr = q.popleft()
        for w in wire_dict[curr]:
            if closed[w] or w == v2: # 방문했거나 자른 간선의 반대쪽 노드일 경우 pass
                continue
            closed[w] = True
            node_cnt += 1
            q.append(w)
            
    return node_cnt

def solution(n, wires):
    answer = float("inf")   
    
    for v1, v2 in wires:
        wire_dict[v1].add(v2)
        wire_dict[v2].add(v1)
        
    for wire in wires:
        node_cnt = get_node_cnt_by_bfs(n, wire)
        answer = min(answer, abs(node_cnt - (n - node_cnt))) # 구한 한쪽의 노드 수와 반대쪽 노드 수(n - 구한 한쪽 노드 수)의 차이
    
    return answer