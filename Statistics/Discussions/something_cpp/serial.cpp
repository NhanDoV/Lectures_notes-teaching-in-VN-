#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <queue>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

// Geometry-related functions
double computeAreaCircle(double radius);
double computeAreaTriangle(double a, double b, double c);
void findCenter(double xa, double ya, double xb, double yb);
void findIncenter(double xa, double ya, double xb, double yb, double xc, double yc);

// Volume-related functions (new additions)
double computeVolumeSphere(double radius);
double computeVolumeCone(double radius, double height);
double computeVolumeCube(double side);

// Fibonacci-related functions
long long fibonacci(int n);
long long fiboByGoldenRatio(int a, int b, int n);

// Number-related functions
bool checkSmithNumber(int n);
bool isPrime(int x);

// Utility functions
void rearrangeArray(int n);
int gcd(int a, int b);
long long lcm(long long a, long long b);
int smallestMultipleOf9(int n);

// Matrix-related functions
void matrixAddition();
void matrixMultiplication();
void matrixTranspose();
void matrixDeterminant();
void matrixInverse();

// User functions for the menu
void circle();
void triangle();
void midpoint();
void incenter();
void fibonacciSequence();
void generalizedFibonacci();
void smithNumber();
void primeCheck();
void rearrange();
void gcdCalculation();
void lcmCalculation();
void smallestMultipleOf9Calculation();
void matrixAdd();
void matrixMul();
void matrixTrans();
void matrixDet();
void matrixInv();

// New User functions for Volume-related menu options
void sphereVolume();
void coneVolume();
void cubeVolume();

int main() {
    cout << "Choose a function:\n";
    cout << " 1. Compute Area of a Circle\n";
    cout << " 2. Compute Area of a Triangle\n";
    cout << " 3. Find the Midpoint of Two Points\n";
    cout << " 4. Find the Incenter of a Triangle\n";
    cout << " 5. Fibonacci Sequence\n";
    cout << " 6. Generalized Fibonacci using Golden Ratio\n";
    cout << " 7. Check if a Number is a Smith Number\n";
    cout << " 8. Check if a Number is Prime\n";
    cout << " 9. Rearrange Array\n";
    cout << " 10. Compute GCD of Two Numbers\n";
    cout << " 11. Compute LCM of Two Numbers\n";
    cout << " 12. Find the Smallest Multiple of 9\n";
    cout << " 13. Matrix Addition\n";
    cout << " 14. Matrix Multiplication\n";
    cout << " 15. Matrix Transpose\n";
    cout << " 16. Matrix Determinant\n";
    cout << " 17. Matrix Inverse\n";
    cout << " 18. Compute Volume of a Sphere\n";  // New menu option
    cout << " 19. Compute Volume of a Cone\n";    // New menu option
    cout << " 20. Compute Volume of a Cube\n";    // New menu option
    cout << "Enter your choice: ";

    int choice;
    cin >> choice;

    switch (choice) {
        case 1: circle(); break;
        case 2: triangle(); break;
        case 3: midpoint(); break;
        case 4: incenter(); break;
        case 5: fibonacciSequence(); break;
        case 6: generalizedFibonacci(); break;
        case 7: smithNumber(); break;
        case 8: primeCheck(); break;
        case 9: rearrange(); break;
        case 10: gcdCalculation(); break;
        case 11: lcmCalculation(); break;
        case 12: smallestMultipleOf9Calculation(); break;
        case 13: matrixAdd(); break;
        case 14: matrixMul(); break;
        case 15: matrixTrans(); break;
        case 16: matrixDet(); break;
        case 17: matrixInv(); break;
        case 18: sphereVolume(); break;         // New case for sphere volume
        case 19: coneVolume(); break;           // New case for cone volume
        case 20: cubeVolume(); break;           // New case for cube volume
        default: cout << "Invalid choice!" << endl;
    }

    return 0;
}

