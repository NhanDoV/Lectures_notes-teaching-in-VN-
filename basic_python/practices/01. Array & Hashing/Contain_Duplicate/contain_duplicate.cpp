#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>

class ContainDuplicate {
public:

    // Approach 1: brute force
    // Time: O(n^2), Space: O(1)
    bool brute_force(const std::vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] == arr[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    // Approach 2: sorting
    // Time: O(n log n), Space: O(1) if in-place
    bool sorting(std::vector<int> arr) {  
        // pass by value to avoid modifying original
        std::sort(arr.begin(), arr.end());
        
        for (int i = 1; i < (int)arr.size(); i++) {
            if (arr[i] == arr[i - 1]) {
                return true;
            }
        }
        return false;
    }

    // Approach 3: hashmap counting
    // Time: O(n), Space: O(n)
    bool hash_count(const std::vector<int>& arr) {
        if (arr.empty()) return false;

        std::unordered_map<int, int> mp;

        for (int val : arr) {
            mp[val]++;           // count
            if (mp[val] > 1) {   // early exit
                return true;
            }
        }

        return false;
    }

    // Approach 4: hash set with early return
    // Time: O(n), Space: O(n)
    bool hash_set(const std::vector<int>& arr) {
        std::unordered_set<int> seen;

        for (int num : arr) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }

        return false;
    }

    // Approach 5: comparing lengths
    // Time: O(n), Space: O(n)
    bool hash_set_length(const std::vector<int>& arr) {
        std::unordered_set<int> s(arr.begin(), arr.end());
        return s.size() < arr.size();
    }
};

int main() {
    ContainDuplicate sol;
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;
    
    std::vector<int> arr(n);
    std::cout << "Enter " << n << " elements separated by spaces: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    std::cout << std::boolalpha << sol.hash_set(arr) << "\n";

    return 0;
}