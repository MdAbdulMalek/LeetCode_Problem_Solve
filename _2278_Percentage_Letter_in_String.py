class Solution:
    def percentageLetter(self, s, letter):
        return int((s.count(letter)/len(s))*100)

object1 = Solution()
print(object1.percentageLetter("jjjj", "k")) 
