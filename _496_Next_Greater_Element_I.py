class Solution:
    def nextGreaterElement(self, nums1, nums2):
        final = []
        for z in nums1:
            found = False
            ind = nums2.index(z)
            for i in range(ind+1, len(nums2)):
                if nums2[i] > z:
                    final.append(nums2[i])
                    found = True
                    break
                else: found = False
            if found == False: final.append(-1)                   
        return final
