    # a
def create_permutation(n):
    # import
    from random import randint

    # variables
    possible_ints = [integer for integer in range(n)]
    permutation = []

    # while-loop
    while len(possible_ints) > 0:
        random_index = randint(0,(len(possible_ints) - 1))
        permutation.append(possible_ints.pop(random_index))

    # return
    return permutation


    # b
def scramble_word(word):
    # import
    from random import randint

    # variables
    word = [char for char in word]
    scrambled_word = ""

    # while-loop
    while len(word) > 0:
        random_index = randint(0,((len(word)) - 1))
        scrambled_word += word.pop(random_index)

    # return
    return scrambled_word
