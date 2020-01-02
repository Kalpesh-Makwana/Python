def verse(n):
    surprise=''.join([
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ][n::-1])
    if n==0:
        surprise=surprise.replace('and ',"")
    return surprise

def recite(start_verse, end_verse):
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
    return ["On the "+day[n-1]+" day of Christmas my true love gave to me: "+verse(n-1) for n in range(start_verse,end_verse+1)]
    