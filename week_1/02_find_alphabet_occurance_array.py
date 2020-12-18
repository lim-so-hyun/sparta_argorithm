def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for letter in string:
        if not letter.isalpha():
            continue
        new_index=ord(letter)-ord('a')
        alphabet_occurrence_array [new_index] += 1

    return alphabet_occurrence_array

print (find_alphabet_occurrence_array("hello my name is sparta"))
