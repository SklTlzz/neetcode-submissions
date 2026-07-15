class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map_str = dict()
        hash_map_col = dict()
        hash_map_sqr = dict()
        
        for i in range(len(board)):
            for j in range(len(board)):
                sqr_cords = (i // 3 , j // 3)

                if board[i][j] == ".":
                    continue

                if board[i][j] in hash_map_str.get(i, set()):
                    return False
                hash_map_str.setdefault(i, set()).add(board[i][j])

                if board[i][j] in hash_map_sqr.get(sqr_cords, set()):
                    return False
                hash_map_sqr.setdefault(sqr_cords, set()).add(board[i][j])

                if board[i][j] in hash_map_col.get(j, set()):
                    return False
                hash_map_col.setdefault(j, set()).add(board[i][j])
                    
        return True
