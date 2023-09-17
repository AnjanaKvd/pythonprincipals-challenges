def is_anagram(st1, st2):
    if sorted(st1) == sorted(st2):
        return True
    else:
        return False