def first_unique_char(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            del char_count[char]  # Remove after finding
            return char

    return None  # No unique character found

print(first_unique_char("swiss")) 