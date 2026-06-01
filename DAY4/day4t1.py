def average(*marks):
    if len(marks)==0: 
       return ("No mark entered")

    return sum(marks)/len(marks)
print(average(10,30,50,70))
print(average())