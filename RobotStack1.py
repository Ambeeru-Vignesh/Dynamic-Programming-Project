# Iterative Approach

def distribute_robots(b, n, k):
    # Create a 3D array dp[b+1][n+1][k+1]
    dp = [[[0 for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(b + 1)]

    # Initialize base cases
    for i in range(b + 1):
        for j in range(n + 1):
            for x in range(k + 1):
                if i == 0:
                    dp[i][j][x] = 1
                elif j <= 0 or x <= 0:
                    dp[i][j][x] = 0
                else:
                    dp[i][j][x] = 0
                    # Calculate dp[i][j][x] using the recurrence relation
                    for y in range(min(x, i) + 1):
                        dp[i][j][x] += dp[i - y][j - 1][x]

    return dp[b][n][k]

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        instances = [list(map(int, line.strip().split())) for line in lines]
    return instances


input_file = "input.txt"  # Replace with your input file name
instances = read_input(input_file)
for instance in instances:
    b, n, k = instance
    ways = distribute_robots(b, n, k)
    print(f"({b},{n},{k}) = {ways}")