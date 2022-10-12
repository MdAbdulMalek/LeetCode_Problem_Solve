class Solution:
    def largestPerimeter(self, nums):
        if len(nums) < 3:
            return 0
        
        nums.sort(reverse = True)
        
        for i in range(3,len(nums)+1):
            if(nums[i-3] < nums[i-2] + nums[i-1]):
                return sum(nums[i-3:i])
        return 0

object1 = Solution()
print(object1.largestPerimeter([2,1,2]))  
