class Solution:
    def convertToTitle(self, columnNumber):
        ans = []
        A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while columnNumber > 0:
             m = columnNumber % 26
             ans.append(A[m-1])
             columnNumber = (columnNumber-1) // 26
        ans.reverse()
        return ''.join(ans)

ob1 = Solution()
print(ob1.convertToTitle(28))
