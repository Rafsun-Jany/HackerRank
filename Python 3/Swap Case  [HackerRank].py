def swap_case(s):
    new_string = ""
    for letters in s:
        if letters.isupper():
            new_string = new_string + letters.lower()
        else:
            new_string = new_string + letters.upper()
    return new_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
