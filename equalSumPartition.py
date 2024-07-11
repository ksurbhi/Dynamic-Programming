class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        print(arr_sum)
        if arr_sum % 2 != 0:
            return False
        else: 
            arr_sum = arr_sum // 2
            return self.subsetSum(nums,arr_sum,len(nums))
    def subsetSum(self, arr:List[int], sum_:int ,n:int):
        # Create a DP table with dimensions (n+1) x (sum_+1)
        dp = [[False for x in range (sum_+1)] for x in range(n+1)]
        # Initialize the first column as True because a sum of 0 can always be achieved with an empty subset
        for i in range(n + 1):
            dp[i][0] = True
        # fill the dp table
        for i in range(1,n+1):
            for j in range(1,sum_+1):
                if arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][sum_]

            
            
