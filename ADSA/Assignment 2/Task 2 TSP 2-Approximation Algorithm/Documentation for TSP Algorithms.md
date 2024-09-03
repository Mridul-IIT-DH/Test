# Documentation for Vertex Cover and TSP Algorithms

## Task 2: Traveling Salesman Problem (TSP) 2-Approximation Algorithm

### Full Code for Task 2

```python
import heapq
from collections import defaultdict

def read_tsp_input(file_path):
    """
    Reads the input for the TSP algorithm from a specified file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        list: A list of dictionaries, each containing a graph and the number of vertices.
    """
    graphs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph_data = []

        for line in lines:
            line = line.strip()
            if line:
                graph_data.append(line)
            elif graph_data:
                # Process a complete graph
                graph, n = process_graph_data(graph_data)
                graphs.append({'graph': graph, 'n': n})
                graph_data = []

    return graphs

def process_graph_data(graph_data):
    """
    Processes graph data from a list of lines.

    Args:
        graph_data (list): A list of lines representing the graph data.

    Returns:
        dict: A dictionary containing the edges of the graph with weights.
        int: The number of vertices in the graph.
    """
    graph = {'edges': []}
    n, m = map(int, graph_data[0].split())

    for line in graph_data[1:]:
        parts = list(map(int, line.split()))
        if len(parts) == 3:
            u, v, weight = parts
            graph['edges'].append((u, v, weight))
        else:
            print(f"Warning: Skipping line with incorrect format: {line}")

    return graph, n

def prim_mst(graph, n):
    """
    Constructs the Minimum Spanning Tree (MST) using Prim's algorithm.

    Args:
        graph (dict): A dictionary containing the edges of the graph with weights.
        n (int): The number of vertices in the graph.

    Returns:
        list: A list of edges in the MST.
    """
    # Create an adjacency list from the edge list
    adj = [[] for _ in range(n)]
    for u, v, weight in graph['edges']:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    # Prim's algorithm initialization
    start_vertex = 0  # Start from vertex 0
    mst_edges = []
    visited = [False] * n
    edges = [(weight, start_vertex, to) for to, weight in adj[start_vertex]]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if not visited[to]:
            visited[to] = True
            mst_edges.append((frm, to, weight))
            for to_next, weight in adj[to]:
                if not visited[to_next]:
                    heapq.heappush(edges, (weight, to, to_next))

    return mst_edges

def preorder_traversal(mst_edges, start_vertex):
    """
    Performs a preorder traversal of the MST to create a tour.

    Args:
        mst_edges (list): A list of edges in the MST.
        start_vertex (int): The starting vertex for the traversal.

    Returns:
        list: A list representing the tour.
    """
    # Create an adjacency list for the MST
    mst_adj = defaultdict(list)
    for u, v, _ in mst_edges:
        mst_adj[u].append(v)
        mst_adj[v].append(u)

    # Perform DFS to get the preorder traversal
    tour = []
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        tour.append(vertex)
        for neighbor in mst_adj[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_vertex)
    return tour

def tsp_2_approximation(graph, n):
    """
    Implements the 2-approximation algorithm for TSP.

    Args:
        graph (dict): A dictionary containing the edges of the graph with weights.
        n (int): The number of vertices in the graph.

    Returns:
        list: A list representing the tour.
    """
    # Step 1: Construct the Minimum Spanning Tree (MST)
    mst_edges = prim_mst(graph, n)

    # Step 2: Perform a preorder traversal of the MST to create a tour
    start_vertex = 0  # Start from vertex 0
    tour = preorder_traversal(mst_edges, start_vertex)

    return tour

# Define the file path
file_path = r"C:\Users\mridu\Downloads\Monu\IIT's lab work\Test\ASDA\Assignment 2\task2-input.txt"

# Read the graphs from the input file
graphs = read_tsp_input(file_path)

# Calculate and print the TSP tour for each graph
for graph_data in graphs:
    graph = graph_data['graph']
    n = graph_data['n']
    tsp_tour = tsp_2_approximation(graph, n)
    print("TSP Tour:", tsp_tour)
```

### Explanation of Task 2 Code

1. **`read_tsp_input(file_path)`**:
   - **Purpose**: Reads the input file and constructs a list of graphs.
   - **Process**: It reads lines from the file, accumulating lines until an empty line is found, indicating the end of a graph's data. It then calls `process_graph_data` to create a graph dictionary.

   ```python
   graphs = []
   ```

2. **`process_graph_data(graph_data)`**:
   - **Purpose**: Converts a list of lines representing graph edges into a dictionary format.
   - **Process**: It extracts the number of vertices `n` and edges `m` from the first line. It then iterates through the remaining lines, parsing each line to extract the vertices `u`, `v`, and weight `weight`. The edge `(u, v)` with weight `weight` is added to the `edges` list of the graph dictionary.

   ```python
   n, m = map(int, graph_data[0].split())
   ```

3. **`prim_mst(graph, n)`**:
   - **Purpose**: Constructs the Minimum Spanning Tree (MST) using Prim's algorithm.
   - **Process**: It creates an adjacency list from the edge list in the input graph dictionary. It then initializes Prim's algorithm starting from vertex 0. The algorithm repeatedly selects the edge with the minimum weight from the available edges and adds it to the MST.

   ```python
   adj = [[] for _ in range(n)]
   ```

4. **`preorder_traversal(mst_edges, start_vertex)`**:
   - **Purpose**: Performs a preorder traversal of the MST to create a tour.
   - **Process**: It creates an adjacency list `mst_adj` from the `mst_edges` list. It then performs a depth-first search (DFS) starting from the `start_vertex`, adding each visited vertex to the `tour` list in preorder.

   ```python
   mst_adj = defaultdict(list)
   ```

5. **`tsp_2_approximation(graph, n)`**:
   - **Purpose**: Implements the 2-approximation algorithm for TSP.
   - **Process**: It first calls the `prim_mst` function to construct the MST from the input graph. It then calls the `preorder_traversal` function, starting from vertex 0, to create the tour based on the MST.

   ```python
   mst_edges = prim_mst(graph, n)
   ```

6. **Main Execution Block**:
   - **Purpose**: Reads graphs from the specified input file and computes the TSP tour for each graph.
   - **Process**: Calls the `read_tsp_input` function and iterates through the returned graphs, printing the calculated TSP tour for each.

   ```python
   graphs = read_tsp_input(file_path)
   ```

### Example Input for Task 2

Assuming the input file `task2-input.txt` contains:

```
5 10
0 1 1
0 2 2
0 3 2
0 4 2
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 2
```

### Dry Run for Task 2

1. **Input File Read**: The first line is read, indicating there are 5 vertices and 10 edges.
   - Vertices: `5`
   - Edges: `10`

2. **Processing Edges**: The subsequent lines are processed to form the graph:
   - Edges: `[(0, 1, 1), (0, 2, 2), (0, 3, 2), (0, 4, 2), (1, 2, 1), (1, 3, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 4, 2)]`

3. **Constructing MST**:
   - Starting from vertex `0`, the algorithm selects edges based on minimum weights.
   - The MST edges selected might look like: `[(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 4, 2)]`.

4. **Preorder Traversal**:
   - Starting from vertex `0`, the DFS visits vertices in the order: `0 -> 1 -> 2 -> 3 -> 4`.
   - The resulting tour is: `[0, 1, 2, 3, 4]`.

5. **Final Output**:
   - The output will display the tour for the TSP, which approximates a valid route through the vertices based on the MST.