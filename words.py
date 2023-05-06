def print_upper_words(words):
    """Print every word on a seperate line and completely uppercase
    
        >>> print_upper_words(["Bryce", "Harper", "is", "a", "machine"])
        BRYCE
        HARPER
        IS
        A
        MACHINE
    """

    for word in words:
        print(word.upper())

def print_upper_words_v2(words):
    """Print words on a seperatre line, capitalized, but onlu if starting with letter E or e
    
    >>> print_upper_words_e(["egg", "apple", "Elephant"]):
    EGG
    ELEPHANT
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_v3(words, starting_char):
    """Should retrun every word beginning with a specified letter on its own line and uppercased
    
    >>> print_upper_words_general(["Pineapple","Chicken", "Finland", "baseball"], starting_char={"b", "P"})
        BASEBALL
        PINEAPPLE
    """

    for word in words:
        for letter in starting_char:
            if word.startswith(letter):
                print(word.upper())
                break

            # break here prevents the code from continuing to search after finding the desired word
            #  Terminates innermost loop, searches in the outermost loop