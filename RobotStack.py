import sys

# Function to calculate the number of ways to distribute robots into stacks
def distribute_robots(b, n, k, memo):
    if b == 0:
        return 1
    if n <= 0 or k <= 0:
        return 0
    if (b, n, k) in memo:
        return memo[(b, n, k)]
    
    ways = 0
    for i in range(min(k, b) + 1):
        ways += distribute_robots(b - i, n - 1, k, memo)
    
    memo[(b, n, k)] = ways
    return ways

# Read input from a text file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        instances = [list(map(int, line.strip().split())) for line in lines]
    return instances

if len(sys.argv) != 2:
    print("Usage: python RobotStack.py input.txt")
    sys.exit(1)

input_file = sys.argv[1]
instances = read_input(input_file)
for instance in instances:
    b, n, k = instance
    memo = {}
    ways = distribute_robots(b, n, k, memo)
    print(f"({b},{n},{k}) = {ways}")
