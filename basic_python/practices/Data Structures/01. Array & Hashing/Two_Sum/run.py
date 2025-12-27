import random
from two_sum import twoSum

def parse_list(s: str):
    """Parse a comma-separated string into a list of ints."""
    return [int(x.strip()) for x in s.split(",") if x.strip()]

def parse_indices(s: str):
    """Parse expected indices like '0,1' into a list of ints."""
    return [int(x.strip()) for x in s.split(",") if x.strip()]

def load_test_cases(path: str):
    """Load test cases from file using ';' separator."""
    with open(path, "r") as f:
        lines = f.read().strip().split("\n")

    cases = []
    for line in lines:
        if line.strip() == "":
            continue
        # Split by semicolon
        parts = [p.strip() for p in line.split(";")]
        if len(parts) != 3:
            raise ValueError(f"Invalid test case format: {line}")
        
        nums_str, target_str, expected_str = parts
        nums = parse_list(nums_str)
        target = int(target_str)
        expected = parse_indices(expected_str)
        cases.append((nums, target, expected))
    return cases


def run_tests():
    print("=================== PROBLEM STATEMENT ========================")
    print("Given an array of integers 'nums' and an integer 'target',")
    print("return indices of the two numbers such that they add up to target.")
    print("You may assume that each input would have exactly one solution.")
    print("Example: nums = [2,7,11,15], target = 9  -->  output: [0,1]\n")

    print("""
            Available approaches to solve this problem:
            
            1. BRUTE FORCE
               - Time Complexity: O(n²)
               - Space Complexity: O(1)
            
            2. SORTING + TWO POINTERS
               - Time Complexity: O(n log n)
               - Space Complexity: O(n)
            
            3. HASHMAP ONE PASS
               - Time Complexity: O(n)
               - Space Complexity: O(n)
            
            4. HASHMAP TWO PASS
               - Time Complexity: O(n)
               - Space Complexity: O(n)
          """)

    choice = input("Please select one of the approaches (1 / 2 / 3 / 4): ").strip()
    solver = twoSum()

    # Map the choice to the correct method
    method_map = {
        "1": solver.brute_force,
        "2": solver.sorting,
        "3": solver.hashmap_one_pass,
        "4": solver.hashmap_two_pass,
    }

    if choice not in method_map:
        print("⚠️ Invalid choice! Defaulting to BRUTE FORCE (1).")
        method = solver.brute_force
    else:
        method = method_map[choice]

    # Load test cases
    test_cases = load_test_cases("tests/test_cases.txt")
    failed = []

    # Run tests
    for nums, target, expected in test_cases:
        try:
            result = method(nums.copy(), target)  # Copy for safety (sorting modifies list)
            if result != expected:
                failed.append((nums, target, expected, result))
        except Exception as e:
            failed.append((nums, target, expected, f"Error: {e}"))

    print("\n=================== TEST RESULTS ========================")
    if not failed:
        print("Congratulation, all test cases passed!")
    else:
        random_fail = random.choice(failed)
        nums, target, expected, result = random_fail
        print("Failed; look at this test-case:")
        print(f"Input: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()