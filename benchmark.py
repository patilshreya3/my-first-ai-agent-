import timeit
from search_algorithms import bfs, dfs, graph, start, goal


def measure(function):
    times = timeit.repeat(
        lambda: function(graph, start, goal),
        repeat=3,
        number=10000
    )

    average = sum(times) / len(times)

    return times, average


bfs_times, bfs_average = measure(bfs)
dfs_times, dfs_average = measure(dfs)


print("===== BFS Timing =====")
print("Run times:", bfs_times)
print("Average:", bfs_average, "seconds")
print()

print("===== DFS Timing =====")
print("Run times:", dfs_times)
print("Average:", dfs_average, "seconds")
