while True:
    questions = [
        ("What is the capital of India?", "delhi"),
        ("Which language are we learning?", "python"),
        ("How many days are in a week?", "7"),
        ("What is 5 + 5?", "10"),
        ("Which planet do we live on?", "earth"),
        ("What is the opposite of hot?", "cold"),
        ("How many months are in a year?", "12"),
        ("Which animal is called the king of the jungle?", "lion"),
        ("What is 10 * 2?", "20"),
        ("Which star gives us light?", "sun")
    ]

    score = 0

    print("\n===== WELCOME TO THE QUIZ GAME =====")

    for question, answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", answer)

    percentage = (score / len(questions)) * 100

    print("\n===== QUIZ RESULT =====")
    print("Your score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 50:
        print("Good job! Keep improving.")
    else:
        print("Keep practising!")

    play_again = input("\nPlay again? (y/n): ").strip().lower()

    if play_again != "y":
        print("Thank you for playing!")
        break
