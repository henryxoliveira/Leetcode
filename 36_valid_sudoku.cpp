#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        /**
         * Determine if a 9x9 Sudoku board is valid.
         * 
         * Approach:
         * 1. Use sets to track seen digits in rows, columns, and 3x3 sub-boxes
         * 2. For each filled cell, check if the digit has been seen in its row, column, or box
         * 3. If any duplicate is found, return false
         * 4. Only filled cells (digits 1-9) need validation; empty cells ('.') are ignored
         * 
         * Time Complexity: O(1) since the board is always 9x9 = 81 cells
         * Space Complexity: O(1) since we use fixed-size sets for 81 cells
         */
        
        // Initialize sets for rows, columns, and boxes
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char cell = board[i][j];
                
                // Skip empty cells
                if (cell == '.') {
                    continue;
                }
                
                // Check if digit already exists in current row
                if (rows[i].find(cell) != rows[i].end()) {
                    return false;
                }
                rows[i].insert(cell);
                
                // Check if digit already exists in current column
                if (cols[j].find(cell) != cols[j].end()) {
                    return false;
                }
                cols[j].insert(cell);
                
                // Calculate which 3x3 box the cell belongs to
                // Box index: (i/3) * 3 + (j/3)
                int boxIndex = (i / 3) * 3 + (j / 3);
                
                // Check if digit already exists in current box
                if (boxes[boxIndex].find(cell) != boxes[boxIndex].end()) {
                    return false;
                }
                boxes[boxIndex].insert(cell);
            }
        }
        
        return true;
    }
};


