class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // key constraint: strs[i] is made up of lowercase English letters.
        // This means that we only ever have 26 characters to account for

        Map<String, List<String>> anagrams = new HashMap<>();
        for (String s: strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (anagrams.containsKey(key)) {
                anagrams.get(key).add(s);
            }
            else {
                List<String> value = new ArrayList<String>();
                value.add(s);
                anagrams.put(key, value);
            }
        }

        return new ArrayList<>(anagrams.values());

    }
}
