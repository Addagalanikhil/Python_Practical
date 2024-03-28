marks_python = float(input("Enter the marks in Python: "))
marks_c = float(input("Enter the marks in C Programming: "))
marks_math = float(input("Enter the marks in Mathematics: "))
marks_physics = float(input("Enter the marks in Physics: "))

total_marks = marks_python + marks_c + marks_math + marks_physics
aggregate = total_marks / 4

print("Total =", total_marks)
print("Aggregate =", aggregate)

if aggregate > 75:
    print("Grade: Distinction")
elif 60 <= aggregate < 75:
    print("Grade: First Division")
elif 50 <= aggregate < 60:
    print("Grade: Second Division")
elif 40 <= aggregate < 50:
    print("Grade: Third Division")
else:
    print("Grade: Fail")
