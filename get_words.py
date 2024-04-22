import pandas as pd
import random
import time
import sys

def fetch_vocabulary_as_dataframe(filepath):
    vocabulary = pd.read_excel(filepath, index_col=None)
    vocabulary.loc[:,'Example_Sentence'] = vocabulary.loc[:, 'Example_Sentence'].ffill()
    return vocabulary


def create_flashcard(vocabulary, choice='mcq'):
    ind = random.randint(1, len(vocabulary)-1)
    row = vocabulary.iloc[ind]
    german_word = str(row['German']).replace("\n", "/ ")
    synonyms = row['Synonyms']
    english_meaning = str(row['English']).replace("\n", "/ ")
    example_sentence = row['Example_Sentence']
    example_sentence_translation = row['Example_Sentence_Translation']

    if choice=='german_mcq':
        options = random.sample([i for i in range(1, len(vocabulary)-1) if i != ind], 3)
        english_options = list(vocabulary.loc[options]['English'])
        english_options.append(english_meaning)
        random.shuffle(english_options)

        print(f"What is the meaning of {german_word}?")
        print("Options:")
        for index, option in enumerate(english_options):
            print(f"({index+1}) {option}")

        answer = int(input("Enter correct option (1/2/3/4): "))

        if answer == english_options.index(english_meaning)+1:
            print("That is correct!")
        else:
            print(f"Sorry, you are wrong. The correct answer is {english_meaning}")

    elif choice == 'english_mcq':
        options = random.sample([i for i in range(1, len(vocabulary)-1) if i != ind], 3)
        german_options = list(vocabulary.loc[options]['German'])
        german_options.append(german_word)
        random.shuffle(german_options)

        print(f"What is the German word for {english_meaning}?")
        print("Options:")
        for index, option in enumerate(german_options):
            print(f"({index+1}) {option}")

        answer = int(input("Enter correct option (1/2/3/4): "))

        if answer == german_options.index(german_word)+1:
            print("That is correct!")
        else:
            print(f"Sorry, you are wrong. The correct answer is {german_word}")

    
    print(f"Here is an example sentence - {example_sentence}")
    if not (example_sentence_translation != example_sentence_translation):
        yes_no = input("Would you like to see what it means? (yes/no): ")
        if yes_no == 'yes':
            print(example_sentence_translation)
        else:
            pass
    print("----------------------------------------------------------------------------------------------")


def run_flashcards(vocabulary):
    types = ['german_mcq', 'english_mcq']
    
    while(True):
        try:
            c = random.choice(types)
            create_flashcard(vocabulary, choice=c)
        except KeyboardInterrupt:
            print("\n\n***** THANKS FOR PLAYING! ******")
            sys.exit(0)
        finally:
            time.sleep(2)

if __name__=="__main__":
    filepath = "./Vocabular.xlsx"
    df = fetch_vocabulary_as_dataframe(filepath)
    run_flashcards(df)