// Generate squared-sequences
void generateSquaredSequence(int n, int base) {
    /*
        Generate and print a sequence of numbers in the form of:
            base^2  (base + 1)^2    (base + 2)^2   ...
    */
    cout << "Sequence: ";
    for (int i = 1; i <= n; ++i) {
        cout << pow(base + i, 2) << " "; // base^i
    }
    cout << endl;
}
int countPrimes(int n) {
    /*
    Function to count the number of prime numbers less than a given number 'n'.
    
    The function uses the Sieve of Eratosthenes algorithm to efficiently find all prime numbers less than 'n'.
    It initializes an array of booleans where each index represents a number, and the value at that index
    indicates whether the number is prime. The function then iterates over numbers, marking multiples of each 
    prime as non-prime. Finally, it counts the number of `true` values in the array, which represent primes.
    
    Parameters:
    - n: An integer representing the upper limit (exclusive) up to which we want to count primes.
    
    Returns:
    - An integer representing the count of prime numbers less than `n`.
    
    Example:
    - Input: 20
    - Output: 8 (The primes less than 20 are 2, 3, 5, 7, 11, 13, 17, 19)
    
    Time Complexity:
    - O(n log log n), which is the time complexity of the Sieve of Eratosthenes.
    */
    
    if (n <= 2) return 0; // There are no primes less than 2
    
    // Create a boolean array to mark primes (true means prime)
    vector<bool> isPrime(n, true);
    isPrime[0] = isPrime[1] = false; // 0 and 1 are not primes
    
    // Sieve of Eratosthenes
    for (int i = 2; i * i < n; ++i) {
        if (isPrime[i]) {
            // Mark all multiples of i as non-prime
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    // Count the primes
    int primeCount = 0;
    for (int i = 2; i < n; ++i) {
        if (isPrime[i]) {
            primeCount++;
        }
    }
    
    return primeCount;
}

void generateCubedSequence(int n, int base) {
    /*
        Generate and print a sequence of numbers in the form of:
            base^3  (base + 1)^3    (base + 2)^3   ...
    */
    cout << "Sequence: ";
    for (int i = 1; i <= n; ++i) {
        cout << pow(base + i, 3) << " "; // base^i
    }
    cout << endl;
}

// Geometry-related functions
double computeAreaCircle(double radius) {
    /*
        Find the are of a circle knowing that the radius.value
        S = pi * radius^2        
    */
    return M_PI * radius * radius;
}

double computeAreaTriangle(double a, double b, double c) {
    /*
        Find the are of a triangle knowing that the length of 3 edges a, b, c
          S = p*(p-a)*(p-b)*(p-c)
        where p is the semi-perimeter of a triangle
    */    
    // First of all, check the triangle-inequalities
    if (a + b > c && a + c > b && b + c > a) {
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    } else {
        cout << "Invalid triangle sides!" << endl;
        return -1;
    }
}

// Geometry-related functions
double computeAreaCircle(double radius) {
    /*
        Find the area of a circle knowing that the radius.value
        S = pi * radius^2        
    */
    return M_PI * radius * radius;
}

// Volume of a Sphere
double computeVolumeSphere(double radius) {
    /*
        Calculate the volume of a sphere using the formula:
        V = (4/3) * pi * radius^3
    */
    return (4.0 / 3.0) * M_PI * pow(radius, 3);
}

// Volume of a Cone
double computeVolumeCone(double radius, double height) {
    /*
        Calculate the volume of a cone using the formula:
        V = (1/3) * pi * radius^2 * height
    */
    return (1.0 / 3.0) * M_PI * pow(radius, 2) * height;
}

// Volume of a Cube
double computeVolumeCube(double side) {
    /*
        Calculate the volume of a cube using the formula:
        V = side^3
    */
    return pow(side, 3);
}

// User-facing functions to call the volume-related functions
// Function for computing the volume of a sphere
void sphereVolume() {
    double radius;
    cout << "Enter the radius of the sphere: ";
    cin >> radius;
    double volume = computeVolumeSphere(radius);
    cout << "Volume of the sphere: " << volume << endl;
}

// Function for computing the volume of a cone
void coneVolume() {
    double radius, height;
    cout << "Enter the radius of the cone: ";
    cin >> radius;
    cout << "Enter the height of the cone: ";
    cin >> height;
    double volume = computeVolumeCone(radius, height);
    cout << "Volume of the cone: " << volume << endl;
}

// Function for computing the volume of a cube
void cubeVolume() {
    double side;
    cout << "Enter the side length of the cube: ";
    cin >> side;
    double volume = computeVolumeCube(side);
    cout << "Volume of the cube: " << volume << endl;
}

void findCenter(double xa, double ya, double xb, double yb) {
    /*
        Find the coordinate of the mid-point between 2 any given points A(xa, ya) and B(xb, yb)
    */
    double xm = (xa + xb) / 2.0;
    double ym = (ya + yb) / 2.0;
    cout << "Midpoint: (" << xm << ", " << ym << ")" << endl;
}

void findIncenter(double xa, double ya, double xb, double yb, double xc, double yc) {
    /*
      Find the center of a triangle while knowing the coordinates of 3 points
    */
    double a = sqrt(pow(xb - xc, 2) + pow(yb - yc, 2));
    double b = sqrt(pow(xa - xc, 2) + pow(ya - yc, 2));
    double c = sqrt(pow(xa - xb, 2) + pow(ya - yb, 2));

    double x_incenter = (a * xa + b * xb + c * xc) / (a + b + c);
    double y_incenter = (a * ya + b * yb + c * yc) / (a + b + c);

    cout << "Incenter: (" << x_incenter << ", " << y_incenter << ")" << endl;
}

// Fibonacci-related functions
long long fibonacci(int n) {
    /*
        Find the value of the given position n from a fibonacci-sequence
        Noting that this is the standard-Fibonacci with the frist 2 numbers is 1
        For eg,
          F(1) = 1
          F(2) = 1
          F(3) = 2
          F(4) = 3
          F(5) = 5
          F(6) = 8
        Generally, for all n > 2, we have
          F(n) = F(n-1) + F(n-2)
    */
    if (n <= 1) return n;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long next = a + b;
        a = b;
        b = next;
    }
    return b;
}

long long fiboByGoldenRatio(int a, int b, int n) {
    /*
      In this case, we will formulate the generalizedFibonacci using the golden-ratio
      where
        F(a, b, 0) = a
        F(a, b, 1) = b
        F(a, b, n) = F(a, b, n-1) + F(a, b, n-2)
    */
    const double phi = (1 + sqrt(5)) / 2;
    return static_cast<long long>((pow(phi, n + 1) - pow(1 - phi, n + 1)) / sqrt(5));
}

// Number-related functions
bool checkSmithNumber(int n) {
    /*
      Smith number is the number a composite number whose sum of digits is equal to the sum of digits of its prime factorization
      For example:
        648 = 2^3 * 3^4 = 6+4+8 = 2+2+2+3+3+3+3
      Also, this function will help you check if any given number is Smith-number
    */
    auto sumDigits = [](int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    };

    int sumOfInput = sumDigits(n);
    vector<int> primeFactors;
    int temp = n;

    for (int i = 2; i <= temp / 2; ++i) {
        while (temp % i == 0) {
            primeFactors.push_back(i);
            temp /= i;
        }
    }
    if (temp > 1) primeFactors.push_back(temp);

    int sumOfPrimeDigits = 0;
    for (int factor : primeFactors) {
        sumOfPrimeDigits += sumDigits(factor);
    }

    return sumOfInput == sumOfPrimeDigits;
}

bool isPrime(int x) {
    /*
      A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 
      A natural number greater than 1 that is not prime is called a composite number.
      In this function we will check whether a given number is prime-number
    */
    if (x <= 1) return false;
    for (int i = 2; i <= sqrt(x); i++) {
        if (x % i == 0) return false;
    }
    return true;
}

// Utility functions
void rearrangeArray(int n) {
    /*
      This function will reverse any given value from an array.
      You will input the length (number of elements) from an array, denoted by n
      For example,
        n = 5
        arr = 1  -2  4  3   0
        output = 0  3  4  -2  1
    */
    vector<int> arr(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Rearranging the array (move last element to front)
    if (n > 1) {
        int last = arr[n - 1];
        for (int i = n - 1; i > 0; --i) {
            arr[i] = arr[i - 1];
        }
        arr[0] = last;
    }

    // Print rearranged array
    cout << "Rearranged array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int gcd(int a, int b) {
    /*
      find the gcd (greatest common divisor) of any 2 intergers
      Examples
        - gcd(2, 3) = 1
        - gcd(25, 15) = 5
    */
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long lcm(long long a, long long b) {
    /*
      find the lcm (lowest common multipler) of any 2 intergers
      Examples:
        - lcm(2, 3) = 6
        - lcm(24, 12) = 24
        - lcm(24, 18) = 72
    */  
    return (a * b) / gcd(a, b);
}

int smallestMultipleOf9(int n) {
    /*
      find the smallest number such that
        - only contains 2 digits 0 and 9
        - multipler of 9        -
      Examples
        >> smallest_mutilple_of_9(1)  =    9
        >> smallest_mutilple_of_9(2)  =   90
        >> smallest_mutilple_of_9(7)  =  9009
        >> smallest_mutilple_of_9(8)  =  9000
        >> smallest_mutilple_of_9(23) = 990909
        >> smallest_mutilple_of_9(31) = 999099
    */  
    if (n % 9 == 0) return 9;

    queue<string> q;
    unordered_set<int> visited;
    q.push("9");

    while (!q.empty()) {
        string curr = q.front();
        q.pop();
        int num = stoi(curr);
        if (num % n == 0) return num;

        int remainder = num % n;
        if (visited.find(remainder) == visited.end()) {
            visited.insert(remainder);
            q.push(curr + "0");
            q.push(curr + "9");
        }
    }
    return -1; // Should not reach here
}

// Matrix-related functions
void matrixAddition() {
    /*
      Addition of two matrices A and B.
      
      Example:
      For example, if matrix A is:
      
      A = 1  2
          3  4
          
      and matrix B is:
      
      B = 5  6
          7  8
          
      Then the result of matrix addition (A + B) would be:
      
      Result = (1+5)  (2+6)
              (3+7)  (4+8)
      
            = 6  8
              10  12
    */
    
    int r, c;
    cout << "Enter number of rows and columns: ";
    cin >> r >> c;

    vector<vector<int>> A(r, vector<int>(c));
    vector<vector<int>> B(r, vector<int>(c));
    vector<vector<int>> result(r, vector<int>(c));

    cout << "Enter elements of matrix A: \n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> A[i][j];
        }
    }

    cout << "Enter elements of matrix B: \n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> B[i][j];
        }
    }

    // Matrix addition
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }

    // Display result
    cout << "Result of matrix addition: \n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
}

