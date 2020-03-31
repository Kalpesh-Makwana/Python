def rotate(text, key):
    la=""
    for i in text:
        di=ord(i)+key
        if di>122:
            di=di-26
            la+=chr(di)
        elif i.isupper():
            if di>90:
                di=di-26
                la+=chr(di)
            else:
                la+=chr(di)
        else:
            if i.isalpha():
                la+=chr(di)
            else:
                la+=i
    return la