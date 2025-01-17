#Create a TYPING SPEED CALCULATOR that measures the user's typing speed in words per minute (WPM).

import time  #for measuring time intervals
import random  #to select a random text

def calculate_wpm(start_time, end_time, word_count):
    elapsed_time = end_time - start_time  #calculate the time taken in seconds
    return round((word_count / elapsed_time) * 60, 2)  #convert seconds to minutes and calculate WPM

def calculate_accuracy(original_text, user_text):
    original_words = original_text.split()  #split the original text into words
    user_words = user_text.split()  #split the user input into words
    correct_words = sum(1 for o, u in zip(original_words, user_words) if o == u)  #count correct words
    return round((correct_words / len(original_words)) * 100, 2)  #calculate and return accuracy

def main():
    #sample texts for the typing calculation
    sample_texts = [
        "Code is like humor. When you have to explain it, its bad.",
        "Biotechnology is transforming medicine and agriculture.",
        "Research drives innovation and fuels progress.",
        "Life is a journey of learning and discovery."
    ]

    sample_text = random.choice(sample_texts)  #randomly select a sample text
    print("\nTYPING SPEED CALCULATOR")  
    print("Type the text below as fast and flawlessly as you can to challenge your typing skills:\n")
    print(f"\033[1m{sample_text}\033[0m\n")  #display the sample text in bold

    input("Get ready to type! Press Enter to begin your challenge...")  #wait for user to start
    start_time = time.time()  #record the start time
    user_input = input("Ready, set, go! Type the text below: \n")  #prompt user to type the text
    end_time = time.time()  #record the end time

    wpm = calculate_wpm(start_time, end_time, len(sample_text.split()))  #calculate WPM
    accuracy = calculate_accuracy(sample_text, user_input)  #calculate accuracy

    # Display results
    print("\nYour Performance Report:")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")  #Show time taken
    print(f"Words per minute (WPM): {wpm}")  #Show WPM
    print(f"Accuracy: {accuracy}%")  #Show accuracy

    #provide feedback based on WPM
    if wpm < 20:
        print("Feedback: Dont give up! Practice daily to boost your speed.")
    elif wpm < 40:
        print("Feedback: Nice work! You are improving steadily.")
    elif wpm < 60:
        print("Feedback: Good job! You are getting faster.")
    else: 
        print("Feedback: Outstanding speed! You are a typing pro!")

if __name__=="__main__":
    main() #start the program
