#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            std::unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[row][i] == '.') continue;
                if (seen.count(board[row][i])) return false;
                seen.insert(board[row][i]);
            }
        }

        for (int col = 0; col < 9; col++) {
            std::unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[i][col] == '.') continue;
                if (seen.count(board[i][col])) return false;
                seen.insert(board[i][col]);
            }
        }

        for (int square = 0; square < 9; square++) {
            std::unordered_set<char> seen;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }

        return true;
    }
};


int main() {
    Solution sol;
    std::vector<std::vector<char>> board(9, std::vector<char>(9));

    std::cout << "Enter Sudoku board row by row (9 characters per row, digits or '.'): \n";
    for (int i = 0; i < 9; ++i) {
        std::string row;
        std::cin >> row;
        for (int j = 0; j < 9; ++j) {
            board[i][j] = row[j];
        }
    }

    bool valid = sol.isValidSudoku(board);
    std::cout << (valid ? "The board is valid." : "The board is invalid.") << "\n";

    return 0;
}