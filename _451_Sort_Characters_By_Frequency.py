class Solution:
    def frequencySort(self, s):
        l = []
        final = []
        ss = sorted(set(s))
        for i in ss:
            t = s.count(i)
            l.append(t)
        for j in range(len(ss)):  
            m = max(l)
            ind = l.index(m)
            final.append(ss[ind]*l[ind])
            l[ind] = 0
        f=''.join(final)
        return f
