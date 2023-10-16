class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int row = 0; row < board.size(); row++){
            for(int col = 0; col < board[0].size(); col++){
                if(board[row][col] != '.'){
                    if(!isValidLocation(board, row, col, board[row][col])){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    
    bool isValidLocation(vector<vector<char>>& board, int row, int col, char c){
        int row_occ = 0, col_occ = 0, square_occ = 0; // Track number of occurences
        for(int i = 0; i < 9; i++){ if(board[row][i] == c) row_occ++; } // Check row
        for(int i = 0; i < 9; i++){ if(board[i][col] == c) col_occ++; } // Check columns
        
        // Check 3x3 subsquare
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                // Dividing by 3 truncates the value - essentially converts 9x9 coordinate to 3x3 coordinates
                // Multiplying by 3 converts back to 9x9 coordinates, except now it's origin point is the top left of the 3x3 square because of the truncation
                if(board[(row/3)*3 + i][(col/3)*3 + j] == c) square_occ++;
            }
        }
        return (row_occ == 1) && (col_occ == 1) && (square_occ == 1);
    }
};