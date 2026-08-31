class Solution {
public:
    int maxArea(vector<int>& heights) {
        int f_ptr = 0;
        int e_ptr = static_cast<int>(heights.size()) - 1;
        int max_container = 0;

        while (f_ptr < e_ptr) {
            int minH = min(heights[f_ptr], heights[e_ptr]);
            int container_size = minH * (e_ptr - f_ptr);

            if (max_container < container_size) {
                max_container = container_size;
            }
            if (minH == heights[f_ptr]) {
                f_ptr++;
            } else {
                e_ptr--;
            }
        }

        return max_container;
    }
};