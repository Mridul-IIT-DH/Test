// Matrix chain multiplication

#include <iostream>
#include <vector>
#include <fstream>
#include <climits>
#include <sstream>

using namespace std;

// Function to perform matrix chain multiplication
int matrixChainOrder(const vector<int>& dims, int n, vector<vector<int>>& split) {
    vector<vector<int>> dp(n, vector<int>(n, 0));

    // l is the chain length.
    for (int len = 2; len < n; len++) {
        for (int i = 0; i < n - len; i++) {
            int j = i + len;
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                int q = dp[i][k] + dp[k][j] + dims[i] * dims[k] * dims[j];
                if (q < dp[i][j]) {
                    dp[i][j] = q;
                    split[i][j] = k; // record the split point
                }
            }
        }
    }

    return dp[0][n - 1];  // Minimum number of scalar multiplications
}

// Function to print the optimal order of matrix multiplication
void printOptimalOrder(const vector<vector<int>>& split, int i, int j, ofstream& outputFile) {
    if (i == j) {
        outputFile << "A" << i + 1;  // Print matrix name (1-based index)
    } else {
        outputFile << "(";
        printOptimalOrder(split, i, split[i][j], outputFile); // Recurse for the left half
        outputFile << " x ";
        printOptimalOrder(split, split[i][j] + 1, j, outputFile); // Recurse for the right half
        outputFile << ")";
    }
}

int main() {
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");  // Move this line here to ensure it's declared before use
    
    string line;
    while (getline(inputFile, line)) {
        // Skip empty lines
        if (line.empty()) continue;

        // Read the number of matrices for the test case
        stringstream ss(line);
        int n;
        ss >> n;

        // To store the dimensions of the matrices
        vector<int> dims(n + 1);

        // Read the matrix dimensions
        for (int i = 0; i < n; i++) {
            int r, c;
            getline(inputFile, line);
            stringstream ss(line);
            ss >> r >> c;

            if (i == 0) {
                dims[i] = r;  // First matrix's row
            }
            dims[i + 1] = c;  // Next matrix's column
        }

        // Initialize split table for tracking the optimal order
        vector<vector<int>> split(n, vector<int>(n, 0));

        // Compute the minimum scalar multiplications for this test case
        int result = matrixChainOrder(dims, n + 1, split);
        outputFile << "Minimum number of scalar multiplications: " << result << endl;

        // Output the optimal order of multiplication
        outputFile << "Optimal order of multiplication: ";
        printOptimalOrder(split, 0, n - 1, outputFile);  // Pass outputFile as a parameter
        outputFile << "\n" << "\n" << endl;

        // Read the empty line between test cases if present
        getline(inputFile, line); // Skip the empty line
    }

    inputFile.close();
    outputFile.close();
    return 0;
}


// Buy and sell stock

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

struct ProfitResult {
    int profit;
    int buyDay;
    int sellDay;
    int buyPrice;
    int sellPrice;
};

// Function to find all maximum profits and corresponding buy/sell days and prices
vector<ProfitResult> findMaxProfitPairs(const vector<int>& prices) {
    vector<ProfitResult> result;

    int n = prices.size();
    if (n <= 1) return result;

    // Traverse through the price array to find profitable transactions
    for (int i = 0; i < n - 1; ++i) {
        // If a profit is possible (price[i] < price[i+1]), we consider this as a buy/sell pair
        if (prices[i] < prices[i + 1]) {
            int buyDay = i + 1;  // Day to buy (1-based index)
            int sellDay = i + 2; // Day to sell (1-based index)
            int buyPrice = prices[i];
            int sellPrice = prices[i + 1];
            int profit = sellPrice - buyPrice;
            result.push_back({profit, buyDay, sellDay, buyPrice, sellPrice});
        }
    }

    return result;
}

