class Solution:
    def romanToInt(self, s):
        n_IV=s.count("IV")
        n_IX=s.count("IX")
        n_XL=s.count("XL")
        n_XC=s.count("XC")
        n_CM=s.count("CM")
        n_CD=s.count("CD")
        n_I=s.count("I")
        n_V=s.count("V")
        n_X=s.count("X")
        n_L=s.count("L")
        n_C=s.count("C")
        n_D=s.count("D")
        n_M=s.count("M")
        
        total = ((n_I*1)-((n_IV*1)+(n_IX*1)))+((n_V*5)-(n_IV*1))+((n_X*10)-((n_XC*10)+(n_IX*1)+(n_XL*10)))+((n_L*50)-(n_XL*10))+((n_C*100)-((n_CM*100)+(n_XC*10)+(n_CD*100)))+((n_D*500)-(n_CD*100))+((n_M*1000)-(n_CM*100))
        
        return total

        

ob1 = Solution()
print(ob1.romanToInt("III"))
