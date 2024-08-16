class Solution:
    def largestTriangleArea(self, points) -> float:
        area=0
        for i in range(len(points)-2):
        
            x1,y1=points[i][0],points[i][1]
            for left in range(i+1,len(points)-1):
                x2,y2=points[left][0],points[left][1]
                for right in range(i+2,len(points)):
                    x3,y3=points[right][0],points[right][1]
                    newarea=0.5*abs(
                        (x1*(y2-y3))+
                        (x2*(y3-y1))+
                        (x3*(y1-y2)))
                    area=max(area,newarea)
        return area