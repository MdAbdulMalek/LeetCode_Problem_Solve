class Solution:
    def lemonadeChange(self, bills):
        if bills[0] != 5: return False
        fi = 1
        te = 0
        for i in range(1, len(bills)):            
            if bills[i] == 5: fi = fi + 1
            elif bills[i] == 10: 
                te = te + 1
                fi = fi - 1
            elif bills[i] == 20:
                if te >= 1 and fi >= 1:
                    te = te - 1
                    fi = fi - 1
                    print("uuu")
                elif te <= 0 and fi >= 3:
                    fi = fi - 3
                else: return False
            print(bills[i], fi, te)
        if fi >= 0 and te >= 0: return True
        else: return False
