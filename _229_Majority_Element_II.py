class Solution:
    def majorityElement(self, nums):
        s = set(nums)
        l = len(nums)/3
        final = []
        for i in s:
            c = nums.count(i)
            if c > l:
                final.append(i)
        return final

object1 = Solution()
print(object1.majorityElement([1,2]))
