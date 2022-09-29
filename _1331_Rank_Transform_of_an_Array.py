class Solution:
    def arrayRankTransform(self, arr):              
        emp = {}
        s = list(sorted(set(arr)))
        for i in range(len(s)):
            emp[s[i]]=i+1 
        return [emp[i] for i in arr]
object1 = Solution()
print(object1.arrayRankTransform([40,10,20,30,10])) 
