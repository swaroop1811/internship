def vowel_count(s):
    result = {}
    s = s.lower()

    for v in "aeiou":
        count = 0
        for ch in s:
            if ch == v:
                count += 1
        result[v] = count

    return result


print(vowel_count("Hello World"))