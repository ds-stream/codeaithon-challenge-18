def reverse_substrings(s):
    words = s.split(" ")
    reversed_words = []
    for word in words:
        reversed_word = ""
        for i in range(len(word) - 1, -1, -1):
            reversed_word += word[i]
        reversed_words.append(reversed_word)
    return reversed_words.join(" ")
