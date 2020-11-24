import string
import numpy

input_file = numpy.genfromtxt("input.txt", dtype=None, delimiter=1, encoding=None)
width = int(numpy.genfromtxt("input.txt", dtype=None, delimiter=' ', encoding=None, usecols=0)[0])
height = int(numpy.genfromtxt("input.txt", dtype=None, delimiter=' ', encoding=None, usecols=1, max_rows=1))


input = numpy.delete(input_file, 0, axis=0)


def get_input(input):
    '''

    :param input: matrix that consists of lowercase a-z letters
    :return: transposed matrix where in last column all letters bu exits are replaced with ""
    '''
    modified_input = numpy.transpose(input)
    for middle_rows in modified_input[-1:]:
        middle_rows[1:-1] = ""
    return modified_input


def find_paths_for_elements_in_last_column(modified_input, width):
    '''

    :param modified_input: transposed matrix where in last column all letters bu exits are replaced with ""
    :param width: number of columns
    :return: dictionary where lowercase a-z letters are keys and values are lists with len that is equal
    to number of columns

    e.g
    alphabetic_dict = [         ...
                        'a' : [ 1, 5, 6, 12 ]
                              ...           ]

    In list with key 'a' each number indicates number of unique paths to that number in column with same index
    as the list index. In row 0 there's 1 unique path to a`s of that column
                       In row 1 theres 5 unique paths to a`s of that column
    '''
    # initialize dictionary that will store unique routes to each letter in each column
    alphabetic_dict = dict((key, [0] * width) for key in string.ascii_lowercase)
    # initialize dictionary that will store information about previous letter
    matching_nghbr = dict((key, [0] * width) for key in string.ascii_lowercase)
    column_index = 0
    # iterate through initial matrix from left to right moving a column at a time
    for column in modified_input:
        element_index = 0
        for element in column:
            if element:
                # indicate in the alphabetic_dict that letter has occurred in current column
                alphabetic_dict[element][column_index] += 1
                # if letter in previous column differs from current add that letter`s unique paths to current
                # letter`s unique paths
                if column_index > 0 and element != modified_input[column_index - 1][element_index]:
                    matching_nghbr[element][column_index] += 1
                    alphabetic_dict[element][column_index] *= alphabetic_dict[modified_input[column_index - 1][element_index]][column_index - 1]
            element_index += 1
        # for each unique letter in current column add sum of unique paths to this letter
        # from each of the previous columns
        # if unique letter in current column had letter in previous column that wasn't the same then add that letter`s
        # unique paths to current letter unique paths
        for element in set(column):
            if element and column_index > 0:
                if sum((alphabetic_dict[element])[:column_index]) != 0:
                    alphabetic_dict[element][column_index] *= sum((alphabetic_dict[element])[:column_index])
                    alphabetic_dict[element][column_index] += matching_nghbr[element][column_index]
        column_index += 1
    return alphabetic_dict


def calculate_result(d):
    '''

    :param d: dictionary that stores unique routes to each letter in each column
    :return: number of unique routes to exit letters
    '''
    unique_routes = 0
    for element in d:
        unique_routes += (d[element][-1:][0])
    return unique_routes


def print_result(d):
    '''
    :param d: dictionary that stores unique routes to each letter in each column
    prints result into output.txt file
    '''
    with open("output.txt", "w") as output_file:
        output_file.write(str(calculate_result(d)))


if __name__ == "__main__":
    modified_input = get_input(input)
    result_dict = find_paths_for_elements_in_last_column(modified_input, width)
    print_result(result_dict)



