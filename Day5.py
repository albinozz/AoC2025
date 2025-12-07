

def get_fresh_part1(filename):
    file = open(filename)
    ranges = []
    fresh =0
    before_separator = 1
    for line in file:
        if line == "\n":
            for x in ranges:
                x[0] = int(x[0])
                x[1] = int(x[1])
            before_separator = 0
        if before_separator == 1:
            line = line.strip('\n')
            single_range = line.split('-')
            ranges.append(single_range)
        else:
            line = line.strip('\n')
            if line == '':
                continue
            for x in ranges:
                if int(line) in range(x[0], x[1]+1):
                    fresh += 1
                    break
    return fresh

def get_fresh_part2(filename):
    file = open(filename)
    ranges = []
    fresh =0
    for line in file:
            line = line.strip('\n')
            single_range = line.split('-')
            single_range[0] = int(single_range[0])
            single_range[1] = int(single_range[1])
            ranges.append(single_range)
    merged_ranges = []
    ranges.sort(key=lambda x: (x[0], x[1]))
    x_iter = 0
    while x_iter < len(ranges):
        y_iter = x_iter + 1
        start = ranges[x_iter][0]
        end = ranges[x_iter][1]
        if y_iter >= len(ranges):
            merged_ranges.append((start, end))
            break
        while end >= ranges[y_iter][0]:
            start = min(start , ranges[y_iter][0])
            end = max(end, ranges[y_iter][1])
            y_iter += 1
            if y_iter == len(ranges):
                break
        x_iter = y_iter
        merged_ranges.append((start, end))

    for x in merged_ranges:
        fresh += x[1] - x[0] + 1
    return fresh
print(get_fresh_part2("Day5_input"))