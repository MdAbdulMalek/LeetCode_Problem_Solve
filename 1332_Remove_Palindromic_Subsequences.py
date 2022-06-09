class Solution:
    def removePalindromeSub(self, s):
        if(s == " "):
            return 0
        elif(s == s[::-1]):
            return 1
        else:
            return 2
object1 = Solution()
print(object1.removePalindromeSub("abb"))
