# Vertex Cover Evaluation - Detailed Breakdown

### Imports

```java
import java.io.*;
import java.util.*;
```

- **Purpose**: These imports provide the necessary classes for file input/output and the manipulation of data structures.
- **Why**:
  - `java.io.*`: For reading the graph input from a file using classes like `BufferedReader` and `FileReader`.
  - `java.util.*`: For handling data structures such as `List`, `ArrayList`, `Set`, and `HashSet`.

### Code snippet
```java

import java.io.*;
import java.util.*;

public class VertexCoverEvaluation {

public static void main(String[] args) {
    if (args.length != 2) {
       System.out.println("Usage: java VertexCover <graph_file> <parameter_k>");
        System.exit(1);
    }

    String graphFile = args[0];
    int k = Integer.parseInt(args[1]);
    Graph graph = readGraph(graphFile);
    Set<List<Integer>> allCovers = new HashSet<>();
    findAllVertexCovers(graph, k, new ArrayList<>(), allCovers);

    if (allCovers.isEmpty()) {
        System.out.println("No vertex cover found of size at most " + k);
    } else {
        System.out.println("All possible vertex covers of size at most " + k + ":");
        for (List<Integer> cover : allCovers) {
            System.out.println(cover);
        }
    }
}

    private static Graph readGraph(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            br.readLine().trim().split(" ");
            List<int[]> edges = new ArrayList<>();

            String line;
            while ((line = br.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    String[] parts = line.trim().split(" ");
                    edges.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
                }
            }
            return new Graph(edges);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
//Mridul Chandrawanshi
//CS24MT002

    private static void findAllVertexCovers(Graph graph, int k, List<Integer> currentCover, Set<List<Integer>> allCovers) {
        List<int[]> edges = graph.edges;

        if (edges.isEmpty()) {
            List<Integer> coverCopy = new ArrayList<>(currentCover);
            Collections.sort(coverCopy);
            allCovers.add(coverCopy);
            return;
        }

        if (k <= 0) {
            return;
        }

        int[] edge = edges.get(0);
        int u = edge[0];
        int v = edge[1];

        List<int[]> newEdgesU = new ArrayList<>();
        for (int[] e : edges) {
            if (e[0] != u && e[1] != u) {
                newEdgesU.add(e);
            }
        }
        currentCover.add(u);
        findAllVertexCovers(new Graph(newEdgesU), k - 1, currentCover, allCovers);
        currentCover.remove(currentCover.size() - 1);

        List<int[]> newEdgesV = new ArrayList<>();
        for (int[] e : edges) {
            if (e[0] != v && e[1] != v) {
                newEdgesV.add(e);
            }
        }
        currentCover.add(v);
        findAllVertexCovers(new Graph(newEdgesV), k - 1, currentCover, allCovers);
        currentCover.remove(currentCover.size() - 1);
    }

    static class Graph {
        List<int[]> edges;

        Graph(List<int[]> edges) {
            this.edges = edges;
        }
    }
}
```
  
#### How to run the code?

Go to the folder containing the code, and compile it form the terminal `javac VertexCover.java` and then run it using `java VertexCover <graph_file> <parameter_k>`.

### Main Class Declaration

```java
public class VertexCover {
```

- **Purpose**: This class encapsulates all the logic required to solve the vertex cover problem.
- **Why**: In Java, the main logic must reside in a class. This `VertexCover` class contains methods to read the graph, find all possible vertex covers, and print the results.

### Main Method

```java
public static void main(String[] args) {
```

- **Purpose**: This is the entry point for the program where the execution begins.
- **Why**: In Java, every application requires a `main` method as the entry point for execution.
- **How**: It reads command-line arguments, handles input, and initiates the vertex cover finding algorithm.

#### Argument Check

```java
if (args.length != 2) {
    System.out.println("Usage: java VertexCover <graph_file> <parameter_k>");
    System.exit(1);
}
```

- **Purpose**: Ensures that the user provides exactly two arguments: the graph file and the parameter `k`.
- **Why**: The program cannot proceed without these required inputs.
- **How**: 
  - The length of `args` is checked to confirm that two arguments have been provided.
  - If the number of arguments is incorrect, a usage message is printed, and the program exits using `System.exit(1)`.

