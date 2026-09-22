छान 👍 आता `SLE-2-REPORT.md` editor मध्ये open आहे.

आता **हा पूर्ण content copy करून त्या file मध्ये paste कर**:

````markdown
# SLE-2 Report: BFS vs DFS Performance Comparison

## 1. Introduction

For SLE-2, a small graph search problem was used to compare two search algorithms: Breadth First Search (BFS) and Depth First Search (DFS).

The same graph, start node, and goal node were used for both algorithms. Their performance was compared using actual execution-time measurements and the number of nodes expanded.

## 2. Problem Description

The graph used for the experiment was:

```text
             A
            / \
           B   C
          / \   \
         D   E   F
              \
               G
````

* Start node: A
* Goal node: G

Both BFS and DFS found the path:

**A → B → E → G**

## 3. Algorithms Used

### Breadth First Search (BFS)

BFS searches nodes level by level using a queue. It was used to search the graph from A until the goal G was found.

### Depth First Search (DFS)

DFS explores deeper nodes before backtracking, using a stack. It was also used to search from A until G was found.

## 4. Experimental Method

Python's `timeit` module was used to measure execution time.

Each algorithm was executed 10,000 times in each timing run, and 3 timing runs were performed. The average of the three runs was used as the reported timing result.

The number of nodes expanded by each algorithm was also counted.

`py-spy` was additionally used to generate profiling files for both algorithms:

* `results/bfs-profile.svg`
* `results/dfs-profile.svg`

## 5. Results

| Algorithm | Nodes Expanded | Average Time for 10,000 Runs |
| --------- | -------------: | ---------------------------: |
| BFS       |              7 |             0.022056 seconds |
| DFS       |              5 |             0.022370 seconds |

### Individual Timing Runs

**BFS**

* Run 1: 0.023052 seconds
* Run 2: 0.021552 seconds
* Run 3: 0.021565 seconds
* Average: 0.022056 seconds

**DFS**

* Run 1: 0.023828 seconds
* Run 2: 0.022378 seconds
* Run 3: 0.020904 seconds
* Average: 0.022370 seconds

## 6. Discussion

In this particular graph, BFS expanded 7 nodes, while DFS expanded 5 nodes. Both algorithms successfully found the same path: A → B → E → G.

The measured average execution times were very close. BFS had an average time of 0.022056 seconds, while DFS had an average time of 0.022370 seconds for 10,000 runs.

The results show that fewer expanded nodes did not directly correspond to a lower measured execution time in this small experiment. Since the graph is very small, the timing difference is also very small.

Therefore, these results are measurements for this specific graph and should not be treated as a general conclusion about which algorithm is always faster.

## 7. Conclusion

This experiment demonstrated how BFS and DFS can be compared using actual performance measurements.

For this experiment, BFS expanded 7 nodes and DFS expanded 5 nodes. The average measured times for 10,000 runs were 0.022056 seconds for BFS and 0.022370 seconds for DFS.

The experiment helped demonstrate the importance of measuring algorithm performance using actual data.

## 8. AI Contribution

ChatGPT was used as a learning and development assistant to understand BFS and DFS, prepare the benchmark code, understand node counting, and learn how to use `py-spy` for profiling.

The student ran the programs, checked the outputs, collected the measurements, and used the actual results in this report.

```


```

