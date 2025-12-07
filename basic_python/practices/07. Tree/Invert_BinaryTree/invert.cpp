#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// ---------- build tree (level-order, allow None) ----------
TreeNode* build_tree(const vector<optional<int>>& arr) {
    if (arr.empty() || !arr[0].has_value())
        return nullptr;

    TreeNode* root = new TreeNode(arr[0].value());
    queue<TreeNode*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < arr.size()) {
        TreeNode* node = q.front();
        q.pop();

        // left child
        if (i < arr.size() && arr[i].has_value()) {
            node->left = new TreeNode(arr[i].value());
            q.push(node->left);
        }
        i++;

        // right child
        if (i < arr.size() && arr[i].has_value()) {
            node->right = new TreeNode(arr[i].value());
            q.push(node->right);
        }
        i++;
    }
    return root;
}

// ---------- level order ----------
vector<int> level_order(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        result.push_back(node->val);
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    return result;
}

// ---------- height ----------
int height(TreeNode* node) {
    if (!node) return 0;
    return 1 + max(height(node->left), height(node->right));
}

// ---------- print top-down ----------
void print_top_down(TreeNode* root) {
    if (!root) {
        cout << "<empty tree>\n";
        return;
    }

    int h = height(root);
    int max_width = 1 << h; // 2^h

    // BFS including nullptr placeholders
    vector<vector<string>> levels;
    queue<TreeNode*> q;
    q.push(root);

    for (int lvl = 0; lvl < h; lvl++) {
        vector<string> level;
        queue<TreeNode*> next_q;

        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();

            if (node)
                level.push_back(to_string(node->val));
            else
                level.push_back("");

            if (node) {
                next_q.push(node->left);
                next_q.push(node->right);
            } else {
                next_q.push(nullptr);
                next_q.push(nullptr);
            }
        }

        levels.push_back(level);
        q = next_q;
    }

    // pretty-print
    for (int depth = 0; depth < levels.size(); depth++) {
        int spacing = max_width >> depth;

        cout << string(spacing / 2, ' ');
        for (string v : levels[depth]) {
            string cell = v;
            if (cell == "") cell = " ";
            cout << cell << string(spacing / 2, ' ');
        }
        cout << "\n";
    }
}

// ---------- invert tree BFS ----------
TreeNode* invertTree(TreeNode* root) {
    if (!root) return nullptr;
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        swap(node->left, node->right);
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    return root;
}

// ---------- main ----------
int main() {
    cout << "Input your array here: ";
    string raw;
    getline(cin, raw);

    // clean input
    for (char& c : raw)
        if (c == '[' || c == ']' || c == ',') c = ' ';

    stringstream ss(raw);
    string token;

    vector<optional<int>> arr;

    while (ss >> token) {
        if (token == "None" || token == "none" || token == "NULL")
            arr.push_back(nullopt);
        else
            arr.push_back(stoi(token));
    }

    TreeNode* root = build_tree(arr);

    cout << "\nInput Tree:\n";
    print_top_down(root);

    vector<int> before = level_order(root);
    cout << "Input level order: ";
    for (int v : before) cout << v << " ";
    cout << "\n\n";

    root = invertTree(root);

    cout << "Inverted Tree:\n";
    print_top_down(root);

    vector<int> after = level_order(root);
    cout << "Output level order: ";
    for (int v : after) cout << v << " ";
    cout << "\n";

    return 0;
}

/* ---------- For C++ 17
Input your array here: 1 2 3 4 5 6 7

Input Tree:
    1    
  2  3  
 4 5 6 7 
Input level order: 1 2 3 4 5 6 7 

Inverted Tree:
    1    
  3  2  
 7 6 5 4 
Output level order: 1 3 2 7 6 5 4 

-------- */