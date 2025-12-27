class lengthOfLongestSubstring:
    """
        Find the length of the longest substring without duplicate characters.

        Example
            *-----------------------*---------------------*
            |   Input   |  Output   |     Explanation     |
            |-----------|-----------|---------------------|
            | zxyzxyz   |     3     |         xyz         |
            |   xxxx    |     1     |          x          |
            | abcabcbb  |     3     |      abc / bca      |
            *-----------------------*---------------------*
    """

    def brute_force(self, s: str) -> int:
        res = 0                             # Initialize `res` to store the maximum length.

        for i in range(len(s)):             # For each starting index from the input-string,
            charSet = set()                 # Create an empty set `charSet`

            for j in range(i, len(s)):      # Extend the substring by moving j; from i forward

                if s[j] in charSet:         # If s[j] is already in the set, break
                    break
                
                charSet.add(s[j])           # otherwise, add this to set
            res = max(res, len(charSet))
        
        return res

    def brute_force_with_window(self, s: str) -> int:
        n = len(s)                                  # get length of the input-string

        # if the input's length is less than one character
        if n <= 1:
            return n

        # Otherwise,
        max_len = 0
        for i in range(n):                          # for each starting index
            for wd_size in range(1, n - i + 1):     # for each window_size which counting from i
                word = s[i: i + wd_size]            # consider the substring from i which having length = window_size
                if len(set(word)) == wd_size:       # assign if all the character in the substring is unique
                    max_len = max(max_len, wd_size)
        return max_len

    def sliding_window_set(self, s: str) -> int:
        charSet = set()
        left = 0                                # left edge of the window
        res = 0                                 # initialize max_len = 0

        for right in range(len(s)):             # for each right edge that moves through the string
            while s[right] in charSet:          # until the s[right] already in the set
                charSet.remove(s[left])         # remove s[left]
                left += 1                       # move left'index --> right 
            charSet.add(s[right])               # add s[right] to the set
            temp_wd_size = right - left + 1
            res = max(res, temp_wd_size)        # update the new max_len by the current-val vs the new window-size 
        return res

    def sliding_window_hashmap(self, s: str) -> int:
        mp = {}                                     # Create a map mp to store the last index of each character.
        left = 0                                    # for the start of the window,
        res = 0

        for right in range(len(s)):                 # Loop through the string with right's index

            if s[right] in mp:                      # If s[r] is already in map
                left = max(mp[s[right]] + 1, left)  # move left'index to mp[s[r]] + 1, but never backward.

            mp[s[right]] = right                    # update character in map by the right's index

            res = max(res, right - left + 1)        # Update the longest length
        
        return res

# ============================ RUN =====================================
if __name__ == "__main__":
    sol = lengthOfLongestSubstring()
    # 1️. Print class description
    print(sol.__doc__)

    # 2️. Input string
    s = input("Input your string: ").strip()

    # 3️. Choose method
    methods = {
        "1": ("Brute Force", sol.brute_force),
        "2": ("Brute Force with Window", sol.brute_force_with_window),
        "3": ("Sliding Window (Set)", sol.sliding_window_set),
        "4": ("Sliding Window (HashMap)", sol.sliding_window_hashmap),
    }

    print("\nChoose method:")
    for k, v in methods.items():
        print(f"{k}. {v[0]}")

    choice = input("Your choice (1-4): ").strip()

    # 4️. Execute
    if choice in methods:
        name, func = methods[choice]
        ans = func(s)
        print(f"\nMethod: {name}")
        print(f"Result: {ans}")
    else:
        print("Invalid choice")