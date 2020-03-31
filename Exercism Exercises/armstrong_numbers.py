def is_armstrong_number(number):
    temp=number
    s=0
    d=0
    while temp>0:
        temp//=10
        d+=1 

    temp=number
    while temp>0:
        digit=temp%10
        s+=pow(digit,d)
        temp//=10


    if s==number:
        return True
    else:
        return False
        
