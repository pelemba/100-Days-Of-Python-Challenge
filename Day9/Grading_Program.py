student_score = {
    "Matilda": 81,
    "Cleopatra": 78,
    "Hazel": 99,
    "Hope": 74,
    "Nelly": 62,
}

student_grade = {}

for student in student_score:
    score = student_score[student]
    if score >= 90:
        student_grade[student] = "Outstanding"
    elif score >= 80:
        student_grade[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"
print(student_grade)


