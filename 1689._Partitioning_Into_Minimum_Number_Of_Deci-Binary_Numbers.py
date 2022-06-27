class Solution:
    def minPartitions(self, n):
        ans = 0
        for i in n:
            ans = max(ans, int(i))
        return ans

object1 = Solution()
print(object1.minPartitions('32'))