void matrixMultiplication() {
    /*
      Multiplication of two matrices A and B.
      
      Matrix multiplication is possible when the number of columns of the first matrix (A) 
      is equal to the number of rows of the second matrix (B).
      
      Example:
      For example, if matrix A is:
      
      A = 1  2
          3  4
          
      and matrix B is:
      
      B = 5  6
          7  8
          
      Then the result of matrix multiplication (A * B) would be:

      Result = (1*5 + 2*7)  (1*6 + 2*8)
              (3*5 + 4*7)  (3*6 + 4*8)

            = 19  22
              43  50
    */
    
    int r1, c1, r2, c2;
    cout << "Enter number of rows and columns for Matrix A: ";
    cin >> r1 >> c1;
    cout << "Enter number of rows and columns for Matrix B: ";
    cin >> r2 >> c2;

    if (c1 != r2) {
        cout << "Matrix multiplication is not possible." << endl;
        return;
    }

    vector<vector<int>> A(r1, vector<int>(c1));
    vector<vector<int>> B(r2, vector<int>(c2));
    vector<vector<int>> result(r1, vector<int>(c2));

    cout << "Enter elements of matrix A: \n";
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            cin >> A[i][j];
        }
    }

    cout << "Enter elements of matrix B: \n";
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            cin >> B[i][j];
        }
    }

    // Matrix multiplication
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[i][j] = 0;  // Initialize the result matrix element
            for (int k = 0; k < c1; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Display result
    cout << "Result of matrix multiplication: \n";
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
}

