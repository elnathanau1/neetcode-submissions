class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int reverse = target - nums[i];
            if (numToIndex.containsKey(reverse)) {
                return new int[]{numToIndex.get(reverse), i};
            }
            numToIndex.put(nums[i], i);
        }
        return new int[2];
    }
}
