class Solution:
    def lengthOfLongestSubstring(self, s):
        s.replace(" ", "-")
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        else:
            l = []
            max = 0
            final1, final2 = 0, 0
            for i in s:
                l.append(i)
                max = max + 1
                c = l.count(i)               
                if c > 1:
                    if final1 < max:                       
                        final1 = max -1                   
                    ind = l.index(i)
                    l = l[-(len(l)-(ind+1)):]
                    max = len(l)
                    c = 0
                else:
                    final2 = max
            if final1 > final2:
                return final1
            else:
                return final2        
ob1 = Solution()
print(ob1.lengthOfLongestSubstring("pwwkew"))
