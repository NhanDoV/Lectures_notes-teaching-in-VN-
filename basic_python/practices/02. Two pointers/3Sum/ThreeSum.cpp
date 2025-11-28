#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <algorithm>   // sort
using namespace std;

class Solution {
public:

    // ----------------------------------------------------------------
    // 1. Brute Force (O(n^3))
    // ----------------------------------------------------------------
    vector<vector<int>> threeSumBruteForce(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        res.insert({nums[i], nums[j], nums[k]});
                    }
                }
            }
        }
        return vector<vector<int>>(res.begin(), res.end());
    }

    // ----------------------------------------------------------------
    // 2. Hash Map (O(n^2))
    // ----------------------------------------------------------------
    vector<vector<int>> threeSumHashMap(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> count;

        for (int num : nums) {
            count[num]++;
        }

        vector<vector<int>> res;

        for (int i = 0; i < nums.size(); i++) {
            count[nums[i]]--;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < nums.size(); j++) {
                count[nums[j]]--;
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int target = -(nums[i] + nums[j]);
                if (count[target] > 0) {
                    res.push_back({nums[i], nums[j], target});
                }
            }

            for (int j = i + 1; j < nums.size(); j++) {
                count[nums[j]]++;
            }
        }

        return res;
    }

    // ----------------------------------------------------------------
    // 3. Two Pointers (Optimal O(n^2))
    // ----------------------------------------------------------------
    vector<vector<int>> threeSumTwoPointers(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1, r = nums.size() - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum > 0) r--;
                else if (sum < 0) l++;
                else {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol;

    int n;
    std::cout << "Enter the number of elements in the array: ";
    std::cin >> n;

    std::vector<int> nums(n);
    std::cout << "Enter " << n << " integers separated by spaces: ";
    for (int i = 0; i < n; i++) {
        std::cin >> nums[i];
    }

    // Call one of the threeSum methods, for example two pointers optimal approach:
    std::vector<std::vector<int>> result = sol.threeSumTwoPointers(nums);

    std::cout << "Unique triplets that sum to zero:\n";
    for (const auto& triplet : result) {
        std::cout << triplet[0] << " " << triplet[1] << " " << triplet[2] << "\n";
    }

    return 0;
}
