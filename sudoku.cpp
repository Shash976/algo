#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

bool is_move_valid(vector<vector<int>>&sudoku, int row, int col, int num){
    for (int column=0; column<9; column++){
        if (sudoku[row][column]==num) {
            return false;
        }
    }
    for (int row_number=0; row_number<9; row_number++){
        if (sudoku[row_number][col] == num) {
            return false;
        }
    }
    int start_row = 3*floor(row/3);
    int start_col = 3*floor(col/3);
    for (int row_number=start_row; row_number<start_row+3; row_number++){
        for (int column=start_col; column<start_col+3; column++) {
            if (sudoku[row_number][column]==num){
                return false;
            }
        }
    }
    return true;
}

bool solveSudoku(vector<vector<int>>& board) {
    for (int row = 0; row < 9; ++row) {
        for (int col = 0; col < 9; ++col) {
            // If the cell is empty
            if (board[row][col] == 0) {
                // Try filling the cell with numbers from 1 to 9
                for (int num = 1; num <= 9; ++num) {
                    if (is_move_valid(board, row, col, num)) {
                        board[row][col] = num;
                        // Recur with the updated board
                        if (solveSudoku(board)) {
                            return true;
                        }
                        // If the recursion does not lead to a solution, backtrack
                        board[row][col] = 0;
                    }
                }
                // If no number is valid, return to the previous recursive call and backtrack
                return false;
            }
        }
    }
    // If all cells are filled, the puzzle is solved
    return true;
}
int main() {
    vector<vector<int>> board =
                       {
                        {4,6,0,0,3,0,0,1,9},
                        {8,9,0,1,0,2,0,3,4},
                        {0,3,0,0,0,0,6,8,0},
                        {1,7,0,0,4,0,0,2,0},
                        {9,4,0,7,2,0,0,0,1},
                        {0,5,2,0,9,1,0,0,0},
                        {0,0,0,0,1,0,0,0,8},
                        {5,0,0,6,0,7,0,4,0},
                        {0,0,0,2,5,0,1,9,7}
                        };
    if (solveSudoku(board)) {
        // Print the solved puzzle
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution exists." << endl;
    }
    return 0;
    
}
