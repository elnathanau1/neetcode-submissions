class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seenNums = new HashSet<>();
        for (int i : nums) {
            if (seenNums.contains(i)) {
                return true;
            }
            seenNums.add(i);
        }
        return false;
    }
}