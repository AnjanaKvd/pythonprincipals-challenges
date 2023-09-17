def online_count(dict):
    count = 0
    for key, value in dict.items():
        if value == "online":
            count += 1
    return count
    