class Solution:
    def wordPattern(self, pattern, s):
        s_list =list(pattern)
        w_list = s.split()
        d_s = {}
        d_w = {}
        n_s = [d_s.setdefault(i, len(d_s)) for i in s_list]
        n_w = [d_w.setdefault(i, len(d_w)) for i in w_list]
        if n_s == n_w:
            return True
        else:
            return False
ob1 = Solution()
print(ob1.wordPattern("aaaa", "dog cat cat dog"))