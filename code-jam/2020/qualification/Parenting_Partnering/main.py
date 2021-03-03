import sys

INPUT_DATA = sys.stdin.readlines()

for line in INPUT_DATA:
    INPUT_DATA[INPUT_DATA.index(line)] = line.rstrip("\n")

TEST_CASES = int(INPUT_DATA.pop(0))

print(INPUT_DATA)


def output(x, y):
    print(f"Case #{x}: {y}")