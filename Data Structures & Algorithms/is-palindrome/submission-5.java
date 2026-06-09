class Solution {
    public boolean isPalindrome(String s) {
        String s2 = s.toLowerCase();

        StringBuilder sb = new StringBuilder();
        StringBuilder reversed = new StringBuilder();
        for (char c : s2.toCharArray()) {
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                sb.append(c);
                reversed.insert(0, c);
            }
        }

        return sb.toString().equals(reversed.toString());
    }
}
