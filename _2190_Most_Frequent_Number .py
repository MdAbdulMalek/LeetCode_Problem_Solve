class Solution:
    def mostFrequent(self, nums, key):
        d = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] in d:
                    d[nums[i + 1]] += 1
                else:
                    d[nums[i + 1]] = 1
        return max(d, key = lambda j : d[j])

object1 = Solution()
print(object1.mostFrequent([1,100,200,1,100,1, 50], 1)) 
