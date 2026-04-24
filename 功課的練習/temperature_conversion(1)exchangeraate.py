#匯率轉換器
unit = input("請輸入目前的貨幣單位 (T 代表台幣, U 代表美元): ")
amount = float(input("請輸入金額: "))

rate = 32.5  # 匯率：1 美元 = 32.5 台幣

if unit == "T":
    usd = round(amount / rate, 2)
    print(f"轉換後的金額為 {usd} 美元")
elif unit == "U":
    twd = round(amount * rate, 2)
    print(f"轉換後的金額為 {twd} 台幣")
else:
    print("無效的貨幣單位")