void matrixTranspose() {
    /*
      Transpose of any given matrix.
      
      The transpose of a matrix is obtained by swapping rows and columns.
      
      Example:
      For a matrix A:
      
      A = 1  2  3
          4  5  6
          
      The transpose of A (denoted A^T) would be:
      
      A^T = 1  4
            2  5
            3  6
    */
    
    int r, c;
    cout << "Enter number of rows and columns: ";
    cin >> r >> c;

    vector<vector<int>> A(r, vector<int>(c));
    cout << "Enter elements of matrix: \n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> A[i][j];
        }
    }

    vector<vector<int>> result(c, vector<int>(r));

    // Matrix Transpose
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[j][i] = A[i][j];
        }
    }

    // Display result
    cout << "Transposed matrix: \n";
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
}

void matrixDeterminant() {
    /*
      Find the determinant of a given matrix.
      
      The determinant is a scalar value that can be computed from the elements 
      of a square matrix and encodes certain properties of the matrix.
      
      Example:
      For a 2x2 matrix:
      
      A = 1  2
          3  4
          
      The determinant of A is calculated as:
      
      det(A) = (1 * 4) - (2 * 3) = 4 - 6 = -2
    */
    
    int n;
    cout << "Enter the size of the matrix: ";
    cin >> n;

    vector<vector<int>> A(n, vector<int>(n));
    cout << "Enter elements of the matrix: \n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }

    // Calculate determinant using recursion (assuming a helper function 'determinant')
    int det = determinant(A, n);  // You need to define this function separately
    cout << "Determinant of the matrix is: " << det << endl;
}

