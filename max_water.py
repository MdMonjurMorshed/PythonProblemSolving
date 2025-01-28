
#11.Container With Most Water
class Solution(object):
    def maxArea(self, height):
        
        max_water = 0
        l = 0
        r = len(height)-1
        while l<r:

           calculation = min(height[l],height[r])*(r-l)
           if calculation > max_water:
                max_water = calculation
           if height[l] < height[r]:
                l+=1         
           else:
                r-=1

        return max_water            
                

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))


            
