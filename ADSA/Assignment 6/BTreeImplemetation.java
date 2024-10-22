import java.util.ArrayList;
import java.util.List;

// Class representing a node in the B-tree
class BTreeNode {
    int t; // Minimum degree
    List<Integer> keys; // List of keys
    List<BTreeNode> children; // List of children
    boolean leaf; // True if leaf node

    BTreeNode(int t, boolean leaf) {
        this.t = t;
        this.leaf = leaf;
        this.keys = new ArrayList<>();
        this.children = new ArrayList<>();
    }
}

// Class representing the B-tree itself
class BTree {
    private BTreeNode root; // Root node of the B-tree
    private int t; // Minimum degree

    public BTree(int t) {
        this.root = null;
        this.t = t;
    }

    // Insert a key into the B-tree
    public void insert(int key) {
        if (root == null) {
            root = new BTreeNode(t, true);
            root.keys.add(key);
        } else {
            if (root.keys.size() == 2 * t - 1) {
                BTreeNode newRoot = new BTreeNode(t, false);
                newRoot.children.add(root);
                splitChild(newRoot, 0);
                root = newRoot;
                insertNonFull(root, key);
            } else {
                insertNonFull(root, key);
            }
        }
    }

    // Insert a key into a non-full node
    private void insertNonFull(BTreeNode node, int key) {
        int i = node.keys.size() - 1;

        if (node.leaf) {
            node.keys.add(0); // Placeholder for new key
            while (i >= 0 && key < node.keys.get(i)) {
                node.keys.set(i + 1, node.keys.get(i));
                i--;
            }
            node.keys.set(i + 1, key);
        } else {
            while (i >= 0 && key < node.keys.get(i)) {
                i--;
            }
            i++;
            if (node.children.get(i).keys.size() == 2 * t - 1) {
                splitChild(node, i);
                if (key > node.keys.get(i)) {
                    i++;
                }
            }
            insertNonFull(node.children.get(i), key);
        }
    }

    // Split a child of a given parent node
    private void splitChild(BTreeNode parent, int index) {
        BTreeNode fullChild = parent.children.get(index);
        BTreeNode newChild = new BTreeNode(t, fullChild.leaf);

        for (int j = 0; j < t - 1; j++) {
            newChild.keys.add(fullChild.keys.remove(t)); // Move last t-1 keys to new child
        }

        if (!fullChild.leaf) {
            for (int j = 0; j < t; j++) {
                newChild.children.add(fullChild.children.remove(t)); // Move last t children to new child
            }
        }

        parent.children.add(index + 1, newChild); // Add new child to parent
        parent.keys.add(index, fullChild.keys.remove(t - 1)); // Move median key up to parent
    }

    // Perform post-order traversal of the tree
    public void postOrderTraversal(BTreeNode node) {
        if (node != null) {
            for (BTreeNode child : node.children) {
                postOrderTraversal(child);
            }
            System.out.print(node.keys + " ");
        }
    }

    // Check if all leaves are at the same depth
    public void checkLeafDepthConsistency(BTreeNode node, int depth, List<Integer> leafDepths) {
        if (node != null) {
            if (node.leaf) {
                leafDepths.add(depth);
            } else {
                for (BTreeNode child : node.children) {
                    checkLeafDepthConsistency(child, depth + 1, leafDepths);
                }
            }
        }
    }

    // Check that each non-leaf node has between t-1 and 2t-1 keys
    public List<List<Integer>> checkKeyCount(BTreeNode node) {
        List<List<Integer>> violations = new ArrayList<>();
        
        if (node != null) {
            if (node.keys.size() < t - 1 || node.keys.size() > 2 * t - 1) {
                violations.add(new ArrayList<>(node.keys));
            }
            
            for (BTreeNode child : node.children) {
                violations.addAll(checkKeyCount(child));
            }
        }
        
        return violations;
    }

    public BTreeNode getRoot() { return root; } // Get root of the tree
}

// Main class to test the B-tree implementation
public class BTreeImplemetation {

    public static void main(String[] args) {
        int[] keys = {10, 20, 5, 6}; // Replace with your pre-order keys
        
        // Initialize a B-tree with minimum degree t=2 
        BTree btree = new BTree(2);

        System.out.println("Inserting keys into the B-tree:");
        
        // Insert each key into the B-tree 
        for (int key : keys) {
            btree.insert(key);
            System.out.println("Inserted: " + key);
        }

        System.out.println("\nPost-order Traversal:");
        btree.postOrderTraversal(btree.getRoot());
        
        System.out.println("\n\nChecking Leaf Depth Consistency:");
        List<Integer> leafDepths = new ArrayList<>();
        btree.checkLeafDepthConsistency(btree.getRoot(), 0, leafDepths);
        
        System.out.println("Leaf depths: " + leafDepths);
        
        if (leafDepths.size() > 1) {
            System.out.println("Non-conforming nodes found at depths: " + leafDepths);
        } else {
            System.out.println("All leaves are at the same depth.");
        }

        System.out.println("\nChecking Key Count in Nodes:");
        List<List<Integer>> violatingNodes = btree.checkKeyCount(btree.getRoot());
        
        if (!violatingNodes.isEmpty()) {
            System.out.println("Nodes violating key count property: " + violatingNodes);
        } else {
            System.out.println("All nodes conform to the key count property.");
        }
    }
}