class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

object1 = Solution()
print(object1.increasingTriplet([20,100,10,12,5,13]))
