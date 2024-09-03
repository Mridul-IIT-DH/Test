# Documentation for Vertex Cover

## Task 1: Vertex Cover 2-Approximation Algorithm

### Full Code for Task 1

```python
def read_vertex_cover_input(file_path):
    """
    Reads the input for the Vertex Cover algorithm from a specified file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        list: A list of dictionaries, each containing a graph.
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
                graph = process_graph_data(graph_data)
                graphs.append(graph)
                graph_data = []

    return graphs

def process_graph_data(graph_data):
    """
    Processes graph data from a list of lines.

    Args:
        graph_data (list): A list of lines representing the graph data.

    Returns:
        dict: A dictionary containing the edges of the graph.
    """
    graph = {'edges': []}

    for line in graph_data:
        u, v = map(int, line.split())
        graph['edges'].append((u, v))

    return graph

def vertex_cover_2_approximation(graph):
    """
    Implements the 2-approximation algorithm for Vertex Cover.

    Args:
        graph (dict): A dictionary containing the edges of the graph.

    Returns:
        set: A set of vertices representing the vertex cover.
    """
    cover = set()
    edges = set(graph['edges'])

    while edges:
        u, v = edges.pop()
        cover.add(u)
        cover.add(v)
        edges = {edge for edge in edges if u not in edge and v not in edge}

    return cover

# Define the file path
file_path = r"C:\Users\mridu\Downloads\Monu\IIT's lab work\Test\ASDA\Assignment 2\task1-input.txt"

# Read the graphs from the input file
graphs = read_vertex_cover_input(file_path)

# Calculate and print the vertex cover for each graph
for graph in graphs:
    vertex_cover = vertex_cover_2_approximation(graph)
    print("Vertex Cover:", vertex_cover)
```

### Explanation of Task 1 Code

1. **`read_vertex_cover_input(file_path)`**:
   - **Purpose**: Reads the input file and constructs a list of graphs.
   - **Process**: It reads lines from the file, accumulating lines until an empty line is found, indicating the end of a graph's data. It then calls `process_graph_data` to create a graph dictionary.
   
   ```python
   graphs = []
   ```

2. **`process_graph_data(graph_data)`**:
   - **Purpose**: Converts a list of lines representing graph edges into a dictionary format.
   - **Process**: It extracts vertex pairs from each line and appends them to the `edges` list in the graph dictionary.

   ```python
   for line in graph_data:
       u, v = map(int, line.split())
       graph['edges'].append((u, v))
   ```

3. **`vertex_cover_2_approximation(graph)`**:
   - **Purpose**: Implements the 2-approximation algorithm for finding a vertex cover.
   - **Process**: It iteratively selects edges, adds their vertices to the cover, and removes all edges incident to those vertices until all edges are covered.

   ```python
   while edges:
       u, v = edges.pop()
       cover.add(u)
       cover.add(v)
       edges = {edge for edge in edges if u not in edge and v not in edge}
   ```

4. **Main Execution Block**:
   - **Purpose**: Reads graphs from the specified input file and computes the vertex cover for each graph.
   - **Process**: Calls the `read_vertex_cover_input` function and iterates through the returned graphs, printing the calculated vertex cover for each.

   ```python
   graphs = read_vertex_cover_input(file_path)
   for graph in graphs:
       vertex_cover = vertex_cover_2_approximation(graph)
       print("Vertex Cover:", vertex_cover)
   ```

### Example Input for Task 1

Assuming the input file `task1-input.txt` contains:

```
0 1
0 2
1 2
1 3
2 3

0 4
4 5
4 6
5 6
```

### Dry Run for Task 1

1. **Input File Read**: The first graph is read until an empty line is encountered.
   - Graph 1 edges: `[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]`
   
2. **Processing Graph**: The edges are processed and stored in a dictionary.
   - Resulting graph: `{'edges': [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]}`

3. **Vertex Cover Calculation**:
   - Starting with edges: `[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]`
   - Select edge `(0, 1)`, add vertices `0` and `1` to cover.
   - Remove edges incident to `0` and `1`: Remaining edges: `[(1, 2), (1, 3), (2, 3)]`
   - Select edge `(1, 2)`, add vertices `1` and `2` to cover.
   - Remaining edges are covered, final cover: `{0, 1, 2}`