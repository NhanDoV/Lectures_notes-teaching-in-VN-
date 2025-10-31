import random
from fibonacci import Fibonacci

def load_test_cases(path: str):
    with open(path, "r") as f:
        lines = f.read().strip().split("\n")
    cases = []
    for line in lines:
        if line.strip() == "":
            continue
        x_str, y_str = line.strip().split()
        cases.append((int(x_str), int(y_str)))
    return cases


def run_tests():
    print("=================== PROBLEM STATEMENT ========================")
    print("A standard Fibonacci sequence is one where each element "
          "is the sum of the two preceding elements, starting from 0 and 1.")
    print("     0    1    1    2    3    5    8    13    21    ...")    
    print("""
            Now, we have 3 approaches to solve this problem:
            
            1. RECURSIVE APPROACH:          Time Complexity: O(2^n)      Space Complexity: O(n)
            
            2. BASIC DYNAMIC PROGRAMMING:   Time Complexity: O(n)        Space Complexity: O(n)
            
            3. NO MEMO DYNAMIC PROGRAMMING: Time Complexity: O(n)        Space Complexity: O(1)
          """)

    # ========== USER SELECT METHOD ==========
    choice = input("Please select one of the approaches (1 / 2 / 3): ").strip()
    fib = Fibonacci()

    # map number to corresponding method
    method_map = {
        "1": fib.recursive_approach,
        "2": fib.dynamic_programming,
        "3": fib.DP_no_memo
    }

    if choice not in method_map:
        print("⚠️ Invalid choice! Defaulting to RECURSIVE approach (1).")
        method = fib.recursive_approach
    else:
        method = method_map[choice]

    # ========== LOAD TEST CASES ==========
    test_cases = load_test_cases("tests/test_cases.txt")
    failed = []

    # ========== RUN TESTS ==========
    for n, expected in test_cases:
        try:
            result = method(n)
            if result != expected:
                failed.append((n, expected, result))
        except Exception as e:
            failed.append((n, expected, f"Error: {e}"))

    # ========== PRINT RESULTS ==========
    print("\n=================== TEST RESULTS ========================")
    if not failed:
        print("Congratulation, all test cases passed!")
    else:
        random_fail = random.choice(failed)
        n, expected, result = random_fail
        print("Failed; look at this test-case:")
        print(f"Input: n = {n}, Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()