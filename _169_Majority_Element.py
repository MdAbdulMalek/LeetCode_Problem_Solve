class Solution:
    def majorityElement(self, nums):
        s = set(nums)
        l = len(nums)/2
        for i in s:
            c = nums.count(i)
            if c > l:
                return i
object1 = Solution()
print(object1.majorityElement([2,2,1,1,1,2,2]))  
