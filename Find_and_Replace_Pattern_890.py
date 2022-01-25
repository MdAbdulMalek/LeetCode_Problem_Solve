class Solution:
    def findAndReplacePattern(self, words, pattern):
        output=[]
        d_p = {}
        n_p = [d_p.setdefault(i, len(d_p)) for i in pattern]
        w = list(words)
        for i in w:
            d_t={}
            t_t = [d_t.setdefault(i, len(d_t)) for i in i]
            if t_t == n_p:
                output.append(i)
        return output
     
ob1 = Solution()
print(ob1.findAndReplacePattern(["a","b","c"], "a"))