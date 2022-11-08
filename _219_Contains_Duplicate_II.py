class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(dic[nums[i]]-i) <= k:
                    return True
            dic[nums[i]] = i
        return False
ob1 = Solution()
print(ob1.containsNearbyDuplicate([1,2,3,1,2,3],2))
