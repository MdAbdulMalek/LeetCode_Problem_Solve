class Solution:
    def digitSum(self, s, k):
        if len(s) <=k : return s
        while len(s)>k:
            tmp = []
            for i in range(0, len(s), k):
                tmp.append(s[i:i+k])
            for i,t in enumerate(tmp):
                sum = 0
                for j in tmp[i]:
                    sum += int(j)
                tmp[i] = str(sum)
            s = ''.join(tmp)
        return s	

object1 = Solution()
print(object1.digitSum("1",2))
