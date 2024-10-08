import java.util.*;

class Node {
  int val;
  Node left, right;

  public Node(int key) {
    val = key;
    left = right = null;
  }
}

class BinarySearchTree {
  Node root;

  // Insert a key into the tree
  public void insert(int key) {
    if (root == null) {
      root = new Node(key);
    } else {
      insertRec(root, key);
    }
  }

  private void insertRec(Node currentNode, int key) {
    if (key < currentNode.val) {
      if (currentNode.left == null) {
        currentNode.left = new Node(key);
      } else {
        insertRec(currentNode.left, key);
      }
    } else if (key > currentNode.val) {
      if (currentNode.right == null) {
        currentNode.right = new Node(key);
      } else {
        insertRec(currentNode.right, key);
      }
    }
  }

  // Pre-order Traversal (Root, Left, Right)
  public void preorderTraversal(Node node) {
    if (node != null) {
      System.out.print(node.val + " ");
      preorderTraversal(node.left);
      preorderTraversal(node.right);
    }
  }

  // Flip the tree (swap left and right children for each node)
  public void flip(Node node) {
    if (node != null) {
      Node temp = node.left;
      node.left = node.right;
      node.right = temp;
      flip(node.left);
      flip(node.right);
    }
  }

  // Fill the flipped tree with sorted keys in in-order manner
  public void fillInOrder(Node node, List<Integer> keys) {
    if (node == null) {
      return;
    }
    fillInOrder(node.left, keys); // Traverse the left subtree
    node.val = keys.remove(0); // Replace the current node's value with the next sorted key
    fillInOrder(node.right, keys); // Traverse the right subtree
  }

  // Helper function to fill the tree after flipping
  public void fill(List<Integer> keys) {
    Collections.sort(keys); // Sort the keys before filling in in-order traversal
    fillInOrder(root, keys);
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // 1. Take input from the user
    System.out.print("Enter the keys (separated by space): ");
    String userInput = scanner.nextLine();

    // 2. Split the input string by spaces and convert it to a list of integers
    String[] inputKeys = userInput.split(" ");
    List<Integer> keys = new ArrayList<>();
    for (String key : inputKeys) {
      keys.add(Integer.parseInt(key));
    }

    // 3. Create a Binary Search Tree and insert the keys
    BinarySearchTree bst = new BinarySearchTree();
    for (int key : keys) {
      bst.insert(key);
    }

    // 4. Print pre-order traversal before flipping
    System.out.println("Pre-order traversal before flipping:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    // 5. Flip the BST
    bst.flip(bst.root);

    // 6. Print pre-order traversal after flipping
    System.out.println("Pre-order traversal after flipping:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    // 7. Fill the flipped tree with the original keys in sorted order (in-order
    // filling)
    bst.fill(keys);

    // 8. Print pre-order traversal after filling the flipped tree
    System.out.println("Pre-order traversal after filling the flipped BST with sorted keys:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    scanner.close();
  }
}