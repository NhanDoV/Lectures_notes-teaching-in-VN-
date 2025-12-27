#include <iostream>
#include <vector>
using namespace std;

class ProductExceptSelf {
public:

    vector<int> brute_force_1(const vector<int>& nums) {
        int n = nums.size();
        vector<int> res;

        for (int idx = 0; idx < n; idx++) {
            vector<int> arr(n);
            for (int i = 0; i < n; i++)
                arr[i] = (i != idx) ? nums[i] : 1;

            int p = 1;
            for (int x : arr) p *= x;

            res.push_back(p);
        }
        return res;
    }

    vector<int> brute_force_2(const vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);

        for (int i = 0; i < n; i++) {
            int prod = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                prod *= nums[j];
            }
            res[i] = prod;
        }
        return res;
    }

    vector<int> using_division(const vector<int>& nums) {
        int prod = 1, zero_cnt = 0;

        for (int num : nums) {
            if (num != 0) prod *= num;
            else zero_cnt++;
        }

        int n = nums.size();
        vector<int> res(n);

        if (zero_cnt > 1)
            return vector<int>(n, 0);

        for (int i = 0; i < n; i++) {
            if (zero_cnt == 1) {
                res[i] = (nums[i] == 0 ? prod : 0);
            } else {
                res[i] = prod / nums[i];
            }
        }
        return res;
    }

    vector<int> using_presuffix_1(const vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n), pref(n), suff(n);

        pref[0] = 1;
        suff[n - 1] = 1;

        for (int i = 1; i < n; i++)
            pref[i] = nums[i - 1] * pref[i - 1];

        for (int i = n - 2; i >= 0; i--)
            suff[i] = nums[i + 1] * suff[i + 1];

        for (int i = 0; i < n; i++)
            res[i] = pref[i] * suff[i];

        return res;
    }

    vector<int> using_presuffix_2(const vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        int prefix = 1;
        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }

        return res;
    }
};


void print_menu() {
    cout << "\nChoose a method:\n";
    cout << "1. Brute force 1\n";
    cout << "2. Brute force 2\n";
    cout << "3. Using division\n";
    cout << "4. Using prefix/suffix (method 1)\n";
    cout << "5. Using prefix/suffix (method 2)\n";
    cout << "0. Exit\n";
}


int main() {
    cout << "=== Product Except Self Solver ===\n";
    print_menu();

    int n;
    cout << "Input array length: ";
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cout << "  Element " << i + 1 << ": ";
        cin >> nums[i];
    }

    cout << "\nYour input array: ";
    for (int x : nums) cout << x << " ";
    cout << "\n";

    ProductExceptSelf solver;

    cout << "Select option: ";
    int choice;
    cin >> choice;

    vector<int> result;

    switch (choice) {
        case 1: result = solver.brute_force_1(nums); break;
        case 2: result = solver.brute_force_2(nums); break;
        case 3: result = solver.using_division(nums); break;
        case 4: result = solver.using_presuffix_1(nums); break;
        case 5: result = solver.using_presuffix_2(nums); break;
        case 0: 
            cout << "Exiting...\n"; 
            return 0;
        default:
            cout << "Invalid option. Try again.\n";
            return 0;
    }

    cout << "Result: ";
    for (int x : result) cout << x << " ";
    cout << "\n";

    return 0;
}