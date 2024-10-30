import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

class NodeOfBTree {
    List<Integer> keys;
    List<NodeOfBTree> child;
    boolean Leaf;

    NodeOfBTree(boolean Leaf) {
        this.Leaf = Leaf;
        this.keys = new ArrayList<>();
        this.child = new ArrayList<>();
    }
}

public class BTreeImplementation {
    static int currentIndex = 0;
    static final int MIN_DEGREE = 2; // Minimum degree

    public static void main(String[] args) {
        // Directly defining the preorder traversal in the code
        List<Integer> preorderKeys = List.of(10, 20, 1, 2, 3, 4, 11, 12, 21, 22);

        currentIndex = 0;
        NodeOfBTree rootNode = createBTree(preorderKeys, Integer.MIN_VALUE, Integer.MAX_VALUE, true);

        if (rootNode == null) {
            System.out.println("Violation occurred during constructing the tree.");
            return;
        }

        System.out.println("Post-order traversal:");
        printPostOrder(rootNode);
        System.out.println();

        // Collect leaves and their depths
        List<LeafDepth> leafDepths = new ArrayList<>();
        recordLeafDepths(rootNode, 0, leafDepths);

        // Identify unique depths
        Set<Integer> uniqueDepths = new HashSet<>();
        for (LeafDepth leaf : leafDepths) {
            uniqueDepths.add(leaf.depth);
        }

        // Check if all leaves are at the same depth
        if (uniqueDepths.size() == 1) {
            System.out.println("All leaf nodes are at the same depth.");
        } else {
            System.out.println("Leaf are at different depths.");
            System.out.println("Leaf and their depths:");
            for (LeafDepth leaf : leafDepths) {
                System.out.print("Leaf node at depth " + leaf.depth + ": ");
                for (int i = 0; i < leaf.node.keys.size(); i++) {
                    System.out.print(leaf.node.keys.get(i));
                    if (i != leaf.node.keys.size() - 1) System.out.print(" ");
                }
                System.out.println(",");
            }
        }

        // Check for nodes with invalid number of keys
        List<NodeOfBTree> invalidNodes = new ArrayList<>();
        boolean hasKeyViolation = false;
        validateNodeKeys(rootNode, rootNode, hasKeyViolation, invalidNodes);

        if (hasKeyViolation) {
            System.out.println("Some nodes have invalid number of keys.");
            System.out.println("Nodes violating key constraints:");
            for (NodeOfBTree node : invalidNodes) {
                System.out.print("Node: ");
                for (int i = 0; i < node.keys.size(); i++) {
                    System.out.print(node.keys.get(i));
                    if (i != node.keys.size() - 1) System.out.print(" ");
                }
                System.out.println(",");
            }
        } else {
            System.out.println("All nodes have valid number of keys.");
        }
    }

    static NodeOfBTree createBTree(List<Integer> preorderKeys, int minKey, int maxKey, boolean isRoot) {
        if (currentIndex >= preorderKeys.size()) return null;

        NodeOfBTree newNode = new NodeOfBTree(true);

        // Add keys to the node
        while (currentIndex < preorderKeys.size() && newNode.keys.size() < 2 * MIN_DEGREE - 1) {
            int key = preorderKeys.get(currentIndex);

            // If the key is out of the current node's key range, break
            if (key < minKey || key > maxKey) {
                break;
            }

            // Add key to the node
            newNode.keys.add(key);
            currentIndex++;

            // If the next key is less than the current key, it indicates the start of child nodes
            if (currentIndex < preorderKeys.size() && preorderKeys.get(currentIndex) < newNode.keys.get(newNode.keys.size() - 1)) {
                break;
            }
        }

        // Decide whether to create child nodes
        if (newNode.keys.size() >= MIN_DEGREE - 1 && currentIndex < preorderKeys.size() && preorderKeys.get(currentIndex) < newNode.keys.get(newNode.keys.size() - 1)) {
            newNode.Leaf = false;
            int numberOfChildren = newNode.keys.size() + 1;

            // Build child nodes
            for (int i = 0; i < numberOfChildren; ++i) {
                int childMaxKey = (i < newNode.keys.size()) ? newNode.keys.get(i) : maxKey;
                NodeOfBTree childNode = createBTree(preorderKeys, minKey, childMaxKey, false);
                newNode.child.add(childNode);
                minKey = childMaxKey;

                // If child is null, it means there was a violation in child construction
                if (childNode == null) {
                    System.out.println("Violation occurred during tree construction.");
                    return null;
                }
            }

            // Check if the number of non-null child is correct
            int actualChildrenCount = 0;
            for (NodeOfBTree child : newNode.child) {
                if (child != null) actualChildrenCount++;
            }
            if (actualChildrenCount < numberOfChildren) {
                System.out.print("Node with keys ");
                for (int k : newNode.keys) {
                    System.out.print(k + " ");
                }
                System.out.println("has fewer child than expected.");
                return null;
            }
        }

        // Check for underflow in non-root nodes
        if (!isRoot && newNode.keys.size() < MIN_DEGREE - 1) {
            System.out.println("Node underflow");
            return null;
        }

        return newNode;
    }

    static void printPostOrder(NodeOfBTree node) {
        if (node == null) return;

        // Traverse all child first
        for (NodeOfBTree child : node.child) {
            printPostOrder(child);
        }

        // Then print all the keys of the node together
        System.out.print(" ");
        for (int i = 0; i < node.keys.size(); i++) {
            System.out.print(node.keys.get(i));
            if (i != node.keys.size() - 1) {
                System.out.print(" ");
            }
        }
        System.out.print(", ");
    }

    static void recordLeafDepths(NodeOfBTree node, int depth, List<LeafDepth> leafDepths) {
        if (node == null) return;
        if (node.Leaf) {
            leafDepths.add(new LeafDepth(node, depth));
        }
        for (NodeOfBTree child : node.child) {
            recordLeafDepths(child, depth + 1, leafDepths);
        }
    }

    static void validateNodeKeys(NodeOfBTree node, NodeOfBTree root, boolean hasKeyViolation, List<NodeOfBTree> invalidNodes) {
        if (node == null) return;
        int numberOfKeys = node.keys.size();
        if ((node != root && (numberOfKeys < MIN_DEGREE - 1 || numberOfKeys > 2 * MIN_DEGREE - 1)) || (node == root && numberOfKeys > 2 * MIN_DEGREE - 1)) {
            hasKeyViolation = true;
            invalidNodes.add(node);
        }
        for (NodeOfBTree child : node.child) {
            validateNodeKeys(child, root, hasKeyViolation, invalidNodes);
        }
    }

    // Helper class to hold node and depth pairs
    static class LeafDepth {
        NodeOfBTree node;
        int depth;

        LeafDepth(NodeOfBTree node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}
