class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(' ','')if card_num else ''

    def valid(self):

        def double_func(num):
            double=num*2
            return double if double < 10 else double - 9

        if len(self.card_num)<2 or not self.card_num.isdigit():
            return False
        else:
            return sum([int(num) if index%2==0 else double_func(int(num)) for index,num in enumerate(reversed(self.card_num))])%10==0
