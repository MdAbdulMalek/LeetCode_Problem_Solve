class Solution:
    def twoSum(self, nums, target):
        required = {}
        for i in range(len(nums)):
             if target - nums[i] in required:
                return [required[target - nums[i]],i]
             else:
                required[nums[i]]=i
object1 = Solution()
print(object1.twoSum([2,5,5,11], 10))