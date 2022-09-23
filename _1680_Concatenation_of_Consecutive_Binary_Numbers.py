class Solution:
    def concatenatedBinary(self, n):
        value = ''
        m = 1000000007
        for i in range(1, n+1):
            b = bin(i) 
            value = value + b[2:]
        return (int(value, 2)%m)

object1 = Solution()
print(object1.concatenatedBinary(12))
