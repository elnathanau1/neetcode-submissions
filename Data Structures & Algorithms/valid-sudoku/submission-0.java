class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rows = new ArrayList<>();
        List<Set<Character>> columns = new ArrayList<>();
        List<Set<Character>> squares = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            rows.add(new HashSet<Character>(Arrays.asList('1','2','3','4','5','6','7','8','9')));
            columns.add(new HashSet<Character>(Arrays.asList('1','2','3','4','5','6','7','8','9')));
            squares.add(new HashSet<Character>(Arrays.asList('1','2','3','4','5','6','7','8','9')));
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] != '.') {
                    char num = board[i][j];
                    int squareNum = i / 3 * 3 + j / 3;
                    if (!rows.get(i).remove(num) || !columns.get(j).remove(num) || !squares.get(squareNum).remove(num)) {
                        return false;
                    }

                    /**
                    i / 3 * 3 + j / 3

                    0, 0 -> 0
                    2, 2 -> 0
                    3, 3 -> 4
                    */
                }
            }
        }

        return true;
    }
}
