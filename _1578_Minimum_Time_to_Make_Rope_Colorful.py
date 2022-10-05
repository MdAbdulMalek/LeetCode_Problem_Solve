class Solution:
    def minCost(self, colors, neededTime): 
        if len(colors)==1:
              return 0
        sum=0
        total=0
        ind=0
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                if ind==0:
                    sum+=neededTime[i-1]+neededTime[i]
                    ind=max(neededTime[i-1],neededTime[i])
                else:                   
                    sum+=neededTime[i]
                    ind=max(ind,neededTime[i])
            else:
                total+=sum-ind
                sum=0
                ind = 0
        if sum:
            total+=sum-ind            
        return total     
object1 = Solution()
print(object1.minCost("aabaa", [1,2,3,4,1])) 
        
