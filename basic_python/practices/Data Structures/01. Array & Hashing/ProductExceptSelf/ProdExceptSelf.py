class productExceptSelf:
    def brute_force_1(self, nums: list[int]) -> list[int]:
        res = []
        n = len(nums)

        for idx in range(n):
            arr = [nums[_] if _ != idx else 1 for _ in range(n)]
            p = 1
            for elm in arr:
                p *= elm
            res.append(p)
        return res

    def brute_force_2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res

    def using_division(self, nums: list[int]) -> list[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c

        return res

    def using_presuffix_1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

    def using_presuffix_2(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

def print_menu():
    print("\nChoose a method:")
    print("1. Brute force 1")
    print("2. Brute force 2")
    print("3. Using division")
    print("4. Using prefix/suffix (method 1)")
    print("5. Using prefix/suffix (method 2)")
    print("0. Exit")


if __name__ == "__main__":
    print("=== Product Except Self Solver ===")
    print_menu()

    n = int(input("Input array length: "))
    nums = [int(input(f"  Element {i+1}: ")) for i in range(n)]

    print("\nYour input array:", nums)

    solver = productExceptSelf()

    choice = input("Select option: ")

    if choice == "1":
        result = solver.brute_force_1(nums)
    elif choice == "2":
        result = solver.brute_force_2(nums)
    elif choice == "3":
        result = solver.using_division(nums)
    elif choice == "4":
        result = solver.using_presuffix_1(nums)
    elif choice == "5":
        result = solver.using_presuffix_2(nums)
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid option. Try again.")
    print("Result:", result)