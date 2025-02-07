def sort_on(dict):
    return dict["num"]
    
def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    character_dict = {}
    for character in file_contents.lower():
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else: 
                character_dict[character] = 1
    return character_dict

def convert_to_sorted_list(character_dict):
    char_list = []
    for char, count in character_dict.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_report(word_count, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents)
    character_dict = count_characters(file_contents)
    char_list = convert_to_sorted_list(character_dict)
    print_report(word_count, char_list)


main()