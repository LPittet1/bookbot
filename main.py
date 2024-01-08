def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_textbook(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    let_report = letter_report(num_letters)
    print("Frankenstein book report")
    print(f"{num_words} words in the book")
    for character, count in let_report.items():
        print(f"The '{character}' character was found {count} times in the book.")
    
    print("End of report")


def get_book_textbook(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowercase = text.lower()
    letters = {}
    for letter in lowercase:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def letter_report(num_letters):
    letter_list = list(num_letters)
    letter_list.sort()
    let_list = "".join(letter_list)
    alpha_chars = ""
    for char in let_list:
        if char.isalpha() == True:
            alpha_chars += char
    alpha_list =  list(alpha_chars)
    alpha_dict = {let : num_letters[let] for let in alpha_list}
    return alpha_dict

main()