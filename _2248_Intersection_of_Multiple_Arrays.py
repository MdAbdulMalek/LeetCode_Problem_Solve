class Solution:
    def intersection(self, nums):
        s = sorted(nums, key=len)
        ans = list(s[0])
        for i in s[1:]:
            final = []
            for zz in i:
                if zz in ans: 
                    final.append(zz)
                    ans.remove(zz)
            ans = final
        return sorted(ans)

ob1 = Solution()
print(ob1.intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))
