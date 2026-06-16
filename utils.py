from colorama import init, Fore, Style

def clear_screen():
    print("\033[H\033[J", end="", flush=True)


def normalise_umlauts(text):
    """Convert umlauts to their non-umlaut equivalents for comparison."""
    replacements = {
        'ä': 'a', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ö': 'O', 'Ü': 'U',
        'ß': 'ss'
    }
    for umlaut, replacement in replacements.items():
        text = text.replace(umlaut, replacement)
    return text


def check_answer(user_answer, correct_answer, display_correct):
    """
    Check if answer is correct, print result, return True/False.
    """
    if user_answer == correct_answer:
        print(f"{Fore.GREEN}That is correct!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}Sorry, you are wrong. The correct answer is {display_correct}{Style.RESET_ALL}")
        return False


def get_valid_input(prompt, valid_options):
    """Keep prompting until user enters a valid option."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_options:
            return answer
        print(f"{Fore.YELLOW}Invalid input. Please enter one of: {', '.join(valid_options)}{Style.RESET_ALL}")


def get_article(word):
    """Extract article from a German noun, returns None if not a noun."""
    word = word.strip().lower()
    if word.startswith("der "):
        return "der"
    elif word.startswith("die "):
        return "die"
    elif word.startswith("das "):
        return "das"
    return None
