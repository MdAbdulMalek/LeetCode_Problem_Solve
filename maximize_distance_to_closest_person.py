class Solution:
    def maxDistToClosest(self, seats):
        prev, result = -1, 1
        for i in range(len(seats)):
            if seats[i]:
                if prev < 0:
                    result = i
                else:
                    result = max(result, (i-prev)//2)
                prev = i
        return max(result, len(seats)-1-prev)

ob1 = Solution()
print(ob1.maxDistToClosest([1,0,0,0]))
        