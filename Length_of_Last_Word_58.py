class Solution:
    def lengthOfLastWord(self, s):
      ss = s.split()
      l = len(ss)
      return len(ss[l-1])

ob1 = Solution()
print(ob1.lengthOfLastWord("Hello World"))