class Solution:
      def findMinArrowShots(self, points: List[List[int]]) -> int:
            if not points:
                  return 0
            points.sort(key=lambda x: x[1])
            arrows = 1
            first_end = points[0][1]
            for start, end in points:
                  if first_end < start:
                  arrows += 1
                  first_end = end
            return arrows
      
      
      
      
###### another solutio way which is more optimal 


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        #start, end = points[0][0], points[0][1]
        end = points[0][1]
        arrow = 1
        
        for i in range(1, len(points)):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]
        return arrow