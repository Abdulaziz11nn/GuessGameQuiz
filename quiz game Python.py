
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
    
questions = {
 "What is the capital City of Kazakhstan?: ": "A",
 "What year was Pytho?: ": "B",
 "What is the capital of Canada?: ": "B",
 "What is the Capital City of Turkey?: ":"C",
 "What is the currency of Poland?: ":"A",
 "which palanet is the biggest?" :"A"
}

options = [["A.Astana", "B.Almata ", "C.Taraz ", "D.Aktay"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A.Vancouver", "B.Toronto ", "C.Ottawa ", "D.Calgary"],
          ["A.Afyon", "b.Isparta", "C.Ankara","D.Bursa"],
          ["A.Zloty","B.Tenge","C.Som","D.BSD"],
          ["A.Jupiter", "B.Mars ", "C.Earth ", "D.Venus"]]
new_game()

while play_again():
    new_game()

print("Byeeeeee!")
