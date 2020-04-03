def find_anagrams(word, persons):
    alpha = ''.join(sorted(word.lower()))
    words = []
    for person in persons:
        if alpha == ''.join(sorted(person.lower())) and word.lower() != person.lower():
            words.append(person)
    return words