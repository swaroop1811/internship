def shuffle(lst):
    result = []

    for w in lst:
        if len(w) < 2:
            result.append(w)
        else:
            new = w[-1] + w[1:-1] + w[0]
            result.append(new)

    return result


print(shuffle(["hello", "hi", "a"]))