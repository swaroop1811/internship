def check(users, target):
    result = []
    target = target.lower()

    for u in users:
        if target in u.lower():
            result.append(u)

    return result


print(check(["Alice", "bob", "ALBERT"], "al"))