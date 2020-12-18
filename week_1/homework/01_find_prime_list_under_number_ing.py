input = 20


def find_prime_list_under_number(number):
    under_number_list = list(range(number))[2:]
    multiple_list = []
    for first_num in under_number_list:
        for second_num in under_number_list:
            multiple_num = first_num * second_num
            multiple_list.append(multiple_num)
        for num in under_number_list:
            for compare_num in multiple_list:
                if num == compare_num:
                    under_number_list.remove(num)
    return under_number_list


result = find_prime_list_under_number(input)
print(result)