void matrixInv() {
    /*
      Find the inverse of a matrix.
      
      The inverse of a matrix A is denoted as A^(-1), and is defined such that:
      A * A^(-1) = I, where I is the identity matrix.
      
      Example:
      For a 2x2 matrix A:
      
      A = 4  7
          2  6
          
      The inverse of A, A^(-1), is calculated as:
      
      A^(-1) = (1/det(A)) * adj(A),
      where adj(A) is the adjugate of A, and det(A) is the determinant.
      
      For this example, the determinant is:
      det(A) = (4 * 6) - (7 * 2) = 24 - 14 = 10.
      
      The inverse is then:
      A^(-1) = (1/10) *  [ 6  -7 ]
                          [-2   4 ]
      A^(-1) =  [ 0.6  -0.7 ]
                  [-0.2   0.4 ]
    */  
    int n;
    cout << "Enter the size of the matrix: ";
    cin >> n;

    vector<vector<int>> A(n, vector<int>(n));
    cout << "Enter elements of the matrix: \n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }

    vector<vector<int>> inv(n, vector<int>(n));
    // Calculate matrix inverse here (using Gauss-Jordan or other methods)
    if (inverseMatrix(A, inv)) {  // You need to define 'inverseMatrix' function
        cout << "Inverse matrix: \n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << inv[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "Matrix is singular, cannot find inverse.\n";
    }
}

