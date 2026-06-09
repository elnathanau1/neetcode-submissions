class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> characterCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            characterCount.put(c, characterCount.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            if (characterCount.keySet().contains(c)) {
                if (characterCount.get(c) == 1) {
                    characterCount.remove(c);
                } else {
                    characterCount.put(c, characterCount.get(c) - 1);
                }
            } else { 
                return false; 
            }
        }

        return characterCount.keySet().size() == 0;
    }
}
