def count_ways(x, y):
    if x < y:
        return 0
    if x == y or y == 0:
        return 1

    dp = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0 or i < j:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[x][y]

def main():
    n = int(input("Enter the number of test cases: "))
    test_cases = [list(map(int, input().split())) for _ in range(n)]

    for case in test_cases:
        result = count_ways(case[0] + case[1], case[1])
        print(result)

if __name__ == "__main__":
    main()
