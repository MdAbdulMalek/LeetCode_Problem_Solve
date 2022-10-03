class Solution:
    def repeatedCharacter(self, s):
        emp = [s[0]]
        for i in range(1,len(s)):
            if s[i] in emp:
                return s[i]          
            else:
                emp.append(s[i])
            
object1 = Solution()
print(object1.repeatedCharacter("abccbaacz")) 
