"""
Date: 24-09-2024
Author: Namrata Modha
Purpose: WAP that promts the user to enter scores for 5 subjects Your program should display each subject and its letter grade.
The conditions for the letter grade are as follows:

C >= 50
C+ >= 55
B- >= 60
B >= 70
B+ >= 79
A ->= 80
A >= 85
A+ >= 90

Calculate the average score while ensuring loops are used to accomplish your solution.
"""

total = 0

# Loop to get scores for 5 subjects
for i in range(1, 6):
    score = float(input(f"Please enter the Score {i}: "))
    total += score

# Calculate the average score
avg = total / 5

# Display total and average scores
print(f"Total Score is {total}")
print(f"Average is {avg}")

# Determine and display the letter grade based on the average score
if avg >= 90:
    print(f"Your score is {avg}: and the grade is A+")
elif avg >= 85:
    print(f"Your score is {avg}: and the grade is A")
elif avg >= 80:
    print(f"Your score is {avg}: and the grade is A-")
elif avg >= 79:
    print(f"Your score is {avg}: and the grade is B+")
elif avg >= 70:
    print(f"Your score is {avg}: and the grade is B")
elif avg >= 60:
    print(f"Your score is {avg}: and the grade is B-")
elif avg >= 55:
    print(f"Your score is {avg}: and the grade is C+")
elif avg >= 50:
    print(f"Your score is {avg}: and the grade is C")
else:
    print(f"Your score is {avg}: and the grade is F")