int main() {
    // Open the input file and output file
    ifstream inputFile("bss.txt");
    ofstream outputFile("output.txt");

    if (!inputFile) {
        cerr << "Error opening input file!" << endl;
        return 1;
    }

    if (!outputFile) {
        cerr << "Error opening output file!" << endl;
        return 1;
    }

    string line;
    while (getline(inputFile, line)) {
        // Skip empty lines
        if (line.empty()) {
            continue;
        }

        // Read the number of days for the test case
        int numDays = stoi(line);

        vector<int> prices(numDays);
        // Read the prices for the given number of days
        for (int i = 0; i < numDays; ++i) {
            getline(inputFile, line);  // Read the next price
            prices[i] = stoi(line);
        }

        // Process the prices to find the maximum profit transactions
        vector<ProfitResult> profitPairs = findMaxProfitPairs(prices);

        // If there are profitable transactions, write them to the output file
        if (!profitPairs.empty()) {
            int totalProfit = 0;
            outputFile << "Maximum profit transactions:\n";
            for (const auto& pair : profitPairs) {
                outputFile << "Buy on day " << pair.buyDay << " (price: " << pair.buyPrice 
                           << ") and sell on day " << pair.sellDay << " (price: " << pair.sellPrice 
                           << ") for a profit of " << pair.profit << "\n";
                totalProfit += pair.profit;
            }
            outputFile << "Total maximum profit: " << totalProfit << "\n\n";
        } else {
            outputFile << "No profitable transactions can be made.\n\n";
        }

        // Skip any extra empty line before the next test case (if there's any)
        if (getline(inputFile, line) && line.empty()) {
            continue;
        }
    }

    // Close the files
    inputFile.close();
    outputFile.close();

    return 0;
}


// Traversal

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;

// Function to perform DFS (Depth-First Search)
void dfs(const map<int, vector<int>>& graph, int start, set<int>& visited, ofstream& outputFile) {
    visited.insert(start);  // mark the current node as visited
    outputFile << start << " ";   // write the current node to output file
    
    // Explore all neighbors of the current node
    for (int neighbor : graph.at(start)) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited, outputFile);  // recursively visit the neighbor
        }
    }
}

// Function to perform BFS (Breadth-First Search)
void bfs(const map<int, vector<int>>& graph, int start, ofstream& outputFile) {
    set<int> visited;  // set to track visited nodes
    queue<int> q;      // queue to manage the BFS process
    visited.insert(start);
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        outputFile << node << " ";  // write the current node to output file

        // Visit all unvisited neighbors
        for (int neighbor : graph.at(node)) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}

// Function to parse input and create the adjacency list for each graph
vector<map<int, vector<int>>> parse_graph_input(const string& filename) {
    ifstream file(filename);
    vector<map<int, vector<int>>> graphs;
    string line;
    stringstream graph_stream;
    map<int, vector<int>> graph;
    
    // Read the file line by line
    while (getline(file, line)) {
        if (line.empty()) {
            if (!graph.empty()) {
                graphs.push_back(graph);
                graph.clear();
            }
            continue;
        }

        stringstream line_stream(line);
        int node;
        vector<int> neighbors;
        
        // Read the node and its neighbors
        line_stream >> node;
        int neighbor;
        while (line_stream >> neighbor) {
            neighbors.push_back(neighbor);
        }

        graph[node] = neighbors;
    }

    // Don't forget to add the last graph if the file doesn't end with an empty line
    if (!graph.empty()) {
        graphs.push_back(graph);
    }

    return graphs;
}

// Function to process all graphs and perform DFS and BFS, with output to a file
void process_multiple_graphs(const string& filename, const string& outputFilename) {
    vector<map<int, vector<int>>> graphs = parse_graph_input(filename);

    // Open the output file
    ofstream outputFile(outputFilename);
    if (!outputFile.is_open()) {
        cerr << "Error opening output file!" << endl;
        return;
    }

    // Process each graph
    for (size_t idx = 0; idx < graphs.size(); ++idx) {
        outputFile << "\nGraph " << idx + 1 << ":\n";

        // Perform DFS
        outputFile << "DFS Traversal: ";
        set<int> visited_dfs;
        dfs(graphs[idx], graphs[idx].begin()->first, visited_dfs, outputFile);  // start DFS from the first node
        outputFile << endl;

        // Perform BFS
        outputFile << "BFS Traversal: ";
        bfs(graphs[idx], graphs[idx].begin()->first, outputFile);  // start BFS from the first node
        outputFile << endl;
    }

    outputFile.close();  // Close the output file
}

