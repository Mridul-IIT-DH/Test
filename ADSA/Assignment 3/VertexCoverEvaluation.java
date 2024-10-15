
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
