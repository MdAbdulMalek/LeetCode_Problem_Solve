class Solution:
    def minimumAbsDifference(self, arr):
        final = []
        d = {}
        s = sorted(arr)
        for i in range(len(s)-1):
            d[s[i], s[i+1]] = abs(s[i]-s[i+1])
        m = min(d.values())
        for j in d.items():
            if j[1] == m:
                final.append(list(j[0]))
        return final
object1 = Solution()
print(object1.minimumAbsDifference([1,3,6,10,15]))
