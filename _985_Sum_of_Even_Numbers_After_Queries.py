class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        final = []
        sum = 0
        for k in nums:
            if k%2 == 0:
                sum = sum + k
        for j in queries:
            f = nums[j[1]]
            nums[j[1]] = nums[j[1]]+j[0]
            if f%2 == 0 and nums[j[1]] %2 == 0:
                sum = sum + (nums[j[1]] -f)
            elif f%2 != 0 and nums[j[1]] %2 == 0:
                sum = sum + nums[j[1]]
            elif f%2 == 0 and nums[j[1]] %2 != 0:
                sum = sum - f
            final.append(sum)
        return final
object1 = Solution()
print(object1.sumEvenAfterQueries([1],[[4,0]]))
