class Solution:
    def trap(self, height):
        n = len(height)
        left = [0]*n
        right = [0]*n
        sum = 0

        left[0] = height[0]
        for i in range( 1, n):
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i]);

        for i in range(0, n):
            sum += min(left[i], right[i]) - height[i]
 
        return sum

ob1 = Solution()
print(ob1.trap([0,1,0,2,1,0,1,3,2,1,2,1]))