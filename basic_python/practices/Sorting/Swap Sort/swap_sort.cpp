#include <iostream>
#include <vector>
#include <iomanip>
#include <chrono>

using namespace std;

/*
    Swap Sort (O(n^2))
    Compare every pair (i, j) with j > i and swap if out of order
*/
vector<double> using_swap(vector<double> arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (arr[i] > arr[j]) {
                swap(arr[i], arr[j]);
            }
        }
    }
    return arr;
}

int main() {
    int n;
    cout << "input length of your array: ";
    cin >> n;

    vector<double> arr(n);
    for (int i = 0; i < n; ++i) {
        cout << "\t element " << i + 1 << ": ";
        cin >> arr[i];
    }

    cout << "\nYour input:\n";
    for (double x : arr) cout << x << " ";
    cout << "\n";

    cout << "Swap-Sort results:\n";

    // Start timer
    auto t0 = chrono::high_resolution_clock::now();

    vector<double> res = using_swap(arr);

    // End timer
    auto t1 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = t1 - t0;

    for (double x : res) cout << x << " ";
    cout << "\n";

    cout << fixed << setprecision(6);
    cout << "Elapsed time: " << elapsed.count() << " seconds\n";

    return 0;
}