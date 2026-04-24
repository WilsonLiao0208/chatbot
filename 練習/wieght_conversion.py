#python體重轉換器

weight = float(input("請輸入你的體重:"))
unit = input("你的體重是幾公斤還是磅?(kg/lb)").upper()

print(weight)
print(unit)

if unit == 'kg' :
   weight *= 2.2
   new_unit = '磅'
elif unit == 'LB':
   weight /= 2.2
   new_unit = '公斤'
else:
  print("單位不正確")


print(f"你的體重是{round(weight, 2)}{new_unit}")