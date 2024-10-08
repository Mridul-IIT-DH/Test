# Binary Search Tree (BST) Implementation in Java

This report provides a comprehensive explanation of the Java implementation of a Binary Search Tree (BST), including its key operations such as insertion, pre-order traversal, flipping the tree, and filling a flipped BST.

## Overview

A Binary Search Tree (BST) is a data structure that maintains sorted order of its elements. Each node in the BST contains a key greater than all the keys in its left subtree and less than all the keys in its right subtree.

### Code Snippet

```java
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
        if (node == null) return;

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
```

### Explanation of the Code

#### 1. Node Class

```java
class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}
```

- **Purpose**: Represents a single node in the binary search tree.
- **Attributes**:
  - `data`: Holds the value of the node.
  - `left`: Reference to the left child node.
  - `right`: Reference to the right child node.
- **Constructor**: Initializes the node with a given integer value and sets both children to `null`.

#### 2. BinarySearchTree Class

```java
public class BinarySearchTree {
    Node root;
```

- **Purpose**: Contains the main structure and operations of the binary search tree.
- **Attribute**:
  - `root`: The root node of the BST.

#### 3. Insert Operation

```java
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
```

- **insert(int key)**: Public method to insert a key into the BST.
- **insertRec(Node root, int key)**: Private recursive method to insert a key:
  - If the current `root` is `null`, a new node is created and returned.
  - If the key is less than the `root`'s data, it inserts the key in the left subtree.
  - If the key is greater, it inserts it in the right subtree.
  
**Example**: If we insert the keys `10`, `5`, `15`, the structure becomes:

```
    10
   /  \
  5   15
```

#### 4. Pre-order Traversal

```java
public void preorderTraversal(Node node) {
    if (node != null) {
        System.out.print(node.data + " ");
        preorderTraversal(node.left);
        preorderTraversal(node.right);
    }
}
```

- **Purpose**: Performs a pre-order traversal of the BST (Node -> Left -> Right).
- **Example Output**: For the tree shown above, pre-order traversal would output `10 5 15`.

#### 5. Flip Operation

```java
public void flip(Node node) {
    if (node == null) return;

    // Swap left and right children
    Node temp = node.left;
    node.left = node.right;
    node.right = temp;

    flip(node.left);
    flip(node.right);
}
```

- **Purpose**: Flips the BST such that all left children become right children and vice versa.
- **Example**: For a tree:
```
    10
   /  \
  5   15
```
After flipping, it becomes:
```
    10
   /  \
  15   5
```

#### 6. Fill Operation for Flipped BST

```java
public void fillFlippedBST(BinarySearchTree flippedBst, int[] keys) {
    for (int key : keys) {
        flippedBst.insert(key); // Insert into the flipped tree
    }
}
```

- **Purpose**: Populates the provided `flippedBst` with keys from the given array.
  
**Example Usage**: This method can be called after creating a new `BinarySearchTree` object to fill it with values.

#### 7. Create a Flipped BST

```java
public BinarySearchTree createFlippedBST(int[] keys) {
    BinarySearchTree flippedBst = new BinarySearchTree();
    for (int key : keys) {
        flippedBst.insert(key);
    }
    flippedBst.flip(flippedBst.root); // Flip it after inserting
    return flippedBst;
}
```

- **Purpose**: Creates a new BST, fills it with the provided keys, and flips it to ensure the structure is correct after insertion.
  
**Example**: If we create a flipped BST from `10, 5, 15`, it will be:
```
    10
   /  \
  15   5
```

#### 8. Main Method

```java
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

    // Display

 the pre-order traversal of the flipped BST
    System.out.println("Pre-order Traversal after filling flipped BST:");
    flippedBst.preorderTraversal(flippedBst.root);
    System.out.println();
}
```

- **Input Handling**: Checks if command-line arguments (keys) are provided. If not, it prompts the user.
- **Building the Original BST**: Iterates through the command-line arguments, parses integers, and inserts them into the BST.
- **Pre-order Traversal**: Displays the structure of the original BST.
- **Flipping the BST**: Flips the original BST structure.
- **Creating Flipped BST**: Calls the `createFlippedBST` method to build a new flipped BST and displays its pre-order traversal.

### Example Usage

To run the program, compile it and provide distinct integers as command-line arguments. For example:

```bash
java BinarySearchTree 10 5 3 7 15 13 17
```

### Expected Output

```
Pre-order Traversal of BST:
10 5 3 7 15 13 17 
Pre-order Traversal after filling flipped BST:
10 15 17 13 5 7 3 
```

### Conclusion

The provided implementation efficiently constructs a Binary Search Tree, performs insertions, allows traversal, flips the tree, and creates a new flipped BST. This report highlights each component of the code, providing a clear understanding of how the Binary Search Tree operates in Java.