class Solution {
    public int[] productExceptSelf(int[] nums) {
        int totalProduct = 1;
        int zeroCount = 0;
        for (int i : nums) {
            if (i == 0) {
                zeroCount++;
            }
            else {
                totalProduct *= i;
            }
        }

        if (zeroCount > 1) {
            return new int[nums.length];
        }
        int[] returnArr = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (zeroCount == 0) {
                returnArr[i] = totalProduct / nums[i];
            }
            else if (nums[i] == 0) {
                returnArr[i] = totalProduct;
            }
        }

        return returnArr;
    }
}  
