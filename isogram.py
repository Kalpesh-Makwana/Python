def is_isogram(string):
    flag=True
    string=string.replace(" ","").replace("-","").lower()
    for i in string:
        if string.count(i)>1:
            flag=False
            break
    return flag