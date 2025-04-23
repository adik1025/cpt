"""
Flashcard Quiz Program
 - takes user input
 - stores and manipulates data in a list (data abstraction)
 - contains a student-developed procedure with parameters, return value,
   and an algorithm that uses sequencing, selection, and iteration
 - produces textual output based on the input and program logic
"""

def quiz_card(card, attempts=3):
    """
    Presents a flashcard.

    Parameters:
        card (tuple) – (question, answer)
        attempts (int) – tries allowed before revealing answer
    Returns:
        bool – True or False based on correctness
    """
    question, answer = card
    tries = 0                       # --- sequencing
    while tries < attempts:         # --- iteration
        user = input(f"{question} ")       # input
        if user.strip().lower() == answer.lower():   # --- selection
            print("Correct!\n")   # output
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
        flashcards = []  # Remove existing flashcards
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
