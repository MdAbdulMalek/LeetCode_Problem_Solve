class Solution:
    def topKFrequent(self, nums, k):
        s= set(nums)
        l = []
        final = []
        for i in s:
            t = nums.count(i)
            l.append(t)
        for z,j in enumerate(range(k)):
            m = max(l)
            ind = l.index(m)
            final.append(list(s)[ind])
            l[ind] = 0
        return final
object1 = Solution()
print(object1.topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))
