class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        m,n = len(pizza), len(pizza[0])
        prefixSum = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                prefixSum[i][j] = prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i+1][j+1] + (1 if pizza[i][j]=='A' else 0)
        
        dp = [[[0]*(k+1) for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if prefixSum[i][j]>0:
                    dp[i][j][1]=1
        for p in range(2,k+1):
            for i in range(m):
                for j in range(n):
                    for nc in range(j+1,n):
                        if prefixSum[i][j]-prefixSum[i][nc]>0:
                            dp[i][j][p]=(dp[i][j][p] + dp[i][nc][p-1])%MOD
                    for nr in range(i+1,m):
                        if prefixSum[i][j]-prefixSum[nr][j]>0:
                            dp[i][j][p]=(dp[i][j][p] + dp[nr][j][p-1])%MOD

        
        return (dp[0][0][k])%MOD
