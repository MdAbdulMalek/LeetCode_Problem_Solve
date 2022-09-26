class Solution:
    def equationsPossible(self, equations):
        lc = "abcdefghijklmnopqrstuvwxyz"
        o = []
        for e in equations:
            if e[1] == '=':
                lc = lc.replace(lc[ord(e[0])-97], lc[ord(e[3])-97])
        for e in equations:
            if e[1] == '!':
                if lc[ord(e[0])-97] == lc[ord(e[3])-97]:
                    return False
        return True
object1 = Solution()
print(object1.equationsPossible(["b==a","a==b"]))
