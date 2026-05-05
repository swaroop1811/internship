def student_analyzer():
    students = {
        "alice": 80,
        "Riya": 90,
        "Kiran": 70,
        "Meena": 85
    }

    total = 0

  
    for name in marks:
        total = total + students[name]

    avg = total / len(marks)

    print("Average Marks:", avg)

    print("Above Average marks:")
    for name in students:
        if students[name] > avg
            print(marks, ":", students[name])


student_analyzer()
