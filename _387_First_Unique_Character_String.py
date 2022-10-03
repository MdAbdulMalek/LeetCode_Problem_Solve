class Solution:
    def firstUniqChar(self, s):
        for h,i in enumerate(s):
            c = s.count(i)
            if c == 1:
                return h
        return -1

object1 = Solution()
print(object1.firstUniqChar("aabb"))
