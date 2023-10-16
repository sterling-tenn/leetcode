class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
    
    bool solve(vector<vector<char>>& board){
        for (int row = 0; row < board[0].size(); row++){
            for (int col = 0; col < board.size(); col++){
                if(board[row][col] == '.'){ // If empty space to fill in
                    for(char c = '1'; c<='9'; c++){
                        if (isValidLocation(board, row, col, c)){
                            board[row][col] = c;
                            if(solve(board)){ return true; } // Recursive call - keep trying to solve the next tile
                            else{ board[row][col] = '.'; } // If subsequent recursive calls ever return false (not valid board), then reset the value here and continue the loop
                        }
                    }
                    return false; // No more numbers to try
                }
            }
        }
        return true;
    }
    
    // Check if the board is in a valid state before inserting a number at location row/col
    // Checks to see if there already exists a the number we want to insert in a row, col, or 3x3 subsquare
    bool isValidLocation(vector<vector<char>>& board, int row, int col, char c){
        for(int i = 0; i < 9; i++){ if(board[row][i] == c) return false; } // Check row
        for(int i = 0; i < 9; i++){ if(board[i][col] == c) return false; } // Check columns
        
        // Check 3x3 subsquare
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                // Dividing by 3 truncates the value - essentially converts 9x9 coordinate to 3x3 coordinates
                // Multiplying by 3 converts back to 9x9 coordinates, except now it's origin point is the top left of the 3x3 square because of the truncation
                if(board[(row/3)*3 + i][(col/3)*3 + j] == c) return false;
            }
        }
        
        return true;
    }
};