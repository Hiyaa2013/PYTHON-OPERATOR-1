print("enter marks obtained in 4 subjects..")
math=int(input("Math: "))
science=int(input("Science: "))
english=int(input("English: "))
history=int(input("History: "))
total_marks=math+science+english+history
print("Sum of all subjects is",total_marks)
percentage=(total_marks/400)*100
print("Percentage Marks: ",percentage)