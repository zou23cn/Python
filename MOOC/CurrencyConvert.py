CurrStr = input()
if CurrStr[0:3] in ['RMB']:
    U = eval(CurrStr[3:]) / 6.78 
    print("USD{:.2f}".format(U))
elif CurrStr[0:3] in ['USD']:
    R = eval(CurrStr[3:]) * 6.78
    print("RMB{:.2f}".format(R))
else:
    print(CurrStr[0:2])