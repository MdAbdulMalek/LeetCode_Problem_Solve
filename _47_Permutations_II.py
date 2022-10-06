class Solution:
    def permuteUnique(self, nums):
        a = list(itertools.permutations(nums))

        return list(set(a))