// Helper function to calculate the determinant of a matrix recursively
int determinant(vector<vector<int>>& matrix, int n) {
    /*
      Calculates the determinant of a square matrix recursively.
      
      For a matrix of size 1x1, the determinant is simply the value of the only element.
      For a matrix of size 2x2, the determinant is calculated as:
      det(A) = a*d - b*c for the matrix:
        A = [a b]
            [c d]
      For larger matrices, the determinant is calculated using cofactor expansion along the first row.

      Example:
      For a 3x3 matrix:
      
      A = 1  2  3
          4  5  6
          7  8  9
          
      The determinant is computed as:
      det(A) = 1 * det([5 6; 8 9]) - 2 * det([4 6; 7 9]) + 3 * det([4 5; 7 8])
             = 1 * ((5*9) - (6*8)) - 2 * ((4*9) - (6*7)) + 3 * ((4*8) - (5*7))
             = 0 (in this case, det(A) = 0 as the rows are linearly dependent)
    */
    
    if (n == 1) return matrix[0][0];  // For 1x1 matrix, return the only element
    if (n == 2) return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];  // For 2x2 matrix, use the direct formula
    
    int det = 0;
    for (int i = 0; i < n; i++) {
        // Create a minor matrix by excluding the current row and column
        vector<vector<int>> minor(n - 1, vector<int>(n - 1));
        for (int j = 1; j < n; j++) {
            int colIndex = 0;
            for (int k = 0; k < n; k++) {
                if (k == i) continue;
                minor[j - 1][colIndex] = matrix[j][k];
                colIndex++;
            }
        }
        // Apply cofactor expansion and accumulate the result
        det += pow(-1, i) * matrix[0][i] * determinant(minor, n - 1);
    }
    return det;
}

// Helper function to calculate the inverse of a matrix using Gauss-Jordan elimination
bool inverseMatrix(vector<vector<int>>& matrix, vector<vector<int>>& inv) {
    /*
      Calculates the inverse of a matrix using Gauss-Jordan elimination.
      
      The inverse of a matrix A is a matrix B such that A * B = I, where I is the identity matrix.
      The Gauss-Jordan method involves augmenting the matrix A with the identity matrix I, and then
      performing row operations to reduce the matrix to its inverse.
      
      Example:
      For a 2x2 matrix A:
      
      A = [4 7]
          [2 6]
      
      The inverse matrix A^(-1) is:
      
      A^(-1) = 1/det(A) * adj(A), where adj(A) is the adjugate matrix of A.
      In this case, the determinant of A is:
      det(A) = (4 * 6) - (7 * 2) = 10.
      
      The inverse is then calculated and returned as:
      A^(-1) = 1/10 * [ 6  -7 ]
                          [-2   4 ]
      A^(-1) = [ 0.6  -0.7 ]
                  [-0.2   0.4 ]
    */
    
    int n = matrix.size();
    double det = determinant(matrix, n);  // Get the determinant

    // If determinant is 0, the matrix is singular, so it doesn't have an inverse
    if (det == 0) return false;

    // Augment matrix A with the identity matrix
    vector<vector<double>> augmented(n, vector<double>(2 * n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            augmented[i][j] = matrix[i][j];
            augmented[i][j + n] = (i == j) ? 1 : 0;  // Identity matrix
        }
    }

    // Apply Gauss-Jordan elimination
    for (int i = 0; i < n; i++) {
        // Find the row with the largest element in column i (pivoting)
        double maxEl = fabs(augmented[i][i]);
        int maxRow = i;
        for (int k = i + 1; k < n; k++) {
            if (fabs(augmented[k][i]) > maxEl) {
                maxEl = fabs(augmented[k][i]);
                maxRow = k;
            }
        }

        // If the pivot element is zero, the matrix is singular, no inverse exists
        if (augmented[maxRow][i] == 0) return false;
        
        // Swap the current row with the row having the maximum element
        swap(augmented[i], augmented[maxRow]);

        // Normalize the pivot row (make the pivot element 1)
        double div = augmented[i][i];
        for (int j = 0; j < 2 * n; j++) {
            augmented[i][j] /= div;
        }

        // Eliminate the current column from all other rows
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = augmented[k][i];
                for (int j = 0; j < 2 * n; j++) {
                    augmented[k][j] -= factor * augmented[i][j];
                }
            }
        }
    }

    // Copy the right side of the augmented matrix to the inverse matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            inv[i][j] = augmented[i][j + n];  // Right half is the inverse
        }
    }

    return true;
}