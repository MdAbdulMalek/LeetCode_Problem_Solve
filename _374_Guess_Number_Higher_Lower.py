class Solution:
    def guessNumber(self, n):
        first=1
        last=n
        while first<=last:
            middle=(first+last)//2
            ans=guess(middle) 
            print(ans, middle)
            if ans==0:
                return middle
            elif ans==1:
                first=middle+1
            else:
                last=middle-1
