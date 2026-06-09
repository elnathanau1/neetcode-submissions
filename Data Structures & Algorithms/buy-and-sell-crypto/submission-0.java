class Solution {
    public int maxProfit(int[] prices) {
        int buyIndex = 0;
        int sellIndex = 1;
        int maxProfit = 0;
        while (sellIndex < prices.length) {
            int profit = prices[sellIndex] - prices[buyIndex];
            maxProfit = Math.max(profit, maxProfit);
            if (prices[buyIndex] > prices[sellIndex]) {
                buyIndex = sellIndex;
                sellIndex++;
            } else  {
                sellIndex++;
            }
        }
        return maxProfit;
    }
}
