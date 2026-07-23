stu_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(stu_graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in stu_graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(stu_graph, 'A')