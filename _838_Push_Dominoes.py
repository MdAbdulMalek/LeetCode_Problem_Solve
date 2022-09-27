class Solution:
    def pushDominoes(self, dominoes):
        final = ''
        while dominoes != final:
            final = dominoes
            dominoes = dominoes.replace('R.L', '***')      
            dominoes = dominoes.replace('R.', 'RR')         
            dominoes = dominoes.replace('.L', 'LL')         

        return  dominoes.replace('***', 'R.L') 

object1 = Solution()
print(object1.pushDominoes(".L.R...LR..L.."))
