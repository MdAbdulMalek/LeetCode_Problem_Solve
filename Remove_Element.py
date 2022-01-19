class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        while val in nums:
            nums.remove(val)
        return len(nums)  
    
ob1 = Solution()
print(ob1.removeElement([0,1,2,2,3,0,4,2],2))
