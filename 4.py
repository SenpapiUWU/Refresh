total_marks = 0
total_students = 0
best_marks = 0
best_students = ""

while True:
    name = input("Enter Your Name:")
    if name == "x":
        break
    else:
        mark= int(input("marks:"))
        if mark > 0 and mark < 100:
            print("W")
        elif mark < 0 or mark > 100:
            print("CAP")

        if mark > best_marks:
            best_marks = mark
            best_students = name

print(f"{best_students} is {best_marks} which is the current best mark")
print(f"The average mark was {total_marks/total_students}")