int main() {
    string input_filename = "input.txt";  // specify the input filename
    string output_filename = "output.txt";  // specify the output filename

    // Process graphs and write the result to the output file
    process_multiple_graphs(input_filename, output_filename);

    cout << "Output has been written to " << output_filename << endl;
    return 0;
}


// Optimal BST

#include <iostream>
#include <vector>
#include <climits>
#include <sstream>
#include <fstream>

using namespace std;

// Function to compute the optimal BST cost and the root matrix
void optimal_bst(const vector<int>& keys, const vector<float>& p, const vector<float>& q, int n, vector<vector<float>>& e, vector<vector<float>>& w, vector<vector<int>>& root) {
    // Initialize matrices
    e.resize(n + 1, vector<float>(n + 1, 0));
    w.resize(n + 1, vector<float>(n + 1, 0));
    root.resize(n, vector<int>(n, 0));

    // Initialize the tables for the probabilities
    for (int i = 0; i <= n; ++i) {
        e[i][i] = q[i];
        w[i][i] = q[i];
    }

    // Compute minimum cost and structure
    for (int l = 1; l <= n; ++l) {  // l is the length of the chain
        for (int i = 0; i <= n - l; ++i) {
            int j = i + l - 1;
            e[i][j + 1] = INT_MAX;
            w[i][j + 1] = w[i][j] + p[j] + q[j + 1];
            for (int r = i; r <= j; ++r) {
                float t = e[i][r] + e[r + 1][j + 1] + w[i][j + 1];
                if (t < e[i][j + 1]) {
                    e[i][j + 1] = t;
                    root[i][j] = r;
                }
            }
        }
    }
}

// Function to recursively build the BST structure as a string using the root matrix
string build_bst_structure(const vector<vector<int>>& root, const vector<int>& keys, int i, int j, int parent = -1, const string& side = "Root") {
    if (i > j) {
        return side + " Subtree of " + to_string(parent) + ": None\n";
    }
    int r = root[i][j];
    string subtree = (parent != -1) ? side + " Subtree of " + to_string(parent) + ": Key " + to_string(keys[r]) + "\n"
                                    : "Root of BST: Key " + to_string(keys[r]) + "\n";
    subtree += build_bst_structure(root, keys, i, r - 1, keys[r], "Left");
    subtree += build_bst_structure(root, keys, r + 1, j, keys[r], "Right");
    return subtree;
}

int main() {
    // Open the input file to read test cases
    ifstream input_file("input.txt");
    if (!input_file) {
        cerr << "Error opening input file!" << endl;
        return 1;
    }

    // Open the output file to write results
    ofstream output_file("output.txt");
    if (!output_file) {
        cerr << "Error opening output file!" << endl;
        return 1;
    }

    // Process the input data for each test case
    string line;
    
    while (getline(input_file, line)) {
        if (line.empty()) continue;  // Skip empty lines between test cases

        // Read number of keys
        int n = stoi(line);

        // Read keys
        vector<int> keys(n);
        getline(input_file, line);
        istringstream keys_stream(line);
        for (int i = 0; i < n; ++i) {
            keys_stream >> keys[i];
        }

        // Read probabilities p
        vector<float> p(n);
        getline(input_file, line);
        istringstream p_stream(line);
        for (int i = 0; i < n; ++i) {
            p_stream >> p[i];
        }

        // Read probabilities q (including the first and last dummy probabilities)
        vector<float> q(n + 1);
        getline(input_file, line);
        istringstream q_stream(line);
        for (int i = 0; i <= n; ++i) {
            q_stream >> q[i];
        }

        // Declare matrices for e, w, and root
        vector<vector<float>> e, w;
        vector<vector<int>> root;

        // Calculate minimum cost and root structure
        optimal_bst(keys, p, q, n, e, w, root);
        float min_cost = e[0][n];
        string bst_structure = build_bst_structure(root, keys, 0, n - 1);

        // Write the result to the output file
        output_file << "Test Case Result:\n";
        output_file << "Minimum Cost: " << min_cost << endl;
        output_file << bst_structure;
        output_file << "\n-------------------------------------------------------------\n";
    }

    // Close the input and output files
    input_file.close();
    output_file.close();

    return 0;
}

