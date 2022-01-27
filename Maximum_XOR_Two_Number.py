class Solution:
    def findMaximumXOR(self, nums):
        ans = 0
        for i in range(31, -1, -1):
            ans <<= 1
            pre = {n >> i for n in nums}
            ans += any(ans ^ 1 ^ p in pre for p in pre)
        return ans
ob1 = Solution()
print(ob1.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
