class Solution:
    def strStr(self, haystack, needle):
        if haystack == "" and needle == "":
            return 0
        else:
            if haystack == "":
                return -1
            elif needle == "":
                return 0
            elif needle in haystack:
                final = haystack.index(needle)
                return final
            else:
                return -1

ob1 = Solution()
print(ob1.strStr("", ""))