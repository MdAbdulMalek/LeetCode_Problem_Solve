class Solution:
    def isAnagram(self, s, t):
        su = set(s)
        for i in su:
            cs = s.count(i)
            ts = t.count(i)
            if cs != ts:
                return False
        return True

object1 = Solution()
print(object1.isAnagram("rat", "car"))
