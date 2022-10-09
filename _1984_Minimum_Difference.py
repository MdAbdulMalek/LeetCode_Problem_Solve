class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        arr = nums[:k]
        final = arr[-1] - arr[0]
        print(final, arr)
        for i in range(k, len(nums)):
            arr.pop(0)
            arr.append(nums[i])
            final = min(final, arr[-1] - arr[0])
            
        return final
object1 = Solution()
print(object1.minimumDifference([9,4,1,7], 2)) 
