class Solution:
    def firstBadVersion(self, n: int) -> int:
        first=1
        last=n
        while first<=last:
            mid = (first+last)//2
            ans=isBadVersion(mid)
            if ans==True and isBadVersion(mid-1)==False:
                return mid
            if ans == False:
                first = mid + 1
            else:
                last =  mid - 1
