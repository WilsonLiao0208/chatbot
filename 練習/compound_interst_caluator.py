#複利計算機
#總金額 = 本金*(1+(利率/100))**時間
amount = 0
while amount <= 0:
    amount = float(input("清輸入本金金額"))
    if amount <= 0:
        print("本金金額不能小於或等於零")
    print(amount)
        
        