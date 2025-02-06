def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_count = len(word_list)
        print(word_count)

main()