"""
Date: 25-09-2024
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

# Initialize an array to store scores
scores = []

# Loop to get scores for 5 subjects
for i in range(5):
    score = float(input(f"Please enter the Score for subject {i + 1}: "))
    scores.append(score)

# Calculate the total and average scores
total = sum(scores)
avg = total / len(scores)

# Display total and average scores
print(f"Total Score is {total}")
print(f"Average is {avg}")

# Function to determine the letter grade based on the score
def get_letter_grade(score):
    if score >= 90:
        return 'A+'
    elif score >= 85:
        return 'A'
    elif score >= 80:
        return 'A-'
    elif score >= 79:
        return 'B+'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'B-'
    elif score >= 55:
        return 'C+'
    elif score >= 50:
        return 'C'
    else:
        return 'F'

# Display each subject's score and letter grade
for i, score in enumerate(scores):
    grade = get_letter_grade(score)
    print(f"Subject {i + 1}: Score = {score}, Grade = {grade}")

# Display the average letter grade
average_grade = get_letter_grade(avg)
print(f"Average Grade is {average_grade}")
