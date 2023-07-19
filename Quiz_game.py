def new_game():
    guesses =[]
    correct_guesses =0
    question_num =1

    for key in questions:
        print('-----------------------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter (A,B,C,D): ').upper()
        guesses.append(guess)
        correct_guesses += check_answers(questions.get(key),guess)
        question_num += 1    
    score(correct_guesses, guesses)

def check_answers(answer,guess):
    if answer == guess:
        print('Correct')
        return 1
    else:
        print('Wrong')
        return 0
    
def score(correct_guesses, guesses):
    print('--------------------------------')

    print ('Selected Answers:  ', end="")
    for i in guesses:
        print(i, end=" ",)
    print()
   
    print ('Correct Answers:  ', end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print(f'your score is {score} %')

def play_again():
    Response = input('Do you want to play the game again ? : YES or NO').upper()
    if Response == 'YES':
        return True
    else:
        return False


questions = {"who created the python": "A", 
             "In which year python was created ": "D",
             "what is the name of new intel processor":"C",
             "In which year AMD was eastablished ?": "B"}

options=[['A.Guido van Rossum', 'B.Bill Gates','C.Tim Cook','D.Andy Jassy'],
         ['A.2001','B.1998','C.1996','D.1991'],
         ['A.i3','B.i5','C.i9','D.Xeon'],
         ['A.1956','B.1969','C.1970','D.1985']]

new_game()

while play_again():
    new_game()
print('----------------------')
print('See you again!!')