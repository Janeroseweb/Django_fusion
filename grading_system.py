continue_program = "yes"
name = input("enter your name")
marks = int(input("enter your marks"))
if marks <0 or marks > 100:
    print("invalid marks! enter marks between 0 and 100")
    exit()

if marks >= 70:
    grade =("A")
elif marks >= 60:
    grade =("B")
elif marks >= 50:
    grade =("C")
elif marks >= 40:
    grade =("D")
else:
    grade =("E")

print("student report")
print("Name:",name)
print("Marks:",marks)
print("Grade:",grade)
print("____________")