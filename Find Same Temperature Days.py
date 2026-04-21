gujarat = [25, 26.4, 30.0, 40, 41, 32, 35, 35.2, 40.2]
hyderabad = [30, 25, 30, 40, 52, 25, 32, 40.1, 40.1]

count = 0

for i in range(len(gujarat)):
    g = gujarat[i]
    h = hyderabad[i]

    if g == h:
        count += 1
        print("Same temperature on day", i+1)

print("Total same temperature days:", count)