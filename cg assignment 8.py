# Ask the user to enter marks for three subjects
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (marks1 + marks2 + marks3) / 3

# Determine the grade
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

# Display the grade
print(f"Your average is {average:.2f}, so your grade is {grade}.")