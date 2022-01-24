from random import choice


def read_file(file):
    """open a file and run a listmaking function on it"""
    with open(file, "r+") as file_handle:
        return make_list(file_handle)


def make_list(file):
    """strips newlines out of file
    and makes a list of words out of the text file
    and cleans up any extra blank lines"""
    word_list = [line.strip() for line in file]
    return delete_spaces(word_list)


def delete_spaces(words_list):
    """Cleans up blank spaces from your list"""
    for line in words_list:
        if line == "":
            words_list.remove(line)
    return words_list


# Download text files of words for madlib
interjections_list = read_file("interjections.txt")
adjectives_list = read_file("adjectives.txt")
nouns_list = read_file("nouns.txt")
verbs_list = read_file("adverbs.txt")

# Pick random words out of word type list to make
# Madlibs sentence
print(
    choice(interjections_list),
    "he said",
    choice(verbs_list),
    "as he jumped into his supersonic",
    choice(nouns_list),
    "and drove off with his",
    choice(adjectives_list),
    "wife",
)
