def is_palindrome(text):
    cleaned_text = ""

    for character in text:
        if character.isalnum():
            cleaned_text += character.lower()

    return cleaned_text == cleaned_text[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))
