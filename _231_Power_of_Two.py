class Solution:
    def isPowerOfTwo(self, n):
        for i in range(n):
            val = 2 ** i
            if val == n:
                return True
            if val > n:
                break
        return False

object1 = Solution()
print(object1.isPowerOfTwo(64))
