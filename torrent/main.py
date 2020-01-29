import torrentcharge as tc
if __name__=='__main__':
    options={
            "A":['RGP : Residential Purpose (Up to & Including 15 KW)',tc.Rgp],
            "B":['GLP : For Hospitals, Schools & Religious Purpose',tc.Glp],
            'C':['Non-RGP : Commercial and Industrial Purpose (Up to & Including 15 KW)',tc.Non_Rgp],
            'D':['LTP (AG) : For Agricultural Purpose',tc.Ltp],
            'E':['SL : For Street Light',tc.Street_Light],
            'F':['LEV: LT- Electric Vehicle Charging Stations',tc.Lev_Lt],
            'G':['TMP : For Temporary Supply (Below 100 kW)',tc.Tmp],
        }
    print("---------"*10)
    for option in options:
        print(option+') '+options.get(option)[0])#Display all options to user   

    print("---------"*10)
    choise=input("Please make any choise:") #Getting choise from user
    print("Please Select Proper Choise") if choise not in options.keys() else None
    print("---------"*10)
    val=options.get(choise)  #Giving the user choise value
    if val is not None:
        action=val[1]#giving class name
        action()#calling specific class
    
    