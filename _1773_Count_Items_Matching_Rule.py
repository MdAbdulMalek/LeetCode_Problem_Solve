class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        final = 0
        if ruleKey == 'type': 
            ind = 0
        if ruleKey == 'color':
            ind = 1
        if ruleKey == 'name':
            ind = 2
        for i in items:
            if ruleValue == i[ind]:
                final = final + 1
        return final
object1 = Solution()
print(object1.countMatches([["phone","blue","pixel"],["phone","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
        
