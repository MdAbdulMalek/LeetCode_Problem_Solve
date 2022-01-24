class Solution:
    def detectCapitalUse(self, word):
        l = []
        for i in word:
            num = ord(i)
            if num <= 90 and num >= 65:
                l.append(1)
            else:
                l.append(0)
        first = l[0]
        if len(word) == 1:
            return True
        elif first == 0 and 1 in l:
            return False
        elif first != 0 in l and l.count(1)>1 and 0 in l:
            return False
        else:
            return True
        
ob1 = Solution()
print(ob1.detectCapitalUse("USA"))