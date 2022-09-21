class Solution:
    def findOriginalArray(self, changed):
        f_len = len(changed)
        zc= changed.count(0)
        if f_len%2 != 0 or zc%2 != 0:
            return []
        final = []
        emp = []
        changed.sort()
        for i in changed:
            val = i*2
            if val in changed and i in changed:
                final.append(i)
                emp.append(1)
                changed.remove(val)
        if len(emp) == (f_len//2):
            return final
        else:
            return []
object1 = Solution()
print(object1.findOriginalArray([0,0]))
