def quiz_card(card, attempts=3):
    question, answer = card
    tries = 0
    while tries < attempts:
        user = input(f"{question} ")
        if user.strip().lower() == answer.lower():
            print("Correct!\n")
            return True
        tries += 1
        if tries < attempts:
            print("Try again.\n")
    print(f"The correct answer is: {answer}\n")
    return False

def main():
    flashcards = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("Name the process plants use to make food.", "Photosynthesis")
    ]

    add_more = input("Would you like to add your own flashcards? (y/n) ")
    if add_more.strip().lower() == "y":
        flashcards = []
        while True:
            q = input("Enter a question (leave blank to stop adding): ")
            if q.strip() == "":
                break
            a = input("Enter the answer: ")
            flashcards.append((q, a))

    print("\n----- QUIZ TIME -----\n")
    score = 0
    for card in flashcards:
        if quiz_card(card):
            score += 1

    total = len(flashcards)
    print(f"Your final score: {score}/{total}")
    print(f"Percentage: {score / total * 100:.1f}%  —  Thanks for playing!")

main()
