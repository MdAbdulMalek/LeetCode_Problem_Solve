class Solution:
    def reverseStr(self, s, k):
        for i in range(0, len(s)+1, k*2):
                ss = s[i:i+k][::-1]
                s = s.replace(s[i:i+k], ss)
        return s
        
ob1 = Solution()
print(ob1.reverseStr("abcd", 2)) 