// Min-Max Heap

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <climits>

using namespace std;

// Min-Heap Class
class MinHeap {
public:
    vector<int> heap;

    // Function to heapify the tree (Min-Heap property)
    void heapify(int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < heap.size() && heap[left] < heap[smallest]) {
            smallest = left;
        }
        if (right < heap.size() && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapify(smallest);
        }
    }

    // Function to build the heap
    void buildHeap() {
        int n = heap.size();
        for (int i = n / 2 - 1; i >= 0; --i) {
            heapify(i);
        }
    }

    // Function to extract the root (minimum element)
    int extractMin() {
        if (heap.size() == 0) return INT_MAX;

        int root = heap[0];
        if (heap.size() > 1) {
            heap[0] = heap.back();
            heap.pop_back();
            heapify(0);
        } else {
            heap.pop_back();
        }

        return root;
    }
};

// Max-Heap Class
class MaxHeap {
public:
    vector<int> heap;

    // Function to heapify the tree (Max-Heap property)
    void heapify(int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(heap[i], heap[largest]);
            heapify(largest);
        }
    }

    // Function to build the heap
    void buildHeap() {
        int n = heap.size();
        for (int i = n / 2 - 1; i >= 0; --i) {
            heapify(i);
        }
    }

    // Function to extract the root (maximum element)
    int extractMax() {
        if (heap.size() == 0) return INT_MIN;

        int root = heap[0];
        if (heap.size() > 1) {
            heap[0] = heap.back();
            heap.pop_back();
            heapify(0);
        } else {
            heap.pop_back();
        }

        return root;
    }
};

int main() {
    // Open the input file
    ifstream input_file("input.txt");
    if (!input_file) {
        cerr << "Error opening input file!" << endl;
        return 1;
    }

    vector<int> input_numbers;

    // Open the output file
    ofstream output_file("output.txt");
    if (!output_file) {
        cerr << "Error opening output file!" << endl;
        return 1;
    }

    string line;
    bool first_case = true;

    // Read input file line-by-line
    while (getline(input_file, line)) {
        // Skip empty lines (for multiple test cases)
        if (line.empty()) {
            continue;
        }

        // Process each test case
        istringstream iss(line);
        input_numbers.clear();  // Clear the vector for each test case
        int num;
        while (iss >> num) {
            input_numbers.push_back(num);
        }

        // Initialize Min-Heap and Max-Heap objects for each test case
        MinHeap minHeap;
        MaxHeap maxHeap;

        minHeap.heap = input_numbers;
        maxHeap.heap = input_numbers;

        // Build the heaps
        minHeap.buildHeap();
        maxHeap.buildHeap();

        // Extract the root (Min from Min-Heap, Max from Max-Heap)
        int minExtracted = minHeap.extractMin();
        int maxExtracted = maxHeap.extractMax();

        // Write the result to the output file
        if (!first_case) {
            output_file << "\n-------------------------------------------------------------\n";
        }
        first_case = false;

        output_file << "Min-Heap Extracted (Root): " << minExtracted << endl;
        output_file << "Min-Heap After Extraction: ";
        for (int num : minHeap.heap) {
            output_file << num << " ";
        }
        output_file << endl;

        output_file << "Max-Heap Extracted (Root): " << maxExtracted << endl;
        output_file << "Max-Heap After Extraction: ";
        for (int num : maxHeap.heap) {
            output_file << num << " ";
        }
        output_file << endl;
    }

    // Close the files
    input_file.close();
    output_file.close();

    return 0;
}
