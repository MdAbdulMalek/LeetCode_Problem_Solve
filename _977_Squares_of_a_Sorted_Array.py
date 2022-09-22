class Solution:
    def sortedSquares(self, nums):
        for a in range(len(nums)):
          nums[a] = abs(nums[a])
        nums.sort()
        for i in range(len(nums)):
          nums[i]= nums[i]*nums[i]
        return nums
object1 = Solution()
print(object1.sortedSquares([-7,-3,2,3,11]))
