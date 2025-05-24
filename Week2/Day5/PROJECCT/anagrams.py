from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker("sowpods.txt")  
    
    while True:
        print("\n=== Anagram Checker ===")
        user_input = input("Enter a word (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if len(user_input.split()) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single word containing only alphabetic characters.")
            continue

        word = user_input.lower()

        if checker.is_valid_word(word):
            print(f'\nYour word: "{word.upper()}"')
            print("This is a valid English word.")
            anagrams = checker.get_anagrams(word)
            if anagrams:
                print("Anagrams for your word: " + ", ".join(anagrams))
            else:
                print("No anagrams found.")
        else:
            print(f'\nYour word: "{word.upper()}"')
            print("This is not a valid English word.")

if __name__ == "__main__":
    main()
