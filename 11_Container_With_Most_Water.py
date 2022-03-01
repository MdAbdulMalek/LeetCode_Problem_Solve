class Solution:
    def maxArea(self, height):
            left = 0
            right = len(height)-1
            maximum = 0
            
            while left < right:
                water = (right-left) * min(height[left], height[right])
                if water > maximum:
                    maximum = water
                if height[left] < height[right]:
                    left+=1
                else:
                    right-=1
            return maximum
ob1 = Solution()
print(ob1.maxArea([1,8,6,2,5,4,8,3,7]))
