#include <iostream>
using namespace std;

// Function to calculate the nth Fibonacci number using iteration
long long fibonacci(int n) {
    long long a = 0, b = 1, next;    
    if (n == 0) return a;
    if (n == 1) return b;    
    for (int i = 2; i <= n; i++) {
        next = a + b;
        a = b;
        b = next;
    }    
    return b;
}

int main() {
    int n;    
    cout << "Enter the position (n) in the Fibonacci sequence: ";
    cin >> n;    
    cout << "Fibonacci number at position " << n << " is: " << fibonacci(n) << endl;    
    return 0;
}