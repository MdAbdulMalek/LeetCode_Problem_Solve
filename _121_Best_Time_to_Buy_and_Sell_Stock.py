class Solution:
    def maxProfit(self, prices):    
        max_p = 0
        min_p = float('inf')
        for i in prices:
            min_p = min(min_p, i)
            profit = i - min_p
            max_p = max(max_p, profit)
        return max_p
ob1 = Solution()
print(ob1.maxProfit([2,4,1])) 
