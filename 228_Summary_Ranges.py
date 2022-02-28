class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return nums
        start=-1
        ans=[]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1 and start==-1:
                start=nums[i-1]
            if nums[i]-nums[i-1]!=1:
                if start==-1:
                    ans.append(str(nums[i-1]))
                else:
                    ans.append(str(start)+'->'+str(nums[i-1]))
                    start=-1
        if start==-1:
            ans.append(str(nums[-1]))
        else:
            ans.append(str(start)+'->'+str(nums[-1]))
        return ans
ob1 = Solution()
print(ob1.summaryRanges([0,1,2,4,5,7]))
