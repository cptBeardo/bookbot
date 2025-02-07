def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_count = len(word_list)
        print(f"{word_count} words")
        character_set = set(file_contents.lower())
        # print(character_set)
        character_list = sorted(list(character_set))
        # print(character_list)
        character_dict = {}
        for character in file_contents.lower():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        # print(character_dict)

        alphabet = character_list[-26:]
        print(alphabet)




main()