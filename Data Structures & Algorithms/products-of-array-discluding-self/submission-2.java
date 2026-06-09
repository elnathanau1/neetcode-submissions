class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        prefix[0] = 1;
        suffix[nums.length - 1] = 1;
        for (int i = 1; i < nums.length; i++) {
            int revIndex = nums.length - i - 1;
            prefix[i] = prefix[i-1] * nums[i-1];
            suffix[revIndex] = suffix[revIndex+1] * nums[revIndex+1];
        }

        /**
        [1,2,4,6]
        pre: [1,1,2,8]
        suf: [48,24,6,1]
        */

        int[] answer = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            answer[i] = prefix[i] * suffix[i];
        }
        return answer;
    }

}  
