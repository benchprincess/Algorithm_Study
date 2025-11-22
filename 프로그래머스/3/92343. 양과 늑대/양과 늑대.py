def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
    
    answer = 0
    
    def dfs(sheep, wolf, current, next_nodes):
        nonlocal answer
        
        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1
            
        if wolf >= sheep:
            return
        
        answer = max(answer, sheep)
        
        new_next = next_nodes.copy()
        if current in new_next:
            new_next.remove(current)
        new_next.extend(graph[current])
        
        for nxt in new_next:
            dfs(sheep, wolf, nxt, new_next)
            
    dfs(0,0,0,[0])
    return answer
    
    
    return answer