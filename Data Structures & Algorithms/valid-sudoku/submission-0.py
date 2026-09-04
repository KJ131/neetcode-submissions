class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes = {}
        for i in range(9):
            rows[i] = set()

        for i in range(9):
            columns[i] = set()

        for i in range(3):
            for j in range(3):
                boxes[(i,j)] = set()

        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == '.':
                    continue
                if value in rows[row]:
                    return False
                if value in columns[column]:
                    return False
                if value in boxes[(row//3, column//3)]:
                    return False
                rows[row].add(value)
                columns[column].add(value)
                boxes[(row//3, column//3)].add(value)
        return True