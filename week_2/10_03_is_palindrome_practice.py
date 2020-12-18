input = "abcba"


def is_palindrome(string):
    for index in range(len(string)):
        compare_index = len(string) - 1 - index
        if string[index] != string[compare_index]:
            return "False"
    return "True"


print(is_palindrome(input))