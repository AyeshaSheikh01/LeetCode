# Valid Sudoku 36 
   
class Solution:
    def isValidSudoku(self, board): 
        board=[[cell if cell!="." else "" for cell in row] for row in board] 
        # for rows logic:  
        for sublist in board:   
            mapSave={} # will check unique entries in each row
            for element in sublist: 
                if element!="": 
                    if element not in mapSave and int(element)<=9:  
                        mapSave[element]=1  
                    else:  
                        return False
        # for cols logic
        for cols_list in range(9): 
            mapcols={}    # will check unique entries in each col
            for rows_list in range(9): 
                element=board[rows_list][cols_list]
                if element!="": 
                    if element not in mapcols and int(element)<=9:  
                        mapcols[element]=1  
                    else:  
                        return False  
        # for grid logic              
        for block_row in range(3):
            for block_col in range(3):
                mapGrid = {} # the grid logic- I took ai help in this part
                start_row = block_row * 3
                start_col = block_col * 3
                for i in range(3):
                    for j in range(3):
                        element = board[start_row + i][start_col + j]
                        if element != "":
                            if element not in mapGrid and int(element) <= 9:
                                mapGrid[element] = 1
                            else:
                                return False
        return True


board=[[".","4",".",".",".",".",".",".","."],[".",".","4",".",".",".",".",".","."],[".",".",".","1",".",".","7",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3",".",".",".","6","."],[".",".",".",".",".","6",".","9","."],[".",".",".",".","1",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".","8",".",".",".",".","."]]
print(Solution().isValidSudoku(board))
        