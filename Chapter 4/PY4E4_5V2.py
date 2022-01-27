"""Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
4.14. EXERCISES 55
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input."""

#This is my solo attempt at this, having used the first one as an example

#First, I create the function, which will say Bad Score
#if entered outside 0.0 to 0.l

def computegrade(final_score):
    if 0.0 <= final_score <= 1.0:
        if final_score >= 0.9:
            return 'A'
        elif final_score >= 0.8:
            return 'B'
        elif final_score >= 0.7:
            return 'C'
        elif final_score >= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return 'Bad Score'
        
#Then I prompt the user to enter their score
    
user_score = input('Enter score between 0.0 and 1.0: ')

#Then I test to ensure they entered a number

try:
    final_score = float(user_score)
except:
    print('Invalid Entry')
    exit()

#finally, i run the function and print it to the screen
    
grade = computegrade(final_score)
print(grade)
