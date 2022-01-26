class Solution:
    def plusOne(self, digits):
        str1 = ""
        for ele in digits: 
            str1 += str(ele) 
        int1 = int(str1)
        str2= str(int1 + 1)
        l = []
        for e in str2:
            l.append(e)
        return l

ob1 = Solution()
print(ob1.plusOne([1,2,3]))