#class Solution:
    #def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort(key = lambda x: (x[0], -x[1]))
        #res = prev = 0
        #for _, r in intervals:
            #if r > prev:
                #res += 1    
                #prev = r
        #return res
        
        
 class Solution:
    def removeCoveredIntervals(self, intervals):
      l = []
      for i,j in enumerate(intervals):       
        for y,z in enumerate(intervals):
          if j[0] >= z[0] and j[1] <= z[1] and i!=y:
            l.append(j)
      res = []
      [res.append(x) for x in l if x not in res]
      for h in res:
        intervals.remove(h)
      return len(intervals)
ob1 = Solution()
print(ob1.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))
