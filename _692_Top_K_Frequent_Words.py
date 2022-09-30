class Solution:
    def topKFrequent(self, words, k):
        s= sorted(set(words))
        l = []
        final = []
        for i in s:
            t = words.count(i)
            l.append(t)
        for z,j in enumerate(range(k)):
            m = max(l)
            ind = l.index(m)
            final.append(list(s)[ind])
            l[ind] = 0
        return final

object1 = Solution()
print(object1.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
