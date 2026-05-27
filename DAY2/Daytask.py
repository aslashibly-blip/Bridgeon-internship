marks=[]
print("Enter mark of 10 students:")
for i in range(10):
    marks.append(int(input(f"students{1+1}:")))
print("All marks  : {marks}")
highest=max(marks)
print(f"The highest mark is:",highest)
lowest=min(marks)
print(f"The lowest mark is:",lowest)
average=sum(marks)/len(marks)
print("The average mark is  :",average)
unique_marks=[]
[unique_marks.append(m) for m in marks if m not in unique_marks]
print(f"unique_marks  :{unique_marks}")
above_average=[m for m in unique_marks if m > average]
print(f"Above Average    : {above_average}")