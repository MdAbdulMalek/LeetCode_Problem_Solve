class Solution:
    def mostFrequentEven(self, nums):
        even_num = list(filter(lambda x: (x%2==0),nums)) 
        max = 0
        final = 0
        s = sorted(even_num)
        s.sort(reverse=True)
        for i in (s):
            c = even_num.count(i)
            if c >= max:
                max = c
                final = i
        if len(even_num) <= 0:
            return -1
        return final

object1 = Solution()
print(object1.mostFrequentEven([29,47,21,41,13,37,25,7]))
