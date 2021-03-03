import sys

input_data = sys.stdin.readlines()

# remove newline characters from the list and convert elements into integer
for line in input_data:
    input_data[input_data.index(line)] = int(line.rstrip("\n"))

TEST_CASES = input_data.pop(0)

print(input_data)
print(TEST_CASES)


def output(x, y):
    print(f"Case #{x}: {y}")