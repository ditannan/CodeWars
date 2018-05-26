def expressionsMatter(a, b, c):
    input_list = sorted([a, b, c])

    if input_list[0] > 1:
        return input_list[0] * input_list[1] * input_list[2]
    elif input_list[0] == 1 and input_list[2] > 1:
        return (input_list[0] + input_list[1]) * input_list[2]
    else:
        return 3


expressionsMatter(1, 2, 3)
