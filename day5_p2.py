students_height=input('Input a list of student heights: ').split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)
result_sum=sum(students_height)
result_avg=round(result_sum/len(students_height))
print(result_avg)