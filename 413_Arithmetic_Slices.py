class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0
        sum = 0
        res = [nums[0], nums[1]]
        d = nums[0] - nums[1]
        i=1
        while True:
            dif = nums[i] - nums[i+1]
            if dif == d:
                res.append(nums[i+1])
                i = i + 1
            else:
                if len(res) >= 3:
                    l = [res[y : z] for y in range(len(res)) for z in range(y + 1, len(res) + 1)]
                    for pp in l:
                        if len(pp) >=3:
                            sum = sum + 1
                    l.clear()
                    res.clear()
                res.clear()
                d = nums[i] - nums[i+1]
                res = [nums[i], nums[i+1]]
                i = i + 1
            if i == len(nums)-1:
                break
        l = [res[y : z] for y in range(len(res)) for z in range(y + 1, len(res) + 1)]
        for pp in l:
            if len(pp) >=3:
                sum = sum + 1
        return sum
ob1=Solution()
print(ob1.numberOfArithmeticSlices([1,2,3,8,9,10]))
