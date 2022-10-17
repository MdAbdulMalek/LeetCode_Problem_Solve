class Solution:
    def numJewelsInStones(self, jewels, stones):
        sum = 0
        j = list(jewels)
        for i in j:
            s = stones.count(i)
            sum = sum + s
        return sum
