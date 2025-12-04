def turn_batteries_part1(filename):
    file = open(filename)
    total_joltage = 0

    for line in file:
        first_search = line[:-2]
        first_digit = max(first_search)
        first_digit_pos = line.index(first_digit) + 1
        second_digit = max(line[first_digit_pos:])
        total_joltage += int(first_digit)*10 + int(second_digit)
    return total_joltage

def turn_batteries_part2(filename):
    file = open(filename)
    total_joltage = 0

    for line in file:
        line = line.rstrip('\n')
        digits = []
        digit_pos = 0
        for x in range(1,13):
            if digit_pos > len(line)-12 + 1 +x:
                print(digit_pos, x)
                digits.append(line[digit_pos:])
                break
            first_search = line[digit_pos:(len(line)-12)+x]
            digits.append(max(first_search))
            if len(digits) == 12:
                break
            digit_pos = first_search.index(digits[x-1]) + 1 + digit_pos
        print(digits)
        total_joltage += int(''.join(map(str, digits)))

    return total_joltage

print(turn_batteries_part2("Day3_input"))