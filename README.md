# my-first-ai-agent-

This is my first chatbot.हो 👍 Nano उघडलेला आहे.

आता **README च्या सगळ्या जुन्या मजकुराला खालील मजकुराने replace कर**:

````markdown
# my-first-ai-agent-

This is my first chatbot.

## SLE-2: BFS vs DFS

For SLE-2, I used a small graph search problem to compare Breadth First Search (BFS) and Depth First Search (DFS).

### Graph

```text
             A
            / \
           B   C
          / \   \
         D   E   F
              \
               G
````

Start node: A
Goal node: G

### Results

| Algorithm | Nodes Expanded |     Average Time |
| --------- | -------------: | ---------------: |
| BFS       |              7 | 0.022056 seconds |
| DFS       |              5 | 0.022370 seconds |

The average time was calculated using three timing runs with Python `timeit`.

I also used `py-spy` to create profiling files:

* `results/bfs-profile.svg`
* `results/dfs-profile.svg`

The results are measurements from this small graph and are used for comparison in the SLE-2 report.
