# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
      def rand10(self):
            first = rand7()
            second = rand7()
            temp = (first - 1) * 7 + second
            if temp > 40:
                return self.rand10()
            return (temp % 10) + 1
