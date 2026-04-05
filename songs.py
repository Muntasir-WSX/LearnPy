questions = {
    "What is the name of the song?": "tum ek gorakh banda ho",
    "what is 2+2": "4",
    " Who wrote the song?": "NFAK"
}

score = 0
total_questions = len(questions)
print("Welocome to the quiz! Let's test your knowledge about the song.")
print("Type 'quit' to exit the quiz at any time.\n")

for question, correct_answer in questions.items():
    user_answer = input(question + " ")
    print(user_answer)
    if user_answer.lower() == "quit":
        break
    elif user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect.The correct answer is: {correct_answer}")
        print()
print(f"Your final score is {score} out of {total_questions}.") 