class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.':
                    continue
                if n in row[r] or n in col[c] or n in square[(r//3, c//3)]:
                    return False
                row[r].add(n)
                col[c].add(n)
                square[(r//3, c//3)].add(n)
        return True


        