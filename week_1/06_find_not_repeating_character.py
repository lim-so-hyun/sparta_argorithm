input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array=[0]*26

    for char in string:
        arr_index=ord(char)-ord('a')
        alphabet_occurrence_array [arr_index] += 1

    wanted_occurance=1
    unrepeated_alphabet_index= 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence=alphabet_occurrence_array[index]
        if alphabet_occurrence==wanted_occurance:
            unrepeated_alphabet_index=index
            return chr(unrepeated_alphabet_index+ord('a'))
    return "-"

result = find_not_repeating_character(input)
print(result)