class Solution:
    def triangularSum(self, nums):
        for i in range(len(nums)-1):
            temp = []
            for j in range(len(nums)-1):
                temp.append((nums[j] + nums[j+1])%10)
            nums = temp
        return nums[0]
object1 = Solution()
print(object1.triangularSum([1,2,3,4,5]))
