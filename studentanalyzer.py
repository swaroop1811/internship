def student_analyzer():
    students = {
        "Aarav": 80,
        "Riya": 90,
        "Kiran": 70,
        "Meena": 85
    }

    total = 0

    # find total
    for name in students:
        total = total + students[name]

    avg = total / len(students)

    print("Average Marks:", avg)

    print("Above Average Students:")
    for name in students:
        if students[name] > avg:
            print(name, ":", students[name])


student_analyzer()
