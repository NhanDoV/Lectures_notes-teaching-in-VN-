from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_sq_area = 0

        n = len(bottomLeft)
 
        for i in range(n):
            for j in range(i + 1, n):
 
                x1, y1 = bottomLeft[i]
                x2, y2 = topRight[i]

                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                inter_x1, inter_y1 = max(x1, x3), max(y1, y3)
                inter_x2, inter_y2 = min(x2, x4), min(y2, y4)

                if inter_x1 < inter_x2 and inter_y1 < inter_y2:

                    inter_width = inter_x2 - inter_x1
                    inter_height = inter_y2 - inter_y1

                    side = min(inter_width, inter_height)
                    max_sq_area = max(max_sq_area, side * side)

        return max_sq_area