#### Reading Input Arguments

```java
String graphFile = args[0];
int k = Integer.parseInt(args[1]);
```

- **Purpose**: Extracts the file path for the graph and the integer `k` from the command-line arguments.
- **Why**: The file contains the graph data, and `k` is the maximum size of the vertex cover to be found.
- **How**:
  - `graphFile = args[0]`: Assigns the graph file path to the variable `graphFile`.
  - `k = Integer.parseInt(args[1])`: Converts the string argument `k` to an integer.

### Reading the Graph File

```java
Graph graph = readGraph(graphFile);
```

- **Purpose**: Calls the `readGraph` method to read the graph from the specified file and store it in a `Graph` object.
- **Why**: The graph must be parsed from the file into a usable format (the `Graph` object) for processing.
  
### Finding All Vertex Covers

```java
Set<List<Integer>> allCovers = new HashSet<>();
findAllVertexCovers(graph, k, new ArrayList<>(), allCovers);
```

- **Purpose**: Initializes an empty `HashSet` to store all unique vertex covers and calls `findAllVertexCovers` to compute all possible vertex covers of size at most `k`.
- **Why**: The algorithm recursively explores all possible sets of vertices that could form a vertex cover of size at most `k`.
- **How**:
  - `allCovers`: A `HashSet` is used to store all unique vertex covers. The `Set` ensures that duplicate covers are not stored.
  - `findAllVertexCovers`: Recursively computes vertex covers by trying different combinations of vertices.
  
### Output Results

```java
if (allCovers.isEmpty()) {
    System.out.println("No vertex cover found of size at most " + k);
} else {
    System.out.println("All possible vertex covers of size at most " + k + ":");
    for (List<Integer> cover : allCovers) {
        System.out.println(cover);
    }
}
```

- **Purpose**: Prints the results of the vertex cover search.
- **Why**: The user needs to know whether a vertex cover of size `k` or smaller was found, and what those vertex covers are.
- **How**:
  - If `allCovers` is empty, it means no valid cover of size at most `k` was found, and a message is printed accordingly.
  - If vertex covers were found, the program prints all possible vertex covers stored in `allCovers`.

**Example**:
If no cover is found for `k = 3`, the output will be:
```
No vertex cover found of size at most 3
```
If multiple covers are found, the output might look like:
```
All possible vertex covers of size at most 3:
[0, 1]
[1, 2]
```

---

### `readGraph` Method

```java
private static Graph readGraph(String filePath) {
```

- **Purpose**: Reads the graph data from the specified file and constructs a `Graph` object.
- **Why**: The graph needs to be parsed from its textual representation into a structured object that can be processed by the program.
  
#### File Reading

```java
try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
    String[] firstLine = br.readLine().trim().split(" ");
    int n = Integer.parseInt(firstLine[0]);
    int m = Integer.parseInt(firstLine[1]);
    List<int[]> edges = new ArrayList<>();
```

- **Purpose**: Opens the file and reads the first line to determine the number of vertices `n` and edges `m`. The edges are then stored in a list.
- **Why**: The graph is typically represented in the file by the number of vertices and edges, followed by each edge listed as a pair of vertices.
- **How**: 
  - `BufferedReader br = new BufferedReader(new FileReader(filePath))`: Opens the file and creates a `BufferedReader` for reading it.
  - `firstLine`: Reads the first line, which contains the number of vertices `n` and the number of edges `m`.
  - `edges`: A list to store the edges of the graph, each edge represented as an array of two integers.

#### Edge Parsing

```java
String line;
while ((line = br.readLine()) != null) {
    if (!line.trim().isEmpty()) {
        String[] parts = line.trim().split(" ");
        edges.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
    }
}
return new Graph(edges);
```

- **Purpose**: Reads each line of the file after the first, parses the vertices of each edge, and adds them to the list of edges.
- **Why**: Each line after the first represents an edge in the graph, and the program needs to store these edges for processing.
- **How**:
  - The `while` loop reads each line, checks if it's not empty, splits it into two parts (the two vertices of the edge), and adds the edge to the `edges` list.
  
**Example**:
For a file with content:
```
4 5
0 1
0 2
1 2
1 3
2 3
```
The edges stored will be: `[[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]`.

