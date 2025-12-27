#include <string>
#include <vector>
using namespace std;

class NumSub {
public:

    // ----------------------------------------------------------
    // 1. Brute Force
    // Time: O(n^3) (worst-case)
    // ----------------------------------------------------------
    long long brute_force(const string& s) {
        long long cnt = 0;
        int n = s.size();

        for (int i = 0; i < n; i++) {
            for (int width = 1; width <= n; width++) {
                if (i + width > n) break;               // avoid overflow

                // Check if substring is all '1'
                bool all_one = true;
                for (int k = 0; k < width; k++) {
                    if (s[i + k] != '1') {
                        all_one = false;
                        break;
                    }
                }
                if (all_one) cnt++;
            }
        }
        return cnt;
    }


    // ----------------------------------------------------------
    // 2. Math Trick
    // Count consecutive blocks of 1s
    // For block of length k → contributes k*(k+1)/2 substrings
    // Time: O(n)
    // ----------------------------------------------------------
    long long math_trick(const string& s) {
        long long ans = 0, count = 0;

        for (char c : s) {
            if (c == '1') {
                count++;
            } else {
                ans += (count * (count + 1)) / 2;
                count = 0;
            }
        }

        // last block
        ans += (count * (count + 1)) / 2;

        return ans;
    }


    // ----------------------------------------------------------
    // 3. DP Approach
    // dp[i] = number of consecutive 1s ending at i-1
    // Time: O(n) | Space: O(n)
    // ----------------------------------------------------------
    long long dp(const string& s) {
        int n = s.size();
        vector<long long> dp(n + 1, 0);

        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                dp[i + 1] = dp[i] + 1;
            } else {
                dp[i + 1] = 0;
            }
        }

        long long total = 0;
        for (long long x : dp) total += x;

        return total;
    }
};
