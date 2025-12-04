import numpy as np

def prepare_file(filename):
    file = open(filename)
    new_lines = []
    for line in file:
        separator = " "
        new_lines.append(separator.join(line))
    print(new_lines)
    file = open(filename, 'w')
    file.writelines(new_lines)
    file.close()




def paper_rolls_part1(filename):

    scroll_counter = 0
    grid = np.loadtxt(filename, dtype = str)

    for index, elem in np.ndenumerate(grid):
        if elem == '@':
            start_x_axis = 0 if index[0] == 0 else index[0] - 1
            start_y_axis = 0 if index[1] == 0 else index[1] - 1
            end_x_axis = grid.shape[0] if index[0] >= grid.shape[0]-2 else index[0]+2
            end_y_axis = grid.shape[1] if index[1] >= grid.shape[1]-2 else index[1] + 2
            subgrid = grid[start_x_axis: end_x_axis , start_y_axis : end_y_axis]
            itemindex = np.where(subgrid == '@')
            if len(itemindex[0]) <= 4:
                scroll_counter += 1
    return scroll_counter

def paper_rolls_part2(filename):

    scroll_counter = 0
    grid = np.loadtxt(filename, dtype = str)
    whole_grid_indexes = []
    while True:
        findings_counter = 0
        for index, elem in np.ndenumerate(grid):
            if elem == '@':
                start_x_axis = 0 if index[0] == 0 else index[0] - 1
                start_y_axis = 0 if index[1] == 0 else index[1] - 1
                end_x_axis = grid.shape[0] if index[0] >= grid.shape[0]-2 else index[0]+2
                end_y_axis = grid.shape[1] if index[1] >= grid.shape[1]-2 else index[1]+2
                subgrid = grid[start_x_axis: end_x_axis , start_y_axis : end_y_axis]
                itemindex = np.where(subgrid == '@')
                if len(itemindex[0]) <= 4:
                    scroll_counter += 1
                    whole_grid_indexes.append(index)
                    findings_counter += 1
        if findings_counter == 0:
            break
        for index in whole_grid_indexes:
            grid[index] = '.'
    return scroll_counter


#prepare_file("Day4_input")
#print(paper_rolls_part1('Day4_input'))
print(paper_rolls_part2('Day4_input'))