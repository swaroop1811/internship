def palindrome(lst):
    result = []

    for w in lst:
        if w == w[::-1]:
            result.append(w)

    return result


print(palindrome(["madam", "hello", "racecar"]))