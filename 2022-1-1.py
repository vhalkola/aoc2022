result = 0
    current_total = 0

    for line in input_list:
        if line == '':
            result = max(result, current_total)
            current_total = 0
        else:
            current_total += int(line)