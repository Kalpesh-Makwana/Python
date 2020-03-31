def is_pangram(sentence):
    flag=True
    sentence=sentence.upper()
    for i in range(65,90):
        if chr(i) not in sentence:
            flag=False
    return flag
