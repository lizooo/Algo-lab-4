import string
import numpy

input_file = numpy.genfromtxt("input.txt", dtype=None, delimiter=1, encoding=None)
width = int(numpy.genfromtxt("input.txt", dtype=None, delimiter=' ', encoding=None, usecols=0)[0])
height = int(numpy.genfromtxt("input.txt", dtype=None, delimiter=' ', encoding=None, usecols=1, max_rows=1))

d = dict((key, [0]*width) for key in string.ascii_lowercase)
counter = dict((key, [0]*width) for key in string.ascii_lowercase)
input = numpy.delete(input_file, 0, axis=0)


def get_input(input):
    modified_input = numpy.transpose(input)
    for middle_rows in modified_input[-1:]:
        middle_rows[1:-1] = ""
    return modified_input


def find_paths_for_elements_in_last_column(modified_input):
    column_index = 0
    for column in modified_input:
        element_index = 0
        for element in column:
            if element:
                d[element][column_index] += 1
                if column_index > 0 and element != modified_input[column_index - 1][element_index]:
                    counter[element][column_index] += 1
                    d[element][column_index] *= d[modified_input[column_index - 1][element_index]][column_index - 1]
            element_index += 1
        for element in set(column):
            if element and column_index > 0:
                if sum((d[element])[:column_index]) != 0:
                    d[element][column_index] *= sum((d[element])[:column_index])
                    d[element][column_index] += counter[element][column_index]
        column_index += 1
    print(d)
    return d


def calculate_result():
    unique_routes = 0
    for element in d:
        unique_routes += (d[element][-1:][0])
    return unique_routes


def print_result():
    with open("output.txt", "w" ) as output_file:
        output_file.write(str(calculate_result()))


if __name__ == "__main__":
    modified_input = get_input(input)
    find_paths_for_elements_in_last_column(modified_input)
    print_result()

