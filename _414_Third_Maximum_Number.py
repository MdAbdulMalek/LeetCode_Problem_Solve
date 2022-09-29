class Solution:
    def thirdMax(self, nums):
        s = sorted(set(nums))
        if len(s) >= 3:
            return s[-3]
        return s[-1]
object1 = Solution()
print(object1.thirdMax([2,2,3,1]))
