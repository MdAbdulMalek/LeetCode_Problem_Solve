class Solution:
    def findDuplicate(self, nums):
        s = sorted(nums)
        for h,i in enumerate(s):
            if i == s[h+1]: return i
