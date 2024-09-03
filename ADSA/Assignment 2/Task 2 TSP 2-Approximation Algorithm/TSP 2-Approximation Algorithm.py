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