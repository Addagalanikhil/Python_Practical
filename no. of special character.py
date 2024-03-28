def count_special_characters(text):
    special_characters = 0
    for char in text:
        if not char.isalnum():
            special_characters += 1
    return special_characters

text = "Hello! How are you ?"
special_char_count = count_special_characters(text)
print("Number of special characters:", special_char_count)
