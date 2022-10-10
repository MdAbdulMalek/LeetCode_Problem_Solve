class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

object1 = Solution()
print(object1.arrayPairSum([6,2,6,5,1,2]))   
