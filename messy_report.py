NUM_SCORES = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def calculate_total(student):
    """Return the sum of a student's numeric scores, skipping the name."""
    total = 0
    for index in range(1, len(student)):
        total = total + student[index]
    return total


def calculate_average(student):
    return calculate_total(student) / NUM_SCORES


def count_above_class_average(student_list):
    """Return how many students have an average above the class average."""
    sum_of_averages = 0
    for student in student_list:
        sum_of_averages = sum_of_averages + calculate_average(student)
    class_average = sum_of_averages / len(student_list)
    count = 0
    for student in student_list:
        if calculate_average(student) > class_average:
            count = count + 1
    return count


print("REPORT")
for student in students:
    total = calculate_total(student)
    average = calculate_average(student)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{student[0]} {total} {average} {grade}")

sum_of_averages = 0
for student in students:
    average = calculate_average(student)
    sum_of_averages = sum_of_averages + average
print(f"Class average: {sum_of_averages / len(students)}")

highest_average = 0
topper_name = ""
for student in students:
    average = calculate_average(student)
    if average > highest_average:
        highest_average = average
        topper_name = student[0]
print(f"Topper: {topper_name} {highest_average}")
