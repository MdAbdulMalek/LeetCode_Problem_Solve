class Solution:
    def hammingWeight(self, n):
        ans = bin(n).count('1')
        return ans

object1 = Solution()
print(object1.hammingWeight(11111111111111111111111111111101))
