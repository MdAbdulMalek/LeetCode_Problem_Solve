class Solution:
    def rotate(self, matrix):
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(i, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for r in range(row):
            i, j = 0, col - 1
            while i < j:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
                i += 1
                j -= 1
object1 = Solution()
print(object1.rotate([[1,2,3],[4,5,6],[7,8,9]]))
