class Solution:
    def reverseBits(self, n):
        i = f"{n:#034b}"
        res = int(i[::-1][:-2], 2)
        return res

object1 = Solution()
print(object1.reverseBits(11111111111111111111111111111101))
