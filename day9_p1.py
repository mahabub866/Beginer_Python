student_scores={
    'harry':81,
    'Ron':79,
    'hermione':99,
    'Darco':74,
    'neville':62
}

student_grades={}
for students in student_scores:
    score=student_scores[students]
    if score>90:
        student_grades[students]='Outstanding'
    elif score>80:
        student_grades[students]='Exceeds Expections'
    elif score>70:
        student_grades[students]='Acceptable'
    else:
        student_grades[students]='Acceptable'

    print(students)

print(student_grades)