class checkInclusion:
    """
        Return true if s2 contains a permutation of s1, or false otherwise. 
        That means if a permutation of s1 exists as a substring of s2, then return true.
        Example:
            *-------------*-----------*---------------------*
            |    Input    |  Output   |     Explanation     |
            |-------------|-----------|---------------------|
            | s1: adc     |    True   |         cda         |
            | s2: dcda    |           |    is one of perm   |
            |-------------|-----------|---------------------|
            | s1: abc     |    True   |         cba         |
            | s2: lecabee |           |    is one of perm   |
            *-------------------------*---------------------*
    """
    def brute_force(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        wd_sz = len(s1)

        for i in range(len(s2)):
            for j in range(i + wd_sz - 1, len(s2)):
                subStr = s2[i : j + 1]
                if sorted(subStr) == s1:
                    return True
        return False

    def using_hashtable(self, s1: str, s2: str) -> bool:
        # 1. Build a frequency map for all characters in s1
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        # 2. number of unique characters in s1 whose counts must match.
        need = len(count1)

        # 3. Loop
        for i in range(len(s2)):
            
            # Generate an  empty map `count2` & match counter `cur`
            count2, cur = {}, 0

            # Extend the substring by moving j
            for j in range(i, len(s2)):
                
                # Increment the frequency of s2[j]
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                # If count2[s2[j]] exceeds what count1 requires
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                
                # If the count for this character now matches count1, increase cur
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                
                # If cur == need, return True — we found a valid permutation
                if cur == need:
                    return True
        return False        

    def using_sliding_wd(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, that meant s1 can not be its substring
        if len(s1) > len(s2):
            return False

        # Build character frequency arrays
        s1Count, s2Count = [0] * 26, [0] * 26       # empty array of 26 characters alphabet
        for i in range(len(s1)):                    # loop & count 
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many positions match between the two arrays 
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Slide the window from left to right across
        l = 0                                           # left-index is 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add the new right character and update counts/matches.            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the left character and update counts/matches
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26

# ============================ RUN =====================================
if __name__ == "__main__":
    sol = checkInclusion()
    # 1️. Print class description
    print(sol.__doc__)

    # 2️. Input string
    s1 = input("Input your s1 string: ").strip()
    s2 = input("Input your s2 string: ").strip()

    # 3️. Choose method
    methods = {
        "1": ("Brute Force", sol.brute_force),
        "2": ("Hash Table", sol.using_hashtable),
        "3": ("Sliding Window", sol.using_sliding_wd),
    }

    print("\nChoose method:")
    for k, v in methods.items():
        print(f"{k}. {v[0]}")

    choice = input("Your choice (1-3): ").strip()

    # 4️. Execute
    if choice in methods:
        name, func = methods[choice]
        ans = func(s1, s2)
        print(f"\nMethod: {name}")
        print(f"Result: {ans}")
    else:
        print("Invalid choice")