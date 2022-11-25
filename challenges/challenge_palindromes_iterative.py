def is_palindrome_iterative(word):
    if type(word) is not str or word == "":
        return False

    for index in range(len(word)):
        if word[index] != word[len(word) - index - 1]:
            return False

    return True
