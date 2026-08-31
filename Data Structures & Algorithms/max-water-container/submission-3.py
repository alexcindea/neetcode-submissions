class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        f_ptr = 0
        e_ptr = len(heights) - 1
        max_container = 0

        while f_ptr < e_ptr: 
            minH = min(heights[f_ptr], heights[e_ptr])
            container_size = minH * (e_ptr - f_ptr)
            
            if max_container < container_size:
                max_container = container_size
            if minH == heights[f_ptr]:
                f_ptr += 1
            else:
                e_ptr -= 1
        
        return max_container
            



        