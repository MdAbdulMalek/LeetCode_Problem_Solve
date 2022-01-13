class Solution:
    def containsDuplicate(self, nums):
        n1= len(nums)
        n2=len(set(nums))
        if n1 == n2:
            return False
        else:
            return True
        
ob1 = Solution()
print(ob1.containsDuplicate([3,2,2,3]))