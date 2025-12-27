#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>
using namespace std;

class ValidParentheses {
public:

    // ---------------------------------------------------------
    // Approach 1: Repeated string erasing
    // ---------------------------------------------------------
    bool brute_force(string s) {
        while (true) {
            size_t pos = string::npos;

            if ((pos = s.find("()")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            if ((pos = s.find("{}")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            if ((pos = s.find("[]")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }

            break;
        }
        return s.empty();
    }


    // ---------------------------------------------------------
    // Approach 2: Stack-based validation (optimal)
    // ---------------------------------------------------------
    bool stack_method(const string& s) {
        stack<char> st;
        unordered_map<char, char> closeToOpen = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c : s) {
            if (closeToOpen.count(c)) {
                if (!st.empty() && st.top() == closeToOpen[c]) {
                    st.pop();
                } else {
                    return false;
                }
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};

int main() {
    ValidParentheses checker;
    std::string input;

    // Input your string, e.g. "A man, a plan, a canal: Panama";
    std::cout << "Enter a string to check ValidParentheses: ";
    std::getline(std::cin, input);

    // brute force
    bool result_1 = checker.brute_force(input);

    // stack method
    bool result_2 = checker.stack_method(input);
    
    std::cout << "Is valid Parentheses? (by brute force) " << std::boolalpha << result_1 << "\n";
    std::cout << "Is valid Parentheses? (using stack) " << std::boolalpha << result_2 << "\n";
    
    return 0;
}