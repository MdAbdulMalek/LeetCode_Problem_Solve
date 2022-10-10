class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4: 
            return 0
        nums.sort()
        m = []
        n=4
        for i in range(1, 5):
            m.append(nums[-i] - nums[n-i])
        return min(m)
