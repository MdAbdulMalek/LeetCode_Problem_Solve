class Solution:
    def isPalindrome(self, s):
        final = ""
        for i in [*s]:
            if i.isalpha(): final += i.lower()
            if i.isnumeric(): final += i
        if final == final[::-1]: return True
        else: return False

ob1 = Solution()
print(ob1.isPalindrome("0P"))
