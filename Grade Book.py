def grade_book(student):

    average_marks = {}

    for name, score in student.items():

        avg = sum(score) / len(score)

        average_marks[name] = round(avg, 2)

    return average_mark   # mistake


students = {
    "Arun": [80, 90, 85],
    "Priya": [70, 75, 78],
    "Rahul": [88, 92, 95]
}

print(grade_book(students))
