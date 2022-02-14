class Solution:
    def findTheDifference(self, s, t):
        l=[]
        if len(s) == 0:
            return t
        else:
            for i in t:
                c_s= s.count(i)  
                c_t= t.count(i)
                if c_s != c_t:
                    return i
                else:
                    if i not in s:
                        return i         
ob1 = Solution()
print(ob1.findTheDifference("abcd","dtbac"))
