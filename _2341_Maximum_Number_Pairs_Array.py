class Solution:
    def numberOfPairs(self, nums):
        pair = 0
        final = []
        s =  set(nums)
        for i in s:
            c = nums.count(i)
            if c == 2 or c == 3:
                pair = pair + 1
                nums.remove(i)
                nums.remove(i)
            if c >= 4:
                pair = pair + c//2
                for j in range((c//2)*2): nums.remove(i)
        final.append(pair)
        final.append(len(nums))
        return final

object1 = Solution()
print(object1.numberOfPairs([1,1]))
