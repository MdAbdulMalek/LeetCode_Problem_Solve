class Solution:
    def addToArrayForm(self, num, k):
        num1 = ''
        for i in range(len(num)):
            num1 =  num1 + str(num[i])
        ans = int(num1) + k
        l = []
        for j in str(ans):
            l.append(int(j))
        return l
object1 = Solution()
print(object1.addToArrayForm([2,1,5],806))
