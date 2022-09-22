class Solution:
    def getRow(self, rowIndex):
        numRows = rowIndex + 1
        final = [[1]]
        for i in range(numRows - 1):
            temp = [0] + final[-1] + [0]
            temp2 = []
            for j in range(len(final[-1])+1):            
                temp2.append(temp[j] + temp[j+1])
            final.append(temp2)
        return final[rowIndex]

object1 = Solution()
print(object1.getRow(1))
