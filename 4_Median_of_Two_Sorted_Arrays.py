class Solution:
      def findMedianSortedArrays(self,x,y):
        listt= sorted(x+y)
        new=len(listt)
        midddle=new//2
        final=(listt[midddle] + listt[~midddle]) / 2
        return final
obj=Solution()
print(obj.findMedianSortedArrays([1,5,8],[10,9,7,5]))
