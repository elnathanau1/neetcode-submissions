class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        square_index_map = []
        for _ in range(3):
            square_index_map.append([0,0,0,1,1,1,2,2,2])
        
        for _ in range(3):
            square_index_map.append([3,3,3,4,4,4,5,5,5])
        
        for _ in range(3):
            square_index_map.append([6,6,6,7,7,7,8,8,8])

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val.isdigit():
                    sq = square_index_map[i][j]
                    if val in rows[i] or val in columns[j] or val in squares[sq]:
                        return False
                    rows[i].add(val)
                    columns[j].add(val)
                    squares[sq].add(val)
        
        return True