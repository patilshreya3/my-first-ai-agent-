from search_algorithms import bfs, graph, start, goal

for i in range(100000):
    bfs(graph, start, goal)

print("BFS profiling run completed.")
