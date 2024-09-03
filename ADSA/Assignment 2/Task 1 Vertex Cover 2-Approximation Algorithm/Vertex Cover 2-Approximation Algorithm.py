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