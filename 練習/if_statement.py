#if else elif控制流程

#BooLean布林值
for_sale = False
if for_sale:
    print('此項目正在售出')
else:
    print('此項目未售出')
#if else
age = int(input("請輸入你的年齡:"))
if age >= 18:
    print("你可以註冊")
else:
    print("你必須年滿18歲才能註冊")
#elif => else if的簡寫
age = int(input("請輸入你的年齡:"))
if age >= 100:
    print("你年齡太大,無法註冊") 
elif age >= 19:
    print("你可以註冊")
elif age < 0:
    print("年紀太小,無法註冊")
else:
    print("你必須年滿18歲才能註冊")
#練習

