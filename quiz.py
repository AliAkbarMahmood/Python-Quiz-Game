# Python quiz game
questions=('How many elements are there in a periodic table?: ',
           'Which animal lays the largest eggs?: ',
           'Which planet is the hottest in a solar system?: ',
           "What is the abundant gas in the earth's atmosphere?: ",
           "How many bones are there in human body?: ")
options=(('A.116','B.117','C.118','D.119'),
         ('A.Elephant','B.Crocodile','C.Lion','D.Ostrich'),
         ('A.Mercury','B.Venus','C.Earth','D.Mars'),
         ('A.Nitrogen','B.Oxygen','C.Carbon Dioxide','D.Hydrogen'),
         ('A.206','B.207','C.208','D.209'))
answers=('C','D','B','A','A')
score=0
guesses=[]
question_num=0
for q in questions:
    print()
    print(q)
    for o in options[question_num]:
        print(o)
    guess=input('Enter the guess(A,B,C,D):').upper()
    guesses.append(guess)
    if(guess==answers[question_num]):
        score+=1
        print('Correct answer')
    else:
        print('Wrong answer')
        print(f'{answers[question_num]} is the correct answer')
    question_num+=1
print('---------------')
print('-----RESULT----')
print('---------------')
print("Answers:",end='')
for a in answers:
    print(a,end=' ')
print()
print("Your Guesses:",end='')
for g in guesses:
    print(g,end=' ')
print()
score=int(score/len(guesses)*100)
print(f"Your score is {score}%")
