class Solution:
    def validMountainArray(self, arr):        
        if len(arr) >= 3:
            first=[]
            last=[]
            i=0
            while True:
                if arr[i] < arr[i+1]:
                    first.append(1)
                    i = i + 1
                    if i == (len(arr)-1) or arr[i] > arr[i+1] or arr[i] == arr[i+1]:
                        break
                else:
                    first.append(0)
                    i = i + 0
                    break            
            while True:
                if i == (len(arr)-1):
                    last.append(0)
                    break
                if arr[i] > arr[i+1]:
                    last.append(1)
                    i = i + 1
                    if i == (len(arr)-1):
                        break
                else:
                    last.append(0)
                    i = i + 0
                    break
        else:
            return False
        if 0 in first or 0 in last:
            return False
        else:
            return True

ob1 = Solution()
print(ob1.validMountainArray([2,1]))