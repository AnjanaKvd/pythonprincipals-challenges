def double_letters(word):
    for i in range(len(word)):
        print(word[i], word[i-1])
        if word[i] == word[i-1]:
            return True
    return False