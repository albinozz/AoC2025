import numpy as np


def problems_part1(filename):

    counter = 0
    grid = np.loadtxt(filename, dtype = str)
    for xindex in range(grid.shape[1]):
        if grid[-1][xindex] == '+':
            local_result = 0
            for yindex in range(grid.shape[0] -1):
                local_result += int(grid[yindex][xindex])
        else:
            local_result = 1
            for yindex in range(grid.shape[0] - 1):
                local_result *= int(grid[yindex][xindex])
                if local_result == 0:
                    break
        counter += local_result
    return counter

def problems_part2(filename):
    filelines = []
    max_size = 0
    file = open(filename)
    for line in file:
        line = line.strip('\n')
        filelines.append(line)
    for line in filelines:
        if len(line) > max_size:
            max_size = len(line)

    final_values = 0
    local_values = []
    math_type = ''

    for pos in range(max_size):
        all_empty = 1
        multiplyer = 1
        counter = 0
        if pos < len(filelines[-1]):
            if filelines[-1][pos] == '+':
                math_type = '+'
            elif filelines[-1][pos] == '*':
                math_type = '*'

        for y_pos in range(len(filelines)-2, -1, -1):
            if pos < len(filelines[y_pos]):
                if filelines[y_pos][pos] != ' ':
                    all_empty = 0
                    counter += int(filelines[y_pos][pos])*multiplyer
                    multiplyer *= 10

        if all_empty == 0:
            local_values.append(counter)

        if all_empty == 1 or pos == max_size -1:
            if math_type == '+':
                value = 0
                for x in local_values:
                    value += x
            elif math_type == '*':
                value = 1
                for x in local_values:
                    value *= x
            final_values += value
            value = 0
            local_values = []
    return final_values
print(problems_part2("Day6_input"))

