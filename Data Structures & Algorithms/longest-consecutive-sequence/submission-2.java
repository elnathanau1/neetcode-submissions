class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return 1;

        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            set.add(i);
        }
        
        List<Integer> starts = new ArrayList<>();
        for (int i : nums) {
            if (!set.contains(i-1)) {
                starts.add(i);
            }
        }

        int total = 1;
        int curr = 1;
        for (int start : starts) {
            curr = 1;
            int temp = start;
            while (set.contains(temp + 1)) {
                temp++;
                curr++;
                total = Math.max(total, curr);
            }
        }

        return total;

    }
}
