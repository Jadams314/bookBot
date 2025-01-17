def main():
    path_to_file = "/home/jester/sadBox/bookBot/books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words_array = file_contents.split()
    
    number_of_words = 0

    for item in words_array:
        if isinstance(item, str):
            number_of_words += 1
    
    print(number_of_words)

main()