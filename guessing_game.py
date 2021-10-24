# Guessing Game = You should find the correct answer.

questions = {
    "What is the longest river in the world? : " : "A",
    "What are the five colours of the Olympic rings? : " : "C",
    "What is the most famous Mexican beer? : " : "B",
    "Which meat is used in Glamorgan sausages? : " : "D",
    "which is not one of the seven kingdoms in Game of Thrones? : " : "D"
}

options = [["A) River Nile " , "B) River Amazon" , "C) River Parana" , "D) River Yenisei"],
           ["A) Blue, black, orange, pink and yellow " , "B) Blue, grey, green, black and red" ,
            "C) Blue, yellow, black, green and red" , "D) Blue, yellow, green, black and purple"],
           ["A) Miller " , "B) Corona" , "C) Heineken" , "D) Coors"],
           ["A) Potato " , "B) Carrot" , "C) Tomato" , "D) Cheese"],
           ["A) The North " , "B) The Iron Islands" , "C) The Stormlands" , "D) The Rainlands"]]


def guessing_game():
    guess1 = []
    correct_answer = 0
    questions_number = 1
    for key in questions:
        print(key)
        for i in options[questions_number - 1]:
            print(i)
        guesses = input("Your answer(A,B,C, and D) : ")
        guesses = guesses.upper()
        guess1.append(guesses)
        questions_number += 1
        correct_answer += check_answer(questions.get(key), guesses)
    percentage = int((correct_answer / len(questions) * 100))
    print("Your succes percentage is " + str(percentage) + "%" )
    answer1 = input("Do you want to play again? (YES/NO) : ")
    play_again(answer1)



def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def play_again(answer):
    if answer == "yes":
        return guessing_game()
    else:
        print("Okay. Take care of yourself...")


guessing_game()


