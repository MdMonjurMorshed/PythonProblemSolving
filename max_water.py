class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        r1=len(height)-1
        r2 = len(height)-1
        l = 0
        while r1>=1:

            if r1==l:
                l=0
                r1-=1
            # min_value1 = min(height[i],height[r2])
            min_value2 = min(height[l],height[r1])

          
            # calculation1 = min_value1*(r2-i)
            calculation2 = min_value2*(r1-l)
            l+=1
            # if max_water < calculation1:
            #     max_water = calculation1
            if max_water < calculation2:
                max_water = calculation2

            

        return max_water