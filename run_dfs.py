from search_algorithms import dfs, graph, start, goal

for i in range(100000):
    dfs(graph, start, goal)

print("DFS profiling run completed.")
