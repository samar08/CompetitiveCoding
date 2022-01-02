class Solution {
    public int maxCoins(int[] nums) {
        //bottomUp Approach
        int[][] dp = new int[nums.length][nums.length];
        
        for(int len = 1; len <= nums.length; len++){
            for(int i = 0; i < nums.length + 1 - len; i++){
                
                int leftBoundary = (i != 0)? nums[i - 1]: 1;
                int rightBoundary = (i + len < nums.length)? nums[i + len]: 1;
                
                int k = i + len - 1;
                for(int j = i; j <= k; j++){
                    //in the range of balloons from i to k, picking the balloon at jth
                    //idx to be the last balloon to burst
                    dp[i][k] = Math.max(dp[i][k],
                                        leftBoundary * nums[j] * rightBoundary + 
                                        (j > 0? dp[i][j - 1]: 0) + 
                                        (j < nums.length - 1? dp[j + 1][k]: 0));
                }
            }
        }
        return dp[0][nums.length - 1];
    }
}