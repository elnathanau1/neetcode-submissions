class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return 1;

        Arrays.sort(nums);
        int curr = 1;
        int top = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1] - 1) curr++;
            else if (nums[i] != nums[i+1]) curr = 1;
            top = Math.max(top, curr);
        }

        return top;
    }
}
