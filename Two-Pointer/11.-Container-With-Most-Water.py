class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_area=0

        while l<r:
            area=(r-l)*min(height[l],height[r])
            max_area=max(area,max_area)

            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                r-=1
                #l+=1 update any of the pointer when equal
        return max_area

            
            