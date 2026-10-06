import time

n = int(input("Enter number of coin denominations: "))

coins = []
print("Enter the coin denominations:")
for i in range(n):
    coins.append(int(input()))

amount = int(input("Enter the amount: "))

start_time = time.perf_counter()

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

end_time = time.perf_counter()

if dp[amount] == float('inf'):
    print("Amount cannot be formed using the given coins.")
else:
    print("Minimum number of coins:", dp[amount])

print("Execution Time:", end_time - start_time, "seconds")

print("Time Complexity: O(n × amount)")
print("Space Complexity: O(amount)")
