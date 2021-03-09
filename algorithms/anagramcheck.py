def check_anagram(stra, strb):
    char_counts = {}
    for a in stra:
        if a in char_counts:
            char_counts[a] +=1
        else:
            char_counts[a] = 1

    for a in strb:
        if a in char_counts:
            char_counts[a] -=1
        else:
            return False
    print(char_counts)
    return all(x == 0 for x in char_counts.values())

if __name__ == "__main__":
    print(check_anagram("abdc","dcak"))
