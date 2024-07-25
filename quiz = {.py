quiz = {
    "question_1": {
        "question": "What is the year the camera was invented?",
        "answer": "1989"

    },
    "question2": {
        "question": "What is the capitol of Spain?",
        "answer": "Madrid"

    },

    "question3": {
      "question": "what does “URL” stand for?" ,
      "answer": "Uniform resource locator"

    },
    "question4": {
        "question": "What identity document is required to travel to different countries around the world?",
        "answer": "Passport"
    },
    "question5": {
        "question": "What actor plays Ken in the 2023 blockbuster movie “Barbie?",
        "answer": "Ryan Gosling"
    },
    "question6": {
        "question": "There's a snake in my boot!” is famously spoken by which famous cartoon character?",
        "answer": "Woody"
    },
    "question7": {
    "question": "What year was the first iPod released?",
    "answer": "2001"
    },
    "question8": {
        "question": "How many pounds are in a ton?",
        "answer": 2000

    }
}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value ["answer"].lower():
        print('Correct')
        score = score + 1
        print("Score: " + score)
    else:
        print("Wrong!")
        print("The answer is: " + value ["answer"])
print("Your score is" + str(score))
