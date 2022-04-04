def change_lower_upper(string):
    new_string = []

    for char in string:
        if char.isupper():
            new_string.append(char.lower())
        elif char.islower():
            new_string.append(char.upper())

    return "".join(new_string)

if __name__ == "__main__":
    string = input()
    print(change_lower_upper(string))
