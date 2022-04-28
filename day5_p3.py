students_score=input('Input a list of student score: ').split()
for n in range(0,len(students_score)):
    students_score[n]=int(students_score[n])
print(students_score)
print(f'highst score: {sum(students_score)}')
