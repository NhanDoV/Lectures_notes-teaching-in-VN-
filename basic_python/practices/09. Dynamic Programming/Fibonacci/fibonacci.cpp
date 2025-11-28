#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

class Fibonacci {
public:

    // ----------------------------------------------------------
    // 1. Pure Recursive (Exponential Time)
    // Time: O(2^n)   |   Space: O(n)
    // ----------------------------------------------------------
    int recursive_approach(int n) {
        if (n < 0) {
            throw invalid_argument("n must be non-negative");
        }
        if (n == 0 || n == 1) {
            return n;
        }
        return recursive_approach(n - 1) + recursive_approach(n - 2);
    }


    // ----------------------------------------------------------
    // 2. Dynamic Programming (Linear Time, Linear Space)
    // Time: O(n)   |   Space: O(n)
    // ----------------------------------------------------------
    int dynamic_programming(int n) {
        if (n < 0) {
            throw invalid_argument("n must be non-negative");
        }
        if (n == 0) return 0;
        if (n == 1) return 1;

        vector<long long> dp(n + 1);
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }


    // ----------------------------------------------------------
    // 3. Dynamic Programming — Constant Space
    // Time: O(n)   |   Space: O(1)
    // ----------------------------------------------------------
    long long DP_no_memo(int n) {
        if (n <= 0) {
            throw invalid_argument("n must be greater than 0");
        }
        if (n == 1) return 1;
        if (n == 2) return 1;

        long long prev = 1, curr = 1;
        for (int i = 3; i <= n; i++) {
            long long next = prev + curr;
            prev = curr;
            curr = next;
        }
        return curr;
    }
};

int main() {
    Fibonacci fib;

    int n;
    std::cout << "Enter a non-negative integer n: ";
    std::cin >> n;

    try {
        std::cout << "Recursive approach: " << fib.recursive_approach(n) << "\n";
        std::cout << "Dynamic programming approach: " << fib.dynamic_programming(n) << "\n";

        // For DP no memo approach, check n should be > 0 due to your condition in function
        if (n > 0) {
            std::cout << "DP constant space approach: " << fib.DP_no_memo(n) << "\n";
        } else {
            std::cout << "DP constant space approach: Undefined for n <= 0\n";
        }
    } catch (const std::invalid_argument& e) {
        std::cout << "Error: " << e.what() << "\n";
    }

    return 0;
}
