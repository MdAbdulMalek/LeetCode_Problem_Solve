class Solution(object):
   def bitwiseComplement(self, N):
      s = str(bin(N))
      sum = 0
      num = 1
      for i in s[::-1]:
         if i == "b":
            return sum
         elif i =="0":
            sum+=num
         num*=2
ob1 = Solution()
print(ob1.bitwiseComplement(5))