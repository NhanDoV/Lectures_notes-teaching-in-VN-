class isPalindrome:
    # Approach 1: 
    # Time complexity: O(n)     -   Space complexity: O(n)
    def pointwise_symmetric(self, s: str) -> bool:
        # Step 1: filter alphanumeric and lowercase
        filtered_text = []
        for char in s:
            if char.isalnum():                              # if include digits & alphabet
                filtered_text.append(char.lower())

        # Step 2: check symmetry
        n = len(filtered_text)
        for i in range(n // 2):
            if filtered_text[i] != filtered_text[n - i - 1]:
                return False
        return True

    # Approach 2: compare if its reversed string equal itself
    # Time complexity: O(n)     -   Space complexity: O(n)
    def reverse_string(self, s: str) -> bool:
        text = s.lower()
        alnum_str = ""
        for char in text:
            if char.isalnum():
                alnum_str += char
        return alnum_str == alnum_str[::-1]
    
    # Approach 3: 2 pointers
    # Time complexity: O(n)     -   Space complexity: O(1)
    def use_2pointers(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))