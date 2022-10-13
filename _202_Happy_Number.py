class Solution:
    def isHappy(self, n):
        res = set()
        while n not in res:
            res.add(n)
            my_list = [int(x) for x in str(n)]
            n = sum(x*x for x in my_list)
            if n == 1: return True
        
        return False
ob1 = Solution()
print(ob1.isHappy(19))
