import re
def abbreviate(words):
    acro=re.sub('[-_]'," ",words).split()
    la=""
    for i in acro:
        la+=i[0]
    la=la.upper()
    return la
