class Solution:
    def findClosestElements(self, arr, k, x):       
        i = 0
        ran = len(arr)-1   
        while (ran-i)+1 > k:
            if abs(arr[i]-x) <= abs(arr[ran]-x):
                ran-=1
            else:
                i+=1   
            
        return arr[i:ran+1]

object1 = Solution()
print(object1.findClosestElements([-2,-1,1,2,3,4,5], 7, 3))
