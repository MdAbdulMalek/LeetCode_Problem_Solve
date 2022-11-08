class Solution:
    def findDifference(self, nums1, nums2):
        final = []
        temp = []
        nums2 = list(set(nums2))
        for i in set(nums1):
            if i not in set(nums2): 
                temp.append(i)
            else:
                nums2.remove(i)
        final.append(temp)
        final.append(nums2)
        return final     

ob1 = Solution()
print(ob1.findDifference([1,2,3],[2,4,6]))   
