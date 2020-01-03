def score(word):
    alpha={'AEIOULNRST':1,'DG':2,'BCMP':3,'FHVWY':4,'K':5,'JX':8,'QZ':10}
    word=word.upper()
    cnt=0
    for i in word:
        for j in alpha:
            if i in j:
                cnt+=alpha[j]
                break
    return cnt
