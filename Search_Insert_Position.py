class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            new = nums
            new.append(target)
            new.sort()
            return new.index(target)

ob1 = Solution()
print(ob1.searchInsert([1,3,5,6], 7))