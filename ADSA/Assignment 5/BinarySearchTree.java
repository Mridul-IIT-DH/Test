class Node {
  int data;
  Node left, right;

  public Node(int item) {
    data = item;
    left = right = null;
  }
}

public class BinarySearchTree {
  Node root;

  // Insert operation
  public void insert(int key) {
    root = insertRec(root, key);
  }

  private Node insertRec(Node root, int key) {
    if (root == null) {
      root = new Node(key);
      return root;
    }
    if (key < root.data) {
      root.left = insertRec(root.left, key);
    } else if (key > root.data) {
      root.right = insertRec(root.right, key);
    }
    return root;
  }

  // Pre-order traversal
  public void preorderTraversal(Node node) {
    if (node != null) {
      System.out.print(node.data + " ");
      preorderTraversal(node.left);
      preorderTraversal(node.right);
    }
  }

  // Flip operation
  public void flip(Node node) {
    if (node == null)
      return;

    // Swap left and right children
    Node temp = node.left;
    node.left = node.right;
    node.right = temp;

    flip(node.left);
    flip(node.right);
  }

  // Fill operation that creates a new tree from the keys
  public void fillFlippedBST(BinarySearchTree flippedBst, int[] keys) {
    for (int key : keys) {
      flippedBst.insert(key); // Insert into the flipped tree
    }
  }

  // Create a new flipped BST with the given keys
  public BinarySearchTree createFlippedBST(int[] keys) {
    BinarySearchTree flippedBst = new BinarySearchTree();
    for (int key : keys) {
      flippedBst.insert(key);
    }
    flippedBst.flip(flippedBst.root); // Flip it after inserting
    return flippedBst;
  }

  public static void main(String[] args) {
    BinarySearchTree bst = new BinarySearchTree();

    // Check if keys are provided as command-line arguments
    if (args.length == 0) {
      System.out.println("Please provide distinct keys as command-line arguments.");
      return;
    }

    // Step 1: Build BST from given keys
    int[] keys = new int[args.length];
    for (int i = 0; i < args.length; i++) {
      try {
        keys[i] = Integer.parseInt(args[i]);
        bst.insert(keys[i]);
      } catch (NumberFormatException e) {
        System.out.println("Invalid input: " + args[i] + " is not an integer.");
        return;
      }
    }

    // Step 2: Pre-order Traversal of the original BST
    System.out.println("Pre-order Traversal of BST:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    // Step 3: Flip the BST
    bst.flip(bst.root);

    // Step 4: Create a new flipped BST and fill it with the same keys
    BinarySearchTree flippedBst = bst.createFlippedBST(keys);

    // Display the pre-order traversal of the flipped BST
    System.out.println("Pre-order Traversal after filling flipped BST:");
    flippedBst.preorderTraversal(flippedBst.root);
    System.out.println();
  }
}
