class Solution:
    def intersection(self, nums1, nums2):
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
        return sorted(set(final))
ob1 = Solution()
print(ob1.intersection([4,9,5],[9,4,9,8,4]))
