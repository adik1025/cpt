"""
Flashcard Study Tool

This program contains:
 - user input
 - stores and manipulates data in a list
 - procedure with parameters, return value, and algorithm that contains sequencing, selection, and iteration
 - Produces textual output based on the input and the program logic
"""

def quiz_card(card, attempts=3):
    """
    Prints a flashcard to the user, and allows them to guess the answer [attempts] times
    
    Returns True if answered correctly, False if answered incorrectly in the allocated attempts
    """
    
    question = card[0]
    answer = card[1]
    
    tries = 0
    while tries < attempts: # Loop until the num of tries is exhausted
        
        user = input(f"{question} ") # Ask user question
        
        if user.strip().lower() == answer.lower(): # Run if answer is correct
            
            print("Correct!\n") # Returns true; exits function
            return True
        
        tries = tries + 1
        print("Try Again \n")
        
    print(f"The correct answer is: {answer}\n") # Gives user the correct answer and exits function
    return False

def main():
    """
    Goes through the flashcard creation process and then quizzes the user on the predefined or user-created flashcards. 
    """
    
    # Preset flashcards, if needed
    flashcards = [("What is the capital of France?", "Paris"), ("What is 2 + 2?", "4"), ("Name the process plants use to make food.", "Photosynthesis")]
    
    addMore = input("Would you like to create your own flashcard set? ")
    
    if addMore.strip().lower() == "y":
        flashcards = []
        
        while True: # Loop that continues until the question is blank
            q = input("Enter a question (leave blank to stop adding questions): ")
            if q.strip() == "":
                break
            a = input("Enter the answer to your question: ")
            
            flashcards.append((q, a)) # Appends tuple containing question and answer to the list of flashcards
            
    
    print("\n---QUIZ YOURSELF---\n")
    score = 0
    
    for card in flashcards: # Loop through the flashcards
        if quiz_card(card) == True: # See if user guesses the correct answer
            score = score + 1 # Increment score
            
    total = len(flashcards)
    print(f"Your final score: {score}/{total}!", "thank you for playing")
    
main()