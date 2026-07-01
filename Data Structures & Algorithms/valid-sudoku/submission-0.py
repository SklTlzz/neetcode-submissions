class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hash_map_row = dict()
        hash_map_col = dict()
        hash_map_square = dict()

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != ".":
                    curr_cord = (r // 3, c // 3)
                    if board[r][c] in hash_map_row.get(r, set()) or \
                        board[r][c] in hash_map_col.get(c, set()) or \
                        board[r][c] in hash_map_square.get(curr_cord, set()):
                        return False
                    
                    hash_map_row.setdefault(r, set()).add(board[r][c])
                    hash_map_col.setdefault(c, set()).add(board[r][c])
                    
                    hash_map_square.setdefault(curr_cord, set()).add(board[r][c])

                # if board[j][i] != ".":
                #     if board[j][i] in help_set_col:
                #         return False

                #     help_set_col.add(board[j][i])
                #     curr_cord = (i // 3, j // 3)

                #     if board[j][i] in hash_map_square.setdefault(curr_cord, set()):
                #         return False
                    
                #     hash_map_square.setdefault(curr_cord, set()).add(board[j][i])

        return True
