class Solution:
    def removeAnagrams(self, words):
        final = [words[0]]
        for i in range(1,len(words)):
            cs = sorted(words[i])
            ts = sorted(words[i-1])
            if cs != ts:
                final.append(words[i])    
        return final
object1 = Solution()
print(object1.removeAnagrams(["a","b","c","d","e"]))
