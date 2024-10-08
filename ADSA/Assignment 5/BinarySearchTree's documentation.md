# Detailed Report on Binary Search Tree (BST) Implementation in Java

## Introduction
This report provides a comprehensive overview of a Binary Search Tree (BST) implementation in Java. The BST allows for efficient data storage and retrieval, and this particular implementation includes functionality for inserting nodes, flipping the tree, and filling it with sorted keys. Each section of the code will be discussed in detail, along with relevant examples to clarify the logic and operations performed.

## Overview of Binary Search Tree (BST)
A Binary Search Tree is a binary tree where each node has at most two children, referred to as the left and right child. In a BST:
- The left child contains values less than its parent node.
- The right child contains values greater than its parent node.

This structure allows for efficient searching, insertion, and deletion operations.

## Code Structure
Here is the complete Java code for the Binary Search Tree implementation:

```java
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
        fillInOrder(node.left, keys);  // Traverse the left subtree
        node.val = keys.remove(0);  // Replace the current node's value with the next sorted key
        fillInOrder(node.right, keys);  // Traverse the right subtree
    }

    // Helper function to fill the tree after flipping
    public void fill(List<Integer> keys) {
        Collections.sort(keys);  // Sort the keys before filling in in-order traversal
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

        // 7. Fill the flipped tree with the original keys in sorted order (in-order filling)
        bst.fill(keys);

        // 8. Print pre-order traversal after filling the flipped tree
        System.out.println("Pre-order traversal after filling the flipped BST with sorted keys:");
        bst.preorderTraversal(bst.root);
        System.out.println();

        scanner.close();
    }
}
```

## Code Breakdown

### 1. Node Class
```java
class Node {
    int val;
    Node left, right;

    public Node(int key) {
        val = key;
        left = right = null;
    }
}
```
- **Purpose**: Represents each node in the tree.
- **Attributes**:
  - `val`: Holds the value of the node.
  - `left`: Reference to the left child node.
  - `right`: Reference to the right child node.
- **Constructor**: Initializes the node with a key and sets both children to `null`.

### 2. BinarySearchTree Class
#### Attributes
```java
class BinarySearchTree {
    Node root;
}
```
- **root**: The root node of the BST.

#### Insertion Method
```java
public void insert(int key) {
    if (root == null) {
        root = new Node(key);
    } else {
        insertRec(root, key);
    }
}
```
- **Purpose**: Inserts a new key into the BST.
- **Logic**:
  - If the tree is empty, the new key becomes the root.
  - If not, the `insertRec` method is called to find the correct position recursively.

##### Recursive Insert Method
```java
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
```
- **Purpose**: Helper method to insert a key recursively.
- **Logic**:
  - If the key is smaller than the current node's value, it moves left; if greater, it moves right.
  - This process continues until an empty spot is found.

#### Pre-order Traversal Method
```java
public void preorderTraversal(Node node) {
    if (node != null) {
        System.out.print(node.val + " ");
        preorderTraversal(node.left);
        preorderTraversal(node.right);
    }
}
```
- **Purpose**: Displays the tree in pre-order (Root, Left, Right).
- **Logic**: Recursively visits the root, then the left subtree, followed by the right subtree.

#### Flip Method
```java
public void flip(Node node) {
    if (node != null) {
        Node temp = node.left;
        node.left = node.right;
        node.right = temp;
        flip(node.left);
        flip(node.right);
    }
}
```
- **Purpose**: Swaps the left and right children of every node in the tree.
- **Logic**: Recursively flips the children until all nodes are processed.

#### Fill Method
```java
public void fill(List<Integer> keys) {
    Collections.sort(keys);  // Sort the keys before filling in in-order traversal
    fillInOrder(root, keys);
}
```
- **Purpose**: Fills the flipped tree with sorted keys.
- **Logic**: Sorts the list of keys and then calls `fillInOrder`.

##### In-order Filling Method
```java
public void fillInOrder(Node node, List<Integer> keys) {
    if (node == null) {
        return;
    }
    fillInOrder(node.left, keys);  // Traverse the left subtree
    node.val = keys.remove(0);  // Replace the current node's value with the next sorted key
    fillInOrder(node.right, keys);  // Traverse the right subtree
}
```
- **Purpose**: Fills the tree in in-order (Left, Root, Right) with sorted keys.
- **Logic**: Recursively visits each node, replacing its value with the next key from the sorted list.

### 3. Main Method
```java
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
    System

.out.println("Pre-order traversal after flipping:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    // 7. Fill the flipped tree with the original keys in sorted order (in-order filling)
    bst.fill(keys);

    // 8. Print pre-order traversal after filling the flipped tree
    System.out.println("Pre-order traversal after filling the flipped BST with sorted keys:");
    bst.preorderTraversal(bst.root);
    System.out.println();

    scanner.close();
}
```
- **Purpose**: The main function drives the program.
- **Steps**:
  1. **Input**: Prompts the user to enter keys for the BST.
  2. **Parsing**: Splits the input string into individual keys and converts them to integers.
  3. **Insertion**: Inserts each key into the BST.
  4. **Traversal**: Prints the pre-order traversal before and after flipping the tree.
  5. **Flipping**: Calls the flip method on the tree.
  6. **Filling**: Fills the flipped tree with sorted keys and prints the final traversal.

### Example Usage
When the user runs the program and inputs the keys "5 3 7 2 4 6 8", the following operations occur:

1. **Insertion**: The keys are inserted into the BST, resulting in the structure:
```
        5
      /   \
     3     7
    / \   / \
   2   4 6   8
```

2. **Pre-order Traversal Before Flipping**: Outputs: `5 3 2 4 7 6 8`

3. **Flipping**: The tree is flipped to become:
```
        5
      /   \
     7     3
    / \   / \
   8   6 4   2
```

4. **Pre-order Traversal After Flipping**: Outputs: `5 7 8 6 3 4 2`

5. **Filling**: The flipped tree is filled with the sorted keys, resulting in:
```
        4
      /   \
     6     5
    / \   / \
   7   8 2   3
```

6. **Pre-order Traversal After Filling**: Outputs: `4 6 7 8 5 2 3`

## Conclusion
The provided Java implementation of a Binary Search Tree is a clear demonstration of fundamental data structure operations including insertion, traversal, flipping, and filling. The code is modular and follows good programming practices, making it easy to understand and maintain. This report details each component of the code, illustrating its functionality with explanations and examples, providing a comprehensive understanding of the BST operations.