import pandas as pd
import random
from colorama import Fore, Style
from utils import normalise_umlauts, check_answer, get_valid_input, get_article

def generate_mcq_options(vocabulary, correct_index, column_name, correct_value):
    """Generate 4 shuffled MCQ options with the correct answer included."""
    options = random.sample([i for i in range(1, len(vocabulary)-1) if i != correct_index], 3)
    option_list = list(vocabulary.loc[options][column_name])
    option_list.append(correct_value)
    random.shuffle(option_list)
    return option_list


def create_flashcard(vocabulary, choice='mcq') -> (bool, str):
    ind = random.randint(1, len(vocabulary)-1)
    row = vocabulary.iloc[ind]
    german_word = str(row['German']).replace("\n", "/ ")
    synonyms = row['Synonyms']
    english_meaning = str(row['English']).replace("\n", "/ ")
    example_sentence = row['Example_Sentence']
    example_sentence_translation = row['Example_Sentence_Translation']
    correct_ans = False

    if choice=='german_mcq':
        english_options = generate_mcq_options(vocabulary, ind, 'English', english_meaning)
        print(f"What is the meaning of {german_word}?")
        print("Options:")
        for index, option in enumerate(english_options):
            print(f"({index+1}) {option}")

        answer = get_valid_input("Enter correct option (1/2/3/4): ", ['1', '2', '3', '4'])
        correct_ans = check_answer(answer, str(english_options.index(english_meaning)+1), english_meaning)

    elif choice == 'english_mcq':
        german_options = generate_mcq_options(vocabulary, ind, 'German', german_word)
        print(f"What is the German word for {english_meaning}?")
        print("Options:")
        for index, option in enumerate(german_options):
            print(f"({index+1}) {option}")

        answer = get_valid_input("Enter correct option (1/2/3/4): ", ['1', '2', '3', '4'])
        correct_ans = check_answer(answer, str(german_options.index(german_word)+1), german_word)

    
    elif choice == 'type_answer':
        print(f"Type the German word for: {english_meaning}")
        answer = input("Your answer: ").strip().lower()
        correct_word = german_word.lower()
        
        # Accept answer with or without article
        if answer == correct_word or answer in correct_word.split() or \
           normalise_umlauts(answer) == normalise_umlauts(correct_word) or \
           normalise_umlauts(answer) in [normalise_umlauts(w) for w in correct_word.split()]:

            print(f"{Fore.GREEN}That is correct!{Style.RESET_ALL}")
            correct_ans = True
        else:
            print(f"{Fore.RED}Sorry, you are wrong. The correct answer is '{german_word}'{Style.RESET_ALL}")
            correct_ans = False
    
    elif choice == 'article_quiz':
        article = get_article(german_word)
        if article is None:
            # Not a noun, fall back to german_mcq
            return create_flashcard(vocabulary, choice='german_mcq')
        
        noun_without_article = german_word.split(" ", 1)[1]  # Remove article
        print(f"What is the correct article for '{noun_without_article}'? ({english_meaning})")
        answer = get_valid_input("Enter correct option (der/die/das): ", ['der', 'die', 'das'])
        correct_ans = check_answer(answer, article, f"'{article}'")

    
    if pd.notna(example_sentence):
        print(f"Here is an example sentence - {example_sentence}")
        if pd.notna(example_sentence_translation):
            yes_no = input("Would you like to see what it means? (y/n): ")
            if yes_no.lower() in ['y', 'yes']:
                print(example_sentence_translation)
    print("----------------------------------------------------------------------------------------------")
    return (correct_ans, german_word)