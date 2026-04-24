#python溫賭轉換器
unit = input("請輸入當前的溫度單位(攝氏 C, 華氏 F):")
temp = float(input("請輸入溫度"))

if unit == "C" :
#攝氏轉成華氏
 temp = round(9* temp / 5+32)
 print(f"當前的溫度為{temp}度F")
elif unit == "F":
    temp = round((temp-32)*5/9)
    print(f"當前的溫度為{temp}度C")
else:
   print("非法的溫度單位")