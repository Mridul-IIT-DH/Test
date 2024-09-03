def read_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Read number of vertices and edges
    n, m = map(int, lines[0].strip().split())
    edges = []
    
    # Read edges
    for line in lines[1:]:
        if line.strip():  # Ignore blank lines
            u, v = map(int, line.strip().split())
            edges.append((u, v))
    
    return n, edges

def vertex_cover(graph, k):
    n, edges = graph
    if k < 0:
        return False, []

    if not edges:
        return True, []

    # Pick an arbitrary edge
    u, v = edges[0]

    # Create new edge lists for the two cases
    new_edges_with_u = [e for e in edges if u not in e]
    new_edges_with_v = [e for e in edges if v not in e]

    # Explore both possibilities
    cover_with_u = vertex_cover((n, new_edges_with_u), k - 1)
    if cover_with_u[0]:
        return True, [u] + cover_with_u[1]

    cover_with_v = vertex_cover((n, new_edges_with_v), k - 1)
    if cover_with_v[0]:
        return True, [v] + cover_with_v[1]

    # Explore the case where we include both u and v in the cover
    cover_with_both = vertex_cover((n, edges[1:]), k - 2)
    if cover_with_both[0]:
        return True, [u, v] + cover_with_both[1]

    return False, []

def main(file_path, k):
    graph = read_graph(file_path)
    result = vertex_cover(graph, k)

    if result[0]:
        print("Yes")
        print("Vertex Cover:", result[1])
    else:
        print("No")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python vertex_cover.py <graph_file> <parameter_k>")
        sys.exit(1)

    graph_file = sys.argv[1]
    k = int(sys.argv[2])
    main(graph_file, k)