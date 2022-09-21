class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m] = nums2[i]
            m +=1
        nums1.sort()       
object1 = Solution()
print(object1.merge([0],0,[1],1))
