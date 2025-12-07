import re


def tachyon_counter(filename):
    file = open(filename)
    beam_pos = []
    filelines = []
    for line in file:
        filelines.append(line)
    beam_pos.append((0,filelines[0].find('S')))
    beam_pos_list = [[(beam_pos[0][0], beam_pos[0][1],1)]]
    for y in range(1, len(filelines)):

        spliters_pos = [m.start() for m in re.finditer(r'\^', filelines[y])]
        if not spliters_pos:
            continue
        beam_pos_new = beam_pos.copy()

        for x in beam_pos:
            if x[1] in spliters_pos:
                beam_pos_new.append((x[1],x[1]-1,0))
                beam_pos_new.append((x[1],x[1]+1,0))
                beam_pos_new.remove(x)
            else:
                beam_pos_new.append((x[1], x[1],0))
                beam_pos_new.remove(x)
        beam_pos = beam_pos_new.copy()
        beam_pos = list(set(beam_pos))
        beam_pos_list.append(beam_pos)

    for line_num in range(1, len(beam_pos_list)):
        for y_pos, y in enumerate(beam_pos_list[line_num]):
            hit_counter = 0
            for x in beam_pos_list[line_num-1]:
                if x[1] == y[0]:
                    hit_counter += x[2]
            temp_list = list(y)
            temp_list[2] = hit_counter
            y = tuple(temp_list)
            beam_pos_list[line_num][y_pos] = y

    total = 0
    for line_num in range(1, len(beam_pos_list)):
        for x in beam_pos_list[line_num - 1]:
            hit_counter = 0
            for y_pos, y in enumerate(beam_pos_list[line_num]):
                if x[1] == y[0]:
                    hit_counter = 1
                    break
            if hit_counter == 0:
                total += x[2]
    for x in beam_pos_list[-1]:
        total += x[2]
    return total


print(tachyon_counter("Day7_input"))