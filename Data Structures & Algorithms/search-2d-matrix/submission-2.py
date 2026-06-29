class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        def posToNum(row: int, column: int) -> int: 
            return row * rows + column

        def numToPos(num: int) -> (int, int):
            return (num // columns, num % columns)

        def bs(start: int, end: int) -> int:
            if start > end:
                return -1

            mid_num = (start + end) // 2
            mid_row, mid_col = numToPos(mid_num)
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return mid_val
            elif mid_val < target:
                return bs(mid_num + 1, end)
            else:
                return bs(start, mid_num - 1)
        
        found_index = bs(0, rows * columns - 1)
        return found_index != -1

