class Solution:
    def singleNumber(self, nums):
      if len(nums) == 1:
        return nums[0]
      else:
        for i in nums:
          c = nums.count(i)
          if c != 2:
            return i
ob1 = Solution()
print(ob1.singleNumber([-1,-1,-2]))
