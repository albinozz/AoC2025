import sys


def get_code_part1():
    dial_position = 50
    zero_counter = 0
    file = open("Day1_input")

    for line in file:
        if line[0] == "L":
            dial_position = (dial_position - int(line[1:]))%100
        elif line[0] == "R":
            dial_position = (dial_position + int(line[1:]))%100
        else:
            sys.exit("Error in data")
        if dial_position == 0:
            zero_counter += 1
    return zero_counter

def get_code_part2():
    dial_position = 50
    zero_counter = 0
    file = open("Day1_input")

    for line in file:
        if line[0] == "L":
            new_dial_position = dial_position - int(line[1:])
            base = new_dial_position // 100
            if dial_position == 0 and new_dial_position % 100 != 0:
                zero_counter += abs(base) - 1
            else:
                zero_counter += abs(base)
            if dial_position != 0 and new_dial_position% 100 == 0:
                zero_counter+=1
            dial_position = new_dial_position % 100

        elif line[0] == "R":
            new_dial_position = dial_position + int(line[1:])
            base = new_dial_position // 100
            zero_counter += base
            dial_position = new_dial_position % 100
        else:
            sys.exit("Error in data")

        #print( line, dial_position, zero_counter)
    return zero_counter

#print(get_code_part1())
print(get_code_part2())
