class Solution:
    def minimumCost(self, cost):
        if len(cost) <= 2: return sum(cost)
        s = sorted(cost, reverse = True)
        final = sum(s)
        print(s)
        for i in range(2, len(s), 3):
            print( s[i])
            final = final - s[i]
        return final

object1 = Solution()
print(object1.minimumCost([6,5,7,9,2,2]))
