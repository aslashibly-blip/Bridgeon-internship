def calculate_grade(*marks):
    avg=sum(marks)/len(marks)
    if(avg>=90):
        return "A"
    elif(avg>=80):
        return "B"
    elif(avg>=70):
        return "C"
    else:
        return "D"
    
    return(marks)
print(calculate_grade(98,65,88,77))