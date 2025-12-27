#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <queue>
using namespace std;

class TopKFrequent {
public:

    // ---------------------------------------------------------
    // Approach 1: Sort by frequency (O(n log n))
    // ---------------------------------------------------------
    vector<int> using_sorting(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<pair<int, int>> arr; // (freq, num)
        for (const auto& p : count) {
            arr.push_back({p.second, p.first});
        }

        sort(arr.rbegin(), arr.rend());  // sort descending on freq

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(arr[i].second);
        }
        return res;
    }

    // ---------------------------------------------------------
    // Approach 2: Min Heap (O(n log k))
    // ---------------------------------------------------------
    vector<int> using_minheap(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        // min-heap storing pair (frequency, number)
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> heap;

        for (auto& entry : count) {
            heap.push({entry.second, entry.first});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;
        while (!heap.empty()) {
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;
    }
};

int main() {
    TopKFrequent sol;

    int n, k;
    std::cout << "Enter number of elements: ";
    std::cin >> n;
    
    std::vector<int> nums(n);
    std::cout << "Enter " << n << " elements separated by spaces: ";
    for (int i = 0; i < n; i++) {
        std::cin >> nums[i];
    }

    std::cout << "Enter k: ";
    std::cin >> k;

    std::vector<int> result = sol.using_sorting(nums, k);
    // Or use using_minheap(nums, k) if you prefer

    std::cout << "Top " << k << " frequent elements: ";
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    return 0;
}