# SLE-2: BFS vs DFS
# Problem: Find G starting from A

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

start = "A"
goal = "G"


# Breadth First Search
def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    nodes_expanded = 0

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbour in graph[current]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None, nodes_expanded


# Depth First Search
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        current = path[-1]

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                new_path = path + [neighbour]
                stack.append(new_path)

    return None, nodes_expanded


# Run BFS
bfs_path, bfs_nodes = bfs(graph, start, goal)

# Run DFS
dfs_path, dfs_nodes = dfs(graph, start, goal)


# Display results
print("===== BFS =====")
print("Path:", " -> ".join(bfs_path))
print("Nodes Expanded:", bfs_nodes)

print()

print("===== DFS =====")
print("Path:", " -> ".join(dfs_path))
print("Nodes Expanded:", dfs_nodes)
