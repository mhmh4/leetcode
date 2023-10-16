class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for _ in range(rowIndex + 1)]
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row
