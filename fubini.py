def bell_number(num: int) -> int:
    dp = [[0] * num for _ in range(num)]
    dp[0][0] = 1
    for n in range(1, num):
        for k in range(num):
            dp[n][k] = (k + 1) * (dp[n - 1][k - 1] + dp[n - 1][k])
    return sum(dp[-1])


print([bell_number(i) for i in range(1, 11)])