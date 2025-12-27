#include <iostream>
#include <vector>
#include <string>

using namespace std;

class EncDecodeStrings {
public:
    string encode(const vector<string>& strs) {
        string res;
        for (const string& s : strs) {
            res += to_string(s.length()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(const string& s) {
        vector<string> res;
        int i = 0;
        int n = (int)s.length();

        while (i < n) {
            int j = i;
            while (j < n && s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            res.push_back(s.substr(i, length));
            i += length;
        }
        return res;
    }
};

int main() {
    int n_vocab;
    cout << "Number of words: \t";
    cin >> n_vocab;
    cin.ignore(); // clear newline

    vector<string> raw;
    for (int idx = 0; idx < n_vocab; idx++) {
        cout << "\t" << (idx + 1) << ": \t";
        string vocab;
        getline(cin, vocab);
        raw.push_back(vocab);
    }

    EncDecodeStrings solver;
    string encoded = solver.encode(raw);
    cout << "Encoded string: \t" << encoded << endl;

    vector<string> decoded = solver.decode(encoded);
    cout << "Decoded list: \t";
    for (const string& s : decoded) {
        cout << s << " | ";
    }
    cout << endl;

    // Bonus: verify decode == original
    bool match = (decoded == raw);
    cout << "Match original list? " << (match ? "Yes" : "No") << endl;

    return 0;
}