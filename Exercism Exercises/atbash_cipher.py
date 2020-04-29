a = 'abcdefghijklmnopqrstuvwxyz'
b = 'zyxwvutsrqponmlkjihgfedcba'
a2b = str.maketrans(a, b, ',.')
b2a = str.maketrans(b, a)

def encode(plain_text):
    encoded = plain_text.lower().translate(a2b).replace(' ', '')
    s = ''
    m, n = divmod(len(encoded), 5)
    for i in range(m):
        s += encoded[i*5:i*5+5] + ' '
    if n:
        s += encoded[-n:]
    return s.strip()


def decode(ciphered_text):
    return ciphered_text.translate(b2a).replace(' ', '')