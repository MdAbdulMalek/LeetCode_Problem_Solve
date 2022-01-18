class Solution:
    def isPalindrome(self, x):
        a = str(x)
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
ob1 = Solution()
print(ob1.isPalindrome(121))