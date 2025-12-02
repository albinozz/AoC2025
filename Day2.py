def get_ids_part1(filename):
    file = open(filename)
    sum_of_ids = 0
    for line in file:
        list_of_ids = line.split(',')
        for x in list_of_ids:
            range_values = x.split('-')
            for num in range(int(range_values[0]), int(range_values[1])+1):
                string_id = str(num)
                if len(string_id)%2 == 0:
                    if string_id[:int(len(string_id)/2)] == string_id[int(len(string_id)/2):]:
                        sum_of_ids  += num
    return sum_of_ids

def get_ids_part2(filename):
    file = open(filename)
    sum_of_ids = 0
    for line in file:
        list_of_ids = line.split(',')
        for x in list_of_ids:
            range_values = x.split('-')
            for num in range(int(range_values[0]), int(range_values[1])+1):
                string_id = str(num)
                for split_len in range(1, len(string_id)):
                    if len(string_id) % split_len == 0: #checking if substrings would be even
                        sub = [string_id[split_len*i:(split_len - 1 + split_len*i+1)] for i in range(int(len(string_id)/split_len))]
                        if len(set(sub)) == 1: #are all values the same
                            sum_of_ids += num
                            break
    return sum_of_ids


print(get_ids_part2("Day2_input"))