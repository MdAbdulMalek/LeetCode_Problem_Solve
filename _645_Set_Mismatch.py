class Solution:
    def findErrorNums(self, nums):
        s = sum(nums)
        ss = set(nums)
        sss = sum(ss)
        for i in range(1, len(nums)+1):
            if i not in ss:
                l = i
                break
        return [s-sss,l]
