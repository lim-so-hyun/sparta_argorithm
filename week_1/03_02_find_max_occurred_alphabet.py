input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    def find_alphabet_occurrence_array(string):
        alphabet_occurrence_array = [0] * 26

        for letter in string:
            if not letter.isalpha():
                continue
            new_index = ord(letter) - ord('a')
            alphabet_occurrence_array[new_index] += 1

    max_occurrence=0
    max_alphabet=0
    for index in range (len(alphabet_occurrence_array))
        print(index)
result=find_max_occurred_alphabet (input)
print (result)
