graph = {0: [1, 2],
         1: [0, 3, 4],
         2: [0],
         3: [1],
         4: [2, 3]}


def bfs(graph, start, visited=[], queue=[]):
    visited.append(start)
    queue.append(start)

    while queue:
        x = queue.pop(0)

        for neighbor in graph[x]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


print(bfs(graph, 0))
