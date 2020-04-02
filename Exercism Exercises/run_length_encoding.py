import re

def decode(string):
    output=""
    for same in re.findall(r"(\d*)([a-zA-Z\s])", string):
        if(same[0]!=""): output += int(same[0])*same[1]
        else: output += same[1]
    return output

def encode(string):
    output = ""
    for same in re.findall(r"(.)(\1+)|(.)", string):
        if(same[0]!=""):
            output += str(len(same[0])+len(same[1])) + same[0]
        else: output += same[2]      
    return output