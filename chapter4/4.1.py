from collections import deque

# dfs

def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
            
    return False


# bfs

def bfs(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for val in graph[node]:
            if val not in visited:
                if val == end:
                    return True
                else:
                    queue.append(val)
        visited.add(node)
    return False