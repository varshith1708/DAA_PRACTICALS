def matrix_chain_order(p):
    n = len(p) - 1

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        p[i] * p[k + 1] * p[j + 1])

                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]

n = int(input("Enter number of matrices: "))

p = []

print("Enter dimensions:")
for i in range(n + 1):
    p.append(int(input(f"p[{i}] = ")))

result = matrix_chain_order(p)

print("Minimum number of scalar multiplications:", result)
