def quiz_card(card, attempts=3):
    
    question = card[0]
    answer = card[1]
    
    tries = 0
    while tries < attempts:
        
        user = input(f"{question} ")
        
        if user.strip().lower() == answer.lower():
            
            print("Correct!\n")
            return True
        
        tries = tries + 1
        print("Try Again \n")
        
    print(f"The correct answer is: {answer}\n")
    return False

def main():
    """
    Goes through the flashcard creation process and then quizzes the user on the predefined or user-created flashcards. 
    """
    
    flashcards = [("What is the capital of France?", "Paris"), ("What is 2 + 2?", "4"), ("Name the process plants use to make food.", "Photosynthesis")]
    
    addMore = input("Would you like to create your own flashcard set? ")
    
    if addMore.strip().lower() == "y":
        flashcards = []
        
        while True:
            q = input("Enter a question (leave blank to stop adding questions): ")
            if q.strip() == "":
                break
            a = input("Enter the answer to yourLquestion: ")
            
            flashcards.append((q, a))
            
    
    print("\n---QUIZ YOURSELF---\n")
    score = 0
    
    for card in flashcards:
        if quiz_card(card) == True:
            score = score + 1
            
    total = len(flashcards)
    print(f"Your final score: {score}/{total}!", "thank you for playing")
    
main()