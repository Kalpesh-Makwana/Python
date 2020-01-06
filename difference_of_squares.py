s=0
t=0
def square_of_sum(number):
   s=pow(sum(range(number+1)),2)
   return s
        
def sum_of_squares(number):
    t=sum(pow(i,2) for i in range(number+1)) 
    return t

def difference_of_squares(number):
    s=pow(sum(range(number+1)),2)
    t=sum(pow(i,2) for i in range(number+1))
    return abs(s-t)

