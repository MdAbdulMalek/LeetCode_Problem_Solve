class Solution:
    def titleToNumber(self, columnNumber):
        sum = 0
        A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(columnNumber)):
             sum= sum * 26
             sum = sum + A.index(columnNumber[i])+1
        return sum

ob1 = Solution()
print(ob1.titleToNumber("ZY"))