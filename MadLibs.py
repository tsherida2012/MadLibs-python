from random import choice


def Read_File(file):
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
            words_list.remove(n)
    return list


# Download text files of words for madlib
interjections_list = Read_File("interjections.txt")
adjectives_list = Read_File("adjectives.txt")
nouns_list = Read_File("nouns.txt")
verbs_list = Read_File("adverbs.txt")

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
