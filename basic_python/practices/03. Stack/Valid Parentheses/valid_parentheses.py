class isValid_Parentheses:
    """
        Notes:
                * Here we can not use any symmetric-check to validate since `(` is different from `)`
                * All the examples in this question only contains parentheses likes

                        [(()]           [{()}]          ({)         {[({})]}        (][])

                    invalid test-cases:
                        [(hello{})]         [({(/.)})]
    """

    # Approach 1.
    # Time Complexity: O(n^2)   -   Space complexity: O(n)
    def using_replacement_trick(self, s: str) -> bool:
        # replace if we met any term in the string contained the parentheses
        # When you use `if` instead of `while`, this only works once
        while ("[]" in s) or ("()" in s) or ("{}" in s):
            s = s.replace("[]", "")
            s = s.replace("()", "")
            s = s.replace("{}", "")
        # if the parentheses is valid in s; finally we will get empty string ""
        return s == ""
    
    # Approach 2.
    def using_stack(self, s: str) -> bool:
        my_stack = []
        # define the pairs of open+close
        parentheses_dict = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        for char in s:
            if char in parentheses_dict:
                if my_stack and my_stack[-1] == parentheses_dict[char]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(char)
        return True if not my_stack else False

    # Approach 3. counting
    def count_pairs(self, s: str) -> bool:
        cnt1, cnt2, cnt3 = 0, 0, 0
        for char in s:
            # For ()
            if char == "(":
                cnt1 += 1
            elif char == ")":
                cnt1 -= 1
                if cnt1 < 0:
                    return False
            # For []
            if char == "[":
                cnt2 += 1
            elif char == "]":
                cnt2 -= 1
                if cnt2 < 0:
                    return False
            # For {}
            if char == "{":
                cnt3 += 1
            elif char == "}":
                cnt3 -= 1
                if cnt3 < 0:
                    return False
                                
        return (cnt1 == 0) & (cnt2 == 0) & (cnt3 == 0)

    # Approach 4. using regex
    def using_regex(self, s: str) -> bool:
        import re
        patt = re.compile(r"\(\)|\[\]|\{\}")
        prev = None
        while prev != s:
            prev = s
            s = patt.sub("", s)
        return not s

    # Approach 5. using recursive
    def using_recursive(self, s: str) -> bool:
        if not s:
            return True
        for pair in ["()", "{}", "[]"]:
            if pair in s:
                return self.using_recursive(s.replace(pair, ""))
        return False