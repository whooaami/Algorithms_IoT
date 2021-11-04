graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = []
queue = []


def bfs(graph: dict, node):
    visited.append(node)
    queue.append(node)

    while queue:
        element = queue.pop(0)
        print(element, end=" ")

        for neighbor in graph[element]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


if __name__ == '__main__':
    bfs(graph, 'A')
