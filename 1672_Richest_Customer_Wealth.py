class Solution:
    def maximumWealth(self, accounts):
        max = 0
        for i in accounts:
            now = sum(i)
            if now > max:
                max = now
        return max        
ob1 = Solution()
print(ob1.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))