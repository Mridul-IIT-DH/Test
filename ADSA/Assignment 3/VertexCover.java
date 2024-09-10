import java.io.*;
import java.util.*;

public class VertexCover {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java VertexCover <graph_file> <parameter_k>");
            System.exit(1);
        }

        String graphFile = args[0];
        int k = Integer.parseInt(args[1]);
        Graph graph = readGraph(graphFile);
        Result result = vertexCover(graph, k);

        if (result.isCoverFound) {
            System.out.println("Yes");
            System.out.println("Vertex Cover: " + result.cover);
        } else {
            System.out.println("No");
        }
    }

    private static Graph readGraph(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String[] firstLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(firstLine[0]);
            int m = Integer.parseInt(firstLine[1]);
            List<int[]> edges = new ArrayList<>();

            String line;
            while ((line = br.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    String[] parts = line.trim().split(" ");
                    edges.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
                }
            }
            return new Graph( edges);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static Result vertexCover(Graph graph, int k) {
        List<int[]> edges = graph.edges;

        if (k < 0) {
            return new Result(false, new ArrayList<>());
        }

        if (edges.isEmpty()) {
            return new Result(true, new ArrayList<>());
        }

        int[] edge = edges.get(0);
        int u = edge[0];
        int v = edge[1];

        for (int vertex : new int[]{u, v}) {
            List<int[]> newEdges = new ArrayList<>();
            for (int[] e : edges) {
                if (e[0] != vertex && e[1] != vertex) {
                    newEdges.add(e);
                }
            }
            Result result = vertexCover(new Graph(newEdges), k - 1);
            if (result.isCoverFound) {
                result.cover.add(0, vertex);
                return result;
            }
        }

        return new Result(false, new ArrayList<>());
    }

    static class Graph {
        List<int[]> edges;

        Graph(List<int[]> edges) {
            this.edges = edges;
        }
    }

    static class Result {
        boolean isCoverFound;
        List<Integer> cover;

        Result(boolean isCoverFound, List<Integer> cover) {
            this.isCoverFound = isCoverFound;
            this.cover = cover;
        }
    }
}
