class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        final = [0] * n    
        for i in range(n - 2, -1, -1):
            c = i + 1
            while temperatures[i] >= temperatures[c] and final[c] > 0:
                c += final[c]      
            if temperatures[c] > temperatures[i]:
                final[i] = c - i
        return final
