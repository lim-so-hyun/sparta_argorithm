input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    shift_num = [0] * 2

    if string[0] == 0:
        shift_num[0] += 1
    else:
        shift_num[1] += 1

    for n in range(len(string) - 1):
        if string[(n + 1)]=='1' and string[n]=='0':
            shift_num[1] += 1
        if string[(n + 1)]=='0' and string[n]=='1':
            shift_num[0] += 1

    zero_to_one = shift_num[0]
    one_to_zero = shift_num[1]
    return min(zero_to_one, one_to_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
