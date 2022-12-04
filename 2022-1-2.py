result = 0
    current_total = 0
    top_three = []

    for line in input_list:
        if line == '':
            top_three.append(current_total)
            top_three.sort(reverse=True)
            top_three = top_three[:3]
            current_total = 0
        else:
            current_total += int(line)

    result = sum(top_three)