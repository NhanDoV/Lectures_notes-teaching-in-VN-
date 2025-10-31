class isValid_Parentheses:
    # Here we can not use any symmetric-check to validate since `(` is different from `)`

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
            "[": "]",
            "(": ")",
            "{": "}"
        }
        # for