#邏輯運算子(運算符)

#and or not

temp = int(input("請輸入現在溫度:"))
if temp > 0 and temp < 30:
   print("溫度是適合的")
else:
   print("溫度是不適宜的")
   
#or
   
if temp<= 0 or temp >= 30:
   print("溫度是不適宜")
else:
   print("溫度適宜")