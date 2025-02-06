def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_count = len(word_list)
        print(f"{word_count} words")
        character_set = set(file_contents.lower())
        # print(character_set)
        character_list = sorted(list(character_set))
        print(character_list)
        character_count = []



main()