class Solution:
    def removeDuplicates(self, s):
        final = []
        for i in range(len(s)):
            if final and final[-1] == s[i]:
                final.pop(-1)
            else:
                final.append(s[i])              
        return ''.join(final)
      
ob1 = Solution()
print(ob1.removeDuplicates("azxxzy"))
