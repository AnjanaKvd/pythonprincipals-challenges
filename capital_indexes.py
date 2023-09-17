def capital_indexes(word):
    capitals = []
    for i in range(len(word)):
        if word[i].isupper():
            capitals.append(i)
    return capitals
    
    