class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        used = set()
        def search(i: int, j: int, word: str) -> bool: 
            if not word: 
                return True

            if i < 0 or j < 0 or i >= rows or j >= columns or (i,j) in used:
                return False

            char = word[0]
            if board[i][j] != char:
                return False
            used.add((i,j))

            found = search(i+1, j, word[1:]) or search(i-1, j, word[1:]) or search(i, j + 1, word[1:]) or search(i, j-1, word[1:])

            used.remove((i,j))
            return found
        
        for i in range(rows):
            for j in range(columns):
                if search(i,j,word):
                    return True

        return False