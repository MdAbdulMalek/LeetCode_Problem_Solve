class Solution:
    def commonChars(self, words):
        ans = list(words[0])
        for j in words[1:]:
            final = []
            for k in j:
                if k in ans: 
                    final.append(k)
                    ans.remove(k)
            ans = final
        return ans

ob1 = Solution()
print(ob1.commonChars(["cool","lock","cook"]))
