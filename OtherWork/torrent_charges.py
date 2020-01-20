charges=0
def opt_a(unit):
    def opt_a1():
        if unit in range(0,51):
            charges=unit*320
        elif unit in range(51,151):
            charges=(50*320)+((unit-50)*390)
        else:
            charges=(50*320)+(150*390)+((unit-200)*490)    
        charges=charges/100
        phase=('A) Single Phase','B) Three Phase')
        print(*phase,sep='\n')
        print("========"*10)
        p=input('Make Your Choise: ')
        if p=='A':
            charges+=25 
        elif p=='B':
            charges+=65
        else:
            invalid_data()
        print("========"*10)
        print("Your Charges: %0.2f"%charges)

    def opt_a2():
        if unit in range(0,31):
            charges=unit*150
        elif unit in range(31,51):
            charges=(30*150)+((unit-30)*320)
        elif unit in range(51,151):
            charges=(30*150)+(20*320)+((unit-50)*390)
        else:
            charges=(30*150)+(20*320)+(150*390)+((unit-200)*490)
        charges=charges/100
        print("========"*10)
        print("Your Charges: %0.2f"%charges)


    sub_cat={
                'A':['RGP : Residential General Purpose',opt_a1],
                'B':['BPL : Below Poverty Line',opt_a2]
            }

    for cat in sub_cat:
        print(cat+') '+sub_cat.get(cat)[0])
    print("========"*10)

    s_ch=input("Selecet Your Option: ")

    val1=sub_cat.get(s_ch)

    if val1 is not None:
        t_action=val1[1]
    else:
        t_action=invalid_data
    
    t_action()


    

def opt_b(unit):
        if unit in range(0,201):
            charges=unit*410
        else:
            charges=(200*410)+((unit-200)*480) 
        charges=charges/100
        phase=('A) Single Phase','B) Three Phase')
        print("========"*10)
        print(*phase,sep='\n')
        print("========"*10)
        p=input('Make Your Choise: ')
        if p=='A':
            charges+=30
        elif p=='B':
            charges+=70
        else:
            invalid_data()
        print("========"*10)
        print("Your Charges: %0.2f"%charges)


def opt_c(unit):
    charges=(unit*450)/100
    if unit<=5:
        charges+=70
    elif unit>5 and unit<=15:
        charges+=90
    print("Your Charges: ",charges,"Rs.")
    
def opt_d(unit):print('Your Charges: ',(((unit*330)/100)+((unit*1.34)*10)),'Rs.')##1kWh=1.34bhp-h
def opt_e(unit):print('Your Charges: ',((unit*420)/100),'Rs.')
def opt_f(unit):print('Your Charges: ',(((unit*410)/100)+25),'Rs.')
def opt_g(unit):print('Your Charges: ',(((unit*500)/100)+25),'Rs.')

def invalid_data():
    print("Enter Valid Choise")




if __name__=='__main__':
    options={
                "A":['RGP : Residential Purpose (Up to & Including 15 KW)',opt_a],
                "B":['GLP : For Hospitals, Schools & Religious Purpose',opt_b],
                'C':['Non-RGP : Commercial and Industrial Purpose (Up to & Including 15 KW)',opt_c],
                'D':['LTP (AG) : For Agricultural Purpose',opt_d],
                'E':['SL : For Street Light',opt_e],
                'F':['LEV: LT- Electric Vehicle Charging Stations',opt_f],
                'G':['TMP : For Temporary Supply (Below 100 kW)',opt_g],
            }

    print("========"*10)
    for option in options:
        print(option+') '+options.get(option)[0])
    print("========"*10)
    choise=input("Please make any choise:")
    print("========"*10)
    unit=int(input("Enter Unit: "))
    print("========"*10)
    val=options.get(choise)
    if val is not None:
        action=val[1]
    else:
        action=invalid_data
    action(unit)