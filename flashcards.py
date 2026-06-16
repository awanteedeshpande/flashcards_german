import pandas as pd
import random
import time
import sys
from colorama import init
from utils import clear_screen
from quiz_modes import create_flashcard


def show_welcome():
    print("=" * 60)
    print("       GERMAN VOCABULARY FLASHCARDS")
    print("=" * 60)
    print("\nQuiz modes: MCQ, Type Answer, Article Quiz")
    print("Commands: Press Enter for next question, 'q' to quit")
    print("Tip: If your keyboard does not support umlauts, type without them (e.g., 'uber' for 'über')")
    print("\n" + "=" * 60 + "\n")
    input("Press Enter to start...")


def fetch_vocabulary_as_dataframe(filepath):
    vocabulary = pd.read_excel(filepath, index_col=None)
    return vocabulary


def print_stats(correct, total, wrong_answers):
    print(f"You got {correct} out of {total} correct!")
    if wrong_answers:
        print("Here are the words you got wrong:")
        print(", ".join(wrong_answers))
        print("\n----------------------------------------------------------------------------------------------")


def run_flashcards(vocabulary):
    types = ['german_mcq', 'english_mcq', 'type_answer', 'article_quiz']
    correct = 0
    total = 0
    wrong_answers = []
    
    while(True):
        try:
            clear_screen()
            c = random.choice(types)
            correct_ans, german_word = create_flashcard(vocabulary, choice=c)
            if correct_ans:
                correct += 1
            else:
                wrong_answers.append(german_word)
            total += 1
            cont = input("Press Enter for next question (or 'q' to quit): ")
            if cont.lower() == 'q':
                print("\n***** THANKS FOR PLAYING! ******")
                break
        except KeyboardInterrupt:
            print("\n\n***** THANKS FOR PLAYING! ******")
            print_stats(correct, total, wrong_answers)
            sys.exit(0)
        finally:
            time.sleep(0.5)
    
    print_stats(correct, total, wrong_answers)
    

if __name__=="__main__":
    init()
    filepath = "./Vocabular.xlsx"
    df = fetch_vocabulary_as_dataframe(filepath)
    show_welcome()
    run_flashcards(df)