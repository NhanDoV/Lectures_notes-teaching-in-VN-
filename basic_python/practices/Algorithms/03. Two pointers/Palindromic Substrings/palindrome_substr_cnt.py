import time

class countSubstrings:

    def brute_force(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                left, right = i, j
                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1
                cnt += (left >= right)
        return cnt

    def using_2pointers_optimized(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand_around_center(left, right):
            cnt = 0

            # check if s[i] = s[n - i] for all i
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left) % 2 == 0:
                    print('word [odd] \t : \t', s[left: right + 1])
                else:
                    print('word [even] \t : \t', s[left: right + 1])
                cnt += 1
                left -= 1
                right += 1

            return cnt

        for i in range(n):
            # Odd length palindromes (e.g., 'aba', 'abcba')
            count += expand_around_center(i, i)

            # Even length palindromes (e.g., 'abba', 'aa')
            count += expand_around_center(i, i + 1)

        return count

    def using_2pointers(self, s: str) -> int:

        res = 0

        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

if __name__ == "__main__":

    # Initialize the class
    sol = countSubstrings()

    # ===============================
    # 1. Input
    # ===============================
    s = input("Input a string: \t")
    print("=" * 60)
    print(f"Input string: '{s}'")
    print("=" * 60)

    # ===============================
    # 2. Available methods
    # ===============================
    methods = {
        "1": ("Brute Force", sol.brute_force),
        "2": ("2 Pointers (optimized, verbose)", sol.using_2pointers_optimized),
        "3": ("2 Pointers (clean)", sol.using_2pointers),
    }

    print("\nAvailable methods:")
    for k, (name, _) in methods.items():
        print(f"  {k}. {name}")

    # ===============================
    # 3. Choose method
    # ===============================
    choice = input("\nChoose a method (1/2/3): ").strip()

    if choice not in methods:
        print("X Invalid choice!")
        exit(1)

    method_name, method_fn = methods[choice]
    print(f"\n [o] Running method: {method_name}")

    # ===============================
    # 4. Run + measure time
    # ===============================
    start_time = time.perf_counter()
    result = method_fn(s)
    end_time = time.perf_counter()

    # ===============================
    # 5. Output
    # ===============================
    print("\nResult:")
    print(f"Total palindromic substrings = {result}")
    print(f"Time elapsed: {(end_time - start_time) * 1000:.4f} ms")