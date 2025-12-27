#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <unordered_map>
using namespace std;

class GroupAnagrams {
public:
    vector<vector<string>> usingSort(vector<string>& strs) {
        map<string, vector<string>> res;
        for (const string& s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            res[sorted_s].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
    
    vector<vector<string>> usingHash(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const string& s : strs) {
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }
            
            // Convert count to string key
            string key;
            for (int num : count) {
                key += to_string(num) + ",";
            }
            res[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};

int main() {
    cout << "Enter your list of strings (type one word per line):" << endl;
    int n_words;
    cout << "Number of words: ";
    cin >> n_words;
    cin.ignore(); // Clear newline character
    
    vector<string> raw;
    for (int i = 0; i < n_words; i++) {
        string vocab;
        cout << "\t " << (1 + i) << ": \t";
        getline(cin, vocab);
        raw.push_back(vocab);
    }
    
    string method;
    cout << "Choose method: 'sort' or 'hash': ";
    getline(cin, method);
    transform(method.begin(), method.end(), method.begin(), ::tolower);
    
    GroupAnagrams solver;
    vector<vector<string>> result;
    
    if (method.find("hash") != string::npos) {
        result = solver.usingHash(raw);
    } else {
        result = solver.usingSort(raw);
    }
    
    cout << "Grouped anagrams: ";
    for (const auto& group : result) {
        cout << "[";
        for (size_t i = 0; i < group.size(); i++) {
            cout << "\"" << group[i] << "\"";
            if (i < group.size() - 1) cout << ", ";
        }
        cout << "] ";
    }
    cout << endl;
    
    return 0;
}