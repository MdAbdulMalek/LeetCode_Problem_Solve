class Solution:
    def numMatchingSubseq(self, s, words):
        final = []
        for z in words:
            if len(z) < 1:
                final.append(5)
            if len(s) < 1:
                break
            res = []
            a = 0
            for i in s:
                if len(res) != len(z) and i == z[a]:
                    res.append(1)
                    a = a + 1
            if len(z) == len(res):
                final.append(5)
        return len(final)
ob1=Solution()
print(ob1.numMatchingSubseq("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
