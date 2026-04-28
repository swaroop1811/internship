def clean_and_list(s):
    result = []
    words = s.split(",")

    for word in words:
        word = word.strip()
        word = word.lower()
        result.append(word)

    return result


print(clean_and_list("apple, banana, cherry"))