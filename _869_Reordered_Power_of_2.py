class Solution:
    def reorderedPowerOf2(self, n):
        res = sorted(str(n))
        for i in range(30):
            val = 2 ** i
            val = sorted(str(val))
            if res == val:
                return True
        return False

object1 = Solution()
print(object1.reorderedPowerOf2(46)) 
