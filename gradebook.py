def grade_book(students):
    average_marks = {}

    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        average_marks[name] = round(avg, 2)

    return average_marks
students = {
    "Arun": [80, 90, 85],
    "Priya": [70, 75, 78],
    "Rahul": [88, 92, 95]
}

print(grade_book(students))
