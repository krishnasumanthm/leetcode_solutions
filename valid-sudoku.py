class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def check_rows(self, board):
        for i in xrange(9):
            temp = set()
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in temp:
                    return False
                else:
                    temp.add(board[i][j])
        return True
    
    def check_cols(self, board):
        for i in xrange(9):
            temp = set()
            for j in xrange(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in temp:
                    return False
                else:
                    temp.add(board[j][i])
        return True
     
    def check_sqaures(self, board):
        for i in xrange(3):
            for j in xrange(3):
                temp = set()
                for k in xrange(3):
                    for l in xrange(3):
                        if board[i*3+k][j*3+l] == '.':
                            continue
                        if board[i*3+k][j*3+l] in temp:
                            return False
                        else:
                            temp.add(board[i*3+k][j*3+l])
        return True
    
    def isValidSudoku(self, board):
        return self.check_rows(board) and self.check_cols(board) and self.check_sqaures(board)