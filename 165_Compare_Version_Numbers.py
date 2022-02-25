class Solution:
    def compareVersion(self, version1, version2):
        w1= version1.split(".")
        w2= version2.split(".")
        uw1 = []
        uw2 = []
        for i in w1:
            uw1.append(int(i))
        for j in w2:
            uw2.append(int(j))
        if len(uw1) != len(uw2):
            
            if len(uw1) < len(uw2):
                while True:
                    uw1.append(0)
                    if len(uw1) == len(uw2):
                        break
            if len(uw1) > len(uw2):
                 while True:
                    uw2.append(0)
                    if len(uw1) == len(uw2):
                        break
        if uw1 < uw2:
            return -1 
        if uw1 > uw2:
            return 1
        if uw1 == uw2:
            return 0
ob1 = Solution()
print(ob1.compareVersion( "0.1",  "1.1"))
