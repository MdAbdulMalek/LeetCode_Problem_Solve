class Solution:
    def moveZeroes(self, nums):
        c = nums.count(0)
        for i in range(c):
            nums.remove(0)
            nums.append(0)

ob1 = Solution()
print(ob1.moveZeroes([0]))
