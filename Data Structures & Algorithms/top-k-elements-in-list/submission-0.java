class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int i : nums) {
            freqMap.putIfAbsent(i, 0);
            freqMap.put(i, freqMap.get(i) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> entry1, Map.Entry<Integer, Integer> entry2) {
                return -1 * Integer.compare(entry1.getValue(), entry2.getValue());
            }
        });

        for (Map.Entry entry : freqMap.entrySet()) {
            minHeap.add(entry);
        }

        int[] returnArray = new int[k];
        for (int i = k-1; i >= 0; i--) {
            returnArray[i] = minHeap.poll().getKey();
        }

        return returnArray;
    }
}
