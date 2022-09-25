class Solution:
    def isPowerOfThree(self, n):
        for i in range(n):
            val = 3 ** i
            if val == n:
                return True
            if val > n:
                break
        return False

object1 = Solution()
print(object1.isPowerOfThree(0))
