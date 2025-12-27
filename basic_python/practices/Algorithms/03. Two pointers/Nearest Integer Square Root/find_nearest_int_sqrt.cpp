#include <iostream>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <tuple>

class Find_Nearest_sqrt_integer {
public:
    // Approach 1
    // Time complexity: O(num/2)    Space complexity: O(num/2)
    int brute_force(int num) {
        std::unordered_map<int, int> hashmap;
        for (int digit = 1; digit <= num / 2 + 1; ++digit) {
            int num_sq = digit * digit;
            int diff = std::abs(num - num_sq);
            hashmap[diff] = digit;
        }
        auto min_it = std::min_element(hashmap.begin(), hashmap.end(),
            [](const auto& a, const auto& b) { return a.first < b.first; });
        return min_it->second;
    }

    // Approach 2
    // Time complexity: O(log n)    Space complexity: O(1)
    // Returns the closest integer(s) for the sqrt of num
    std::tuple<int, int, int> using_2pointers(int num) {
        int left = 1, right = num / 2 + 1;
        int mid = 0;
        while (left <= right) {
            mid = left + (right - left) / 2;
            int num_sq = mid * mid;
            if (num_sq == num) {
                return std::make_tuple(mid, mid, mid);
            }
            else if (num_sq < num) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        // After loop ends right < left, so closest integers are right and left
        return std::make_tuple(right, -1, left);
    }
};

int main() {
    Find_Nearest_sqrt_integer finder; // You must run with c++20 and later

    int num;
    std::cout << "Enter the number: ";
    std::cin >> num;

    int closest = finder.brute_force(num);
    std::cout << "Brute force closest sqrt integer to " << num << " is " << closest << std::endl;

    auto [left, mid, right] = finder.using_2pointers(num);
    std::cout << "Using two pointers for " << num << ": ";
    if (mid != -1) {
        std::cout << "Exact sqrt is " << mid << std::endl;
    } else {
        std::cout << "Closest sqrt integers are " << left << " and " << right << std::endl;
    }

    return 0;
}