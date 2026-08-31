class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f_p = 0
        e_p = len(heights) - 1
        max_container = 0
        while f_p < e_p: 
            container_size = min(heights[f_p], heights[e_p]) * (e_p - f_p)
            if max_container < container_size:
                max_container = container_size

            if heights[f_p] > heights[e_p]:
                e_p -= 1
            else:
                f_p += 1
        return max_container


        