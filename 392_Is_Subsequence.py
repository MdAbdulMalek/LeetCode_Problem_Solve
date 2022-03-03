class Solution:
    def isSubsequence(self, s, t):
        if len(s) < 1:
            return True
        if len(t) < 1:
            return False
        res = []
        a = 0
        for h,i in enumerate(t):
            if len(res) != len(s) and i == s[a]:
                res.append(1)
                a = a + 1

        if len(s) == len(res):
            return True
        else:
            return False                 
ob1=Solution()
print(ob1.isSubsequence("twn","xxxxxtxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxnw"))
