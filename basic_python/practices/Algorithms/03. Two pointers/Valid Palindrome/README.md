## Description
### Problem

Given a string s, return true if it is a `palindrome`, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

### Example
#### EX1.
```python
Input: s = "Was it a car or a cat I saw?"

Output: true
```

**Explaination.** After considering only alphanumerical characters we have `"wasitacaroracatisaw"`, which is a palindrome.

#### EX2.
```python
Input: s = "tab a cat"

Output: false
```

**Explaination.** `"tabacat"` is not a palindrome.