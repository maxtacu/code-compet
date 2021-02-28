import sys
# to execute:
# cat test.txt | python main.py

# read the input
input_data = sys.stdin.readlines()

# remove newline characters from the list
for line in input_data:
    input_data[input_data.index(line)] = line.rstrip("\n")

# get and remove the first element from the list that contains number of tests
number_of_tests = int(input_data.pop(0))

# create an empty matrix dict
matrix = {}

for test_set in range(number_of_tests):
    # create an empty internal matrix that will iterate through matrix elements according to matrix size
    internal_matrix = []
    # get the internal matrix size and remove the element from the list
    matrix_size = int(input_data.pop(0))
    for matrix_element in range(matrix_size):
        # split elements by space and append matrix elements to the internal matrix 
        internal_matrix.append(input_data[matrix_element].split())
    # append to matrix dict the 'internal matrix' as value and 'test set' as key
    matrix[test_set] = internal_matrix
    # remove internal matrix that was extracted
    del input_data[:matrix_size]


# convert matrix string elements into integer
for test_set in range(number_of_tests):
    internal_matrix = []
    for matrix_element in matrix[test_set]:
        matrix_element = [int(x) for x in matrix_element]
        internal_matrix.append(matrix_element)
    matrix[test_set] = internal_matrix


def calculate_trace(matrix):
    trace = 0
    for index in range(len(matrix)):
        for _ in range(len(matrix)):
            trace = trace + matrix[index][index]
            break
    return trace


# calculate rows that have repeated values
def repeated_in_rows(matrix):
    rows_with_repeated_values = 0
    for row in matrix:
        if len(row) != len(set(row)):
            rows_with_repeated_values += 1
    return rows_with_repeated_values


# calculate columns that have repeated values
def repeated_in_columns(matrix):
    columns_with_repeated_values = 0
    for row in range(len(matrix)):
        new_list = []
        for column in range(len(matrix)):
            new_list.append(matrix[column][row])
        if len(new_list) != len(set(new_list)):
            columns_with_repeated_values += 1
    return columns_with_repeated_values


def output(x, k, r, c):
    print(f"Case #{x}: {k} {r} {c}")


for test_set in range(len(matrix)):
    output(test_set+1, calculate_trace(matrix[test_set]), repeated_in_rows(matrix[test_set]), repeated_in_columns(matrix[test_set]))