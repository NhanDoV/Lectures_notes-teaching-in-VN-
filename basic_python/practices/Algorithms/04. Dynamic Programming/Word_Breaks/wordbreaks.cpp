#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

class Solution {
public:

    // 1. Pure Recursion (TLE)
    bool wordBreak_recursive(const std::string& s, const std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        return dfs_recursive(s, wordSet, 0);
    }
    bool dfs_recursive(const std::string& s, const std::unordered_set<std::string>& wordSet, int i) {
        if (i == (int)s.size()) return true;
        for (int j = i; j < (int)s.size(); j++) {
            if (wordSet.count(s.substr(i, j - i + 1))) {
                if (dfs_recursive(s, wordSet, j + 1)) return true;
            }
        }
        return false;
    }

    // 2. Recursion + HashSet (same complexity, still TLE)
    bool wordBreak_hashset(const std::string& s, const std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        return dfs_hashset(s, wordSet, 0);
    }
    bool dfs_hashset(const std::string& s, const std::unordered_set<std::string>& wordSet, int i) {
        if (i == (int)s.size()) return true;
        for (int j = i; j < (int)s.size(); j++) {
            if (wordSet.count(s.substr(i, j - i + 1))) {
                if (dfs_hashset(s, wordSet, j + 1)) return true;
            }
        }
        return false;
    }

    // 3. Top-Down DP (Memo) with scanning wordDict
    std::unordered_map<int, bool> memo_topdown;
    bool wordBreak_topdown(const std::string& s, const std::vector<std::string>& wordDict) {
        memo_topdown.clear();
        memo_topdown[(int)s.size()] = true;
        return dfs_topdown(s, wordDict, 0);
    }
    bool dfs_topdown(const std::string& s, const std::vector<std::string>& wordDict, int i) {
        if (memo_topdown.count(i)) return memo_topdown[i];
        for (const auto& w : wordDict) {
            if (i + (int)w.size() <= (int)s.size() && s.substr(i, w.size()) == w) {
                if (dfs_topdown(s, wordDict, i + (int)w.size())) {
                    return memo_topdown[i] = true;
                }
            }
        }
        return memo_topdown[i] = false;
    }

    // 4. Top-Down DP + HashSet + Max Word Length (optimized top-down)
    std::unordered_set<std::string> wordSet_hash;
    std::vector<int> memo_hash;
    int maxWordLen;
    bool wordBreak_topdown_hash(const std::string& s, const std::vector<std::string>& wordDict) {
        wordSet_hash.clear();
        wordSet_hash.insert(wordDict.begin(), wordDict.end());
        memo_hash.assign((int)s.size(), -1);
        maxWordLen = 0;
        for (const auto& w : wordDict) maxWordLen = std::max(maxWordLen, (int)w.size());
        return dfs_topdown_hash(s, 0);
    }
    bool dfs_topdown_hash(const std::string& s, int i) {
        if (i == (int)s.size()) return true;
        if (memo_hash[i] != -1) return memo_hash[i];
        for (int j = i; j < std::min(i + maxWordLen, (int)s.size()); j++) {
            if (wordSet_hash.count(s.substr(i, j - i + 1))) {
                if (dfs_topdown_hash(s, j + 1)) {
                    return memo_hash[i] = 1;
                }
            }
        }
        return memo_hash[i] = 0;
    }

    // 5. Bottom-Up DP (best iterative)
    bool wordBreak_bottomup(const std::string& s, const std::vector<std::string>& wordDict) {
        std::vector<bool> dp((int)s.size() + 1, false);
        dp[(int)s.size()] = true;
        for (int i = (int)s.size() - 1; i >= 0; i--) {
            for (const auto& w : wordDict) {
                if (i + (int)w.size() <= (int)s.size() &&
                    s.substr(i, w.size()) == w &&
                    dp[i + (int)w.size()]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};

int main() {
    Solution sol;
    std::string s;
    int dict_size, method;

    std::cout << "Enter the string s (e.g: applepenapple): ";
    std::getline(std::cin, s);

    std::cout << "Enter the number of words in dictionary (e.g, 2): ";
    std::cin >> dict_size;
    std::cin.ignore();

    std::vector<std::string> wordDict(dict_size);
    std::cout << "Enter dictionary words (apple, pen) one per line:\n";
    for (int i = 0; i < dict_size; i++) {
        std::getline(std::cin, wordDict[i]);
    }

    std::cout << "Select the method (1-5):\n"
              << "1: Recursive\n"
              << "2: Recursion + HashSet\n"
              << "3: Top-Down DP\n"
              << "4: Optimized Top-Down DP + HashSet\n"
              << "5: Bottom-Up DP\n";
    std::cin >> method;

    bool result = false;
    switch (method) {
        case 1:
            result = sol.wordBreak_recursive(s, wordDict);
            break;
        case 2:
            result = sol.wordBreak_hashset(s, wordDict);
            break;
        case 3:
            result = sol.wordBreak_topdown(s, wordDict);
            break;
        case 4:
            result = sol.wordBreak_topdown_hash(s, wordDict);
            break;
        case 5:
            result = sol.wordBreak_bottomup(s, wordDict);
            break;
        default:
            std::cout << "Invalid method selected\n";
            return 1;
    }

    std::cout << "Can the string be segmented? " << std::boolalpha << result << "\n";

    return 0;
}