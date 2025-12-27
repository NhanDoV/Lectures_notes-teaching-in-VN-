#include <iostream>
#include <string>
#include <cctype>
using namespace std;

class isPalindrome {
public:
    // Approach 1:
    // Time complexity: O(n) - Space complexity: O(n)
    bool reverse_string(const string& s) {
        string alnum_str;
        for (char c : s) {
            if (isalnum(c)) {
                alnum_str += tolower(c);
            }
        }
        string reversed(alnum_str.rbegin(), alnum_str.rend());
        return alnum_str == reversed;
    }

    // Approach 2: 2 pointers
    // Time complexity: O(n) - Space complexity: O(1)
    bool use_2pointers(const string& s) {
        int l = 0, r = s.length() - 1;

        while (l < r) {
            while (l < r && !alphaNum(s[l])) l++;
            while (r > l && !alphaNum(s[r])) r--;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
        }
        return true;
    }

private:
    bool alphaNum(char c) {
        return ( (c >= 'A' && c <= 'Z') || 
                 (c >= 'a' && c <= 'z') || 
                 (c >= '0' && c <= '9') );
    }
};

int main() {
    isPalindrome checker;
    std::string input;

    // Input your string, 
    std::cout << "Enter a string to check palindrome: ";
    std::getline(std::cin, input);

    // Using the two pointers approach
    bool result = checker.use_2pointers(input);

    std::cout << "Is palindrome? " << std::boolalpha << result << "\n";

    return 0;
}