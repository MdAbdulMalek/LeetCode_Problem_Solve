class Solution:
    def addDigits(self, num):
            if num < 10:
                return num
            else:
                sum = 0
                r=0
                while True:
                        digit = num % 10
                        r= r * 10 + digit
                        num //= 10 
                        sum = sum + digit
                        if sum > 9 and num == 0:
                            num = sum
                            sum=0

                        if num == 0:
                            break
                return sum
ob1 = Solution()
print(ob1.addDigits(299))
