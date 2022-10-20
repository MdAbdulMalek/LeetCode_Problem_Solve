class Solution:
    def missingNumber(self, nums):
        s = sorted(nums)
        for i in range(len(nums)):
            if i != s[i]: return i
        return s[-1]+1

ob1 = Solution()
print(ob1.missingNumber([9,6,4,2,3,5,7,0,1]))
