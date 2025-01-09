"""
Date: 19-09-2024
Author: Namrata Modha
Purpose: WAP that promts the user to enter scores for 5 subjects Your program should display each subject and its letter grade.
The conditions for the letter grade are as follows:

C >= 50
C+ >= 55
B- >= 60
B >= 70
B+ >= 79
A - >= 80
A >= 85
A+ >= 90

In addition to that, your program should calculate the average score for your user.Your program should display all the relevant details as you see fit.


# Promt the user to enter the score for Subjects
#subject1 = float(input("Please enter the score for Subject1: "))
#subject2 = float(input("Please enter the score for Subject2: "))
#subject3 = float(input("Please enter the score for Subject3: "))
#subject4 = float(input("Please enter the score for Subject4: "))
#subject5 = float(input("Please enter the score for Subject5: "))

# Check the grading
if subject1 >= 90:
    print(f"Your score of subject1 is {subject1}: and the grade is A+")
elif subject1 >= 85:
    print(f"Your score of subject1 is {subject1}: and the grade is A")
elif subject1 >= 80:
    print(f"Your score of subject1 is {subject1}: and the grade is A-")
elif subject1 >= 79:
    print(f"Your score of subject1 is {subject1}: and the grade is B+")
elif subject1 >= 70:
    print(f"Your score of subject1 is {subject1}: and the grade is B")
elif subject1 >= 60:
    print(f"Your score of subject1 is {subject1}: and the grade is B-")
elif subject1 >= 55:
    print(f"Your score of subject1 is {subject1}: and the grade is C+")
elif subject1 >= 50:
    print(f"Your score of subject1 is {subject1}: and the grade is C")
else:
    print(f"Your score of subject1 is {subject1}: and the grade is F")
"""

counter = 1
total = 0
while counter < 6:
    score = float(input("Please enter the Score" +str(counter)+ " : "))
    counter += 1
    #print(f"Score: {score}")
    total = total + score

avg = total / (counter -1)

print(f"Total Score is {total}") 
print(f"Average is {avg}")


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


