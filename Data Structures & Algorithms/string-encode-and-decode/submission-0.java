// recommended time complexity O(m), space O(m+n)
// m is sum of length of all strings, n is number of strings
class Solution {

    // Relevant info: 
    // up to 100 strings
    // each string up to 200 characters
    // each string only has UTF-8 characters

    /**
    idea 1: 
    first 2 characters encode number of strings (n)
    next 3 * n characters encode the length of each string
    remaining characters are just the strings
    */
    public String encode(List<String> strs) {
        String encoded = "";
        for (String s : strs) {
            encoded += String.format("%03d", s.length());
            encoded += s;
        }

        return encoded;
    }

    public List<String> decode(String str) {
        List<String> returnList = new ArrayList<>();
        int index = 0;
        while (index < str.length()) {
            int length = Integer.parseInt(str.substring(index, index + 3));
            String nextWord = str.substring(index+3, index + 3 + length);
            returnList.add(nextWord);
            index = index + 3 + length;
        }

        return returnList;
    }
}
