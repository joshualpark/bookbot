def get_book_text(filepath):
    with open(filepath) as f:
        num_of_words = 0
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            num_of_words += 1
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print ("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")


def get_character_stats(filepath):
    with open(filepath) as f:
        character_stats = {}
        file_contents = f.read()
        lowercase = file_contents.lower()
        characters = list(lowercase)
        for character in characters:
            if character in character_stats:
                character_stats[character] += 1
            else:
                character_stats[character] = 1
    return character_stats

def sort_dict(character_stats):
    print ("--------- Character Count -------")
    sort_dict_list = []
    for letter, amount in character_stats.items():
        if letter.isalpha():
            sort_dict_list.append({"letter": letter, "amount": amount})
    def sort_on(dict):
        return dict["amount"]
    
    sort_dict_list.sort(reverse=True, key=sort_on)

    for letter in sort_dict_list:
        print(f"{letter["letter"]}: {letter["amount"]}")