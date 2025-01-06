#include <iostream>
#include <vector>
#include <climits>
#include <sstream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

// Function to compute the optimal BST cost and the root matrix
void optimal_bst(const vector<float>& p, const vector<float>& q, int n, vector<vector<float>>& e, vector<vector<float>>& w, vector<vector<int>>& root) {
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

int he;

// Function for task 3 and 4
vector<int> task3n4(vector<vector<int>>& root, int n, int i, int j, map<int, int>& height, int& h) {
    if (i > j || i < 1 || j > n) {
        return{};
    }

    vector <int> pre;
    pre.push_back(root[i][j]);
    height[root[i][j]] = h;
    h++;

    vector<int> left = task3n4(root, n, i, root[i][j] -1, height, h);
    vector<int> right = task3n4(root, n, root[i][j] + 1, j, height, h);

    for (auto i : left) {
        pre.push_back(i);
    }

    for (auto i : right) {
        pre.push_back(i);
    }

    h--;
    
    return pre;
}

int main(int argc, char* argv[]) {

    if(argc != 2) {
        cerr << "Usage:" << argv[0] << "inputFile.txt" << "\n";
        return 0;
    }

    // Reading the input file from terminal
    string filename = argv[1];

    // Open the input file to read test cases
    ifstream inputFile(filename);
    if (!inputFile) {
        cerr << "Error opening input file!" << endl;
        return 1;
    }

    // Open the output file to write results
    ofstream outputFile("output.txt");
    if (!outputFile) {
        cerr << "Error opening output file!" << endl;
        return 1;
    }

    // Process the input data for each test case
    string line;
    
    while (getline(inputFile, line)) {
        if (line.empty()) continue;  // Skip empty lines

        // Read number of keys
        int n = stoi(line);

        // Read probabilities p
        vector<float> p(n);
        getline(inputFile, line);
        istringstream p_stream(line);
        int temp;
        p_stream >> temp; // Skipping the first value which is always 0
        for (int i = 0; i <= n; ++i) {
            p_stream >> p[i];
        }

        // Read dummy probabilities q
        vector<float> q(n);
        getline(inputFile, line);
        istringstream q_stream(line);
        for (int i = 0; i <= n; ++i) {
            q_stream >> q[i];
        }

        // Summing up all elements in p
        int sump = 0;
        for (int i = 0; i <= n; i++) {
            sump += p[i];
        }

        // Summing up all elements in q
        int sumq = 0;
        for (int i = 0; i <= n; i++) {
            sumq += q[i];
        }
        outputFile << sump << " " << sumq << endl;
        
        //----------------------------------------------
        // Declare matrices for e, w, and root
        vector<vector<float>> e, w;
        vector<vector<int>> root;

        // Calculate minimum cost and root structure
        optimal_bst(p, q, n, e, w, root);
        float min_cost = e[0][n];
        map<int, int> height;
        int h;
        vector<int> bst_structure = task3n4(root, n, 0, n - 1, height, h);

        // // Write the result to the output file
        outputFile << min_cost << endl;
        outputFile << he << endl;
        for (int i = 0; i < bst_structure.size() ; i++) {
            outputFile << bst_structure[i];
        }
        
        // Close the input and output files
        inputFile.close();
        outputFile.close();
    }
}