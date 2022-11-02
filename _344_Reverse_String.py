class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]

ob1 = Solution()
print(ob1.reverseString(["h","e","l","l","o"]))    
