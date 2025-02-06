import pprint 

def count_words(text):
    words = text.split()
    return len(words)

def count_total_letters(text):
    letter_dict = {} 
    words = [word.lower() for word in text.split()] 
     
    for word in words:
        for letter in word:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1 
    letter_dict[" "] = text.count(" ")
    return letter_dict

def print_letter_report(text):
    total_words = count_words(text)
    letter_dict = count_total_letters(text)
    print(f"{3*'-'} Begin report of books/frankenstein.txt {3*'-'} \n")
    print(f"{total_words} words found in the document \n")
    
    for letter, count in letter_dict.items():
        if letter.isalpha():
            print(f"The letter '{letter}' was found {count} times")


    print(f"{3*'-'} End Report {3*'-'} \n")

def main():
    with open("./books/frankenstein.txt", "r") as file:
        text = file.read()
    letters = count_total_letters(text)
    print_letter_report(text)
main()

