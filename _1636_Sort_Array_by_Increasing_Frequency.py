class Solution:
    def frequencySort(self, nums):
        first = sorted(nums, reverse=True)
        final = sorted(first, key=nums.count)
        return final
object1 = Solution()
print(object1.frequencySort([2,3,1,3,2])) 
