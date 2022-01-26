class Solution:
    def addBinary(self, a, b):
        int_sum = int(a, 2) + int(b, 2)
        bin_sum = bin(int_sum)
        str1 = []
        for ele in bin_sum: 
            str1 += ele
        str1.remove(str1[0])
        str1.remove(str1[0])
        str2=""
        for i in str1:
            str2 += i
        return str2

ob1 = Solution()
print(ob1.addBinary("1010", "1010"))