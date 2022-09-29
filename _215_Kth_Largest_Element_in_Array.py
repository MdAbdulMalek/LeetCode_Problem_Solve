class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
object1 = Solution()
print(object1.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) 
