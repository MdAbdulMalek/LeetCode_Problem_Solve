class Solution:
    def intersect(self, nums1, nums2):
        final = []
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            choto = nums2
            boro = nums1
        else:
            choto = nums1
            boro = nums2
        for i in choto:
            if i in boro: 
                final.append(i)
                boro.remove(i)
        return final
ob1 = Solution()
print(ob1.intersect([1,2,2,1],[2,2])) 
