class Solution:
    def searchRange(self, nums, target):
        n = nums.count(target)
        if n == 0:
            return [-1,-1]
        else:
            ind = nums.index(target)
            return [ind, ind+(n-1)]
object1 = Solution()
print(object1.searchRange([], 0)) 