---

### `findAllVertexCovers` Method

```java
private static void findAllVertexCovers(Graph graph, int k, List<Integer> currentCover, Set<List<Integer>> allCovers) {
```

- **Purpose**: Recursively finds all possible vertex covers of size at most `k` for the given graph.
- **Why**: The vertex cover problem is solved by exploring different combinations of vertices that could cover all edges, and this method finds all such valid combinations.
- **How**: 
  - The method recursively explores the options of including vertices from each edge and tries to reduce the problem size by removing the edges covered by those vertices.

#### Base Case: No More Edges

```java
if (graph.edges.isEmpty()) {
    List<Integer> coverCopy = new ArrayList<>(currentCover);
    Collections.sort(coverCopy);
    allCovers.add(coverCopy);
    return;
}
```

- **Purpose**: If there are no edges left in the graph, the current set of vertices forms a valid vertex cover.
- **Why**: If no edges are left to cover, the current set of vertices is a valid solution, so it is added to the set of covers.
- **How**:
  - The `currentCover` is copied and sorted before being added to `allCovers` to avoid modifying the list during recursion and ensure uniqueness.

#### Base Case: Exceeding the Size Limit

```java
if (k <= 0) {
    return;
}
```

- **Purpose**: Stops the recursion if `k` becomes less than or equal to 0, as it's impossible to find a vertex cover within the size limit.
- **Why**: Once `k` is exhausted, further recursion is pointless because the remaining vertices would exceed the allowed size.
- **How**: If `k <= 0`, the method returns without adding any new covers.

#### Recursive

 Case: Choosing a Vertex

```java
int[] edge = graph.edges.get(0);
int u = edge[0];
int v = edge[1];
```

- **Purpose**: Selects the first edge from the list of edges and its two endpoints, `u` and `v`.
- **Why**: The method will attempt to include either `u` or `v` in the vertex cover, reducing the problem size by removing the edges connected to that vertex.

#### Recursion for Vertex `u`

```java
List<int[]> newEdgesU = new ArrayList<>();
for (int[] e : graph.edges) {
    if (e[0] != u && e[1] != u) {
        newEdgesU.add(e);
    }
}
currentCover.add(u);
findAllVertexCovers(new Graph(newEdgesU), k - 1, currentCover, allCovers);
currentCover.remove(currentCover.size() - 1);
```

- **Purpose**: Recursively attempts to find a vertex cover by including vertex `u` in the current cover and removing all edges incident to `u`.
- **Why**: Including vertex `u` removes all edges connected to it, simplifying the problem for the next recursion step.
- **How**:
  - The method creates a new list of edges (`newEdgesU`) by excluding all edges connected to `u`.
  - Then, `u` is added to the current cover, and the method recursively calls itself with the reduced graph and `k - 1`.

#### Recursion for Vertex `v`

```java
List<int[]> newEdgesV = new ArrayList<>();
for (int[] e : graph.edges) {
    if (e[0] != v && e[1] != v) {
        newEdgesV.add(e);
    }
}
currentCover.add(v);
findAllVertexCovers(new Graph(newEdgesV), k - 1, currentCover, allCovers);
currentCover.remove(currentCover.size() - 1);
```

- **Purpose**: Similar to the `u` case, this code handles the scenario where vertex `v` is added to the cover, and all edges connected to `v` are removed.
- **Why**: This explores the alternate solution of including `v` instead of `u`, ensuring that all possible covers are considered.
- **How**:
  - The method creates a new list of edges (`newEdgesV`) by excluding all edges connected to `v`.
  - Then, `v` is added to the current cover, and the method recursively calls itself with the reduced graph and `k - 1`.

---

### Graph Class

```java
static class Graph {
    List<int[]> edges;

    Graph(List<int[]> edges) {
        this.edges = edges;
    }
}
```

- **Purpose**: Represents the graph as a list of edges, where each edge is an array of two integers (the vertices connected by that edge).
- **Why**: The graph must be represented in a structured way to allow for manipulation and recursive processing in the vertex cover algorithm.
- **How**:
  - The `Graph` class encapsulates the edges of the graph, providing a convenient way to store and manipulate the graph throughout the program.