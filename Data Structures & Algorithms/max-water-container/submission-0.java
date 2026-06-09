class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = Integer.MIN_VALUE;
        while (left <= right) {
            int width = right - left;
            int height = Math.min(heights[left], heights[right]);
            maxArea = Math.max(width * height, maxArea);

            if (heights[left] > heights[right]) {
                right--;
            }
            else {
                left++;
            }
        }
        
        return maxArea;
    }
}
