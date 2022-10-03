class Solution:
    def largestWordCount(self, messages, senders):
        d = {}
        for a in senders:
            d[a] = 0
        for i,j in enumerate(messages):
            d[senders[i]] = d.get(senders[i]) + len(j.split())
        tt = max(sorted(d.values()))
        m = list(d.values()).count(tt)
        if m == 1:
            ind = list(d.values()).index(tt)
            return list(d.keys())[ind]
        zz = {}
        oo = sorted(d.items(), key=lambda item: item[1])
        for z in range(1, m+1):
            zz[oo[-z][0]] = oo[-z][1]
        lll=sorted(zz)[::-1] 
        return lll[0]
