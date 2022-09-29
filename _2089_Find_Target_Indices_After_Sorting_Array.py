class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        c = nums.count(target)
        if c == 0:
            return []
        ind = nums.index(target)
        final = []
        for i in range(ind, c+ind):
            final.append(i)
        return final
object1 = Solution()
print(object1.targetIndices([1,2,5,2,3], 3)) 
