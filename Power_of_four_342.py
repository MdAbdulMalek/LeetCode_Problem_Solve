class Solution:
    def isPowerOfFour(self, n):
        if n==0: return False
        elif n==1: return True
        else:
            while (n != 1):
                if (n % 4 != 0):
                    return False
                n = n // 4
            return True
object1 = Solution()
print(object1.isPowerOfFour(1))
