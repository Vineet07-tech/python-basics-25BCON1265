def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    character_count = {}

    for character in first_string:
        character_count[character] = character_count.get(character, 0) + 1

    for character in second_string:
        if character not in character_count:
            return False

        character_count[character] -= 1

        if character_count[character] < 0:
            return False

    return True


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("a", "a"))
