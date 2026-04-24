# input使用者輸入
name = input("請輸入名字:")
print(f"你的名字是{name}")
# 練習一:填詞遊戲
adj_1 = input("請輸入第1個形容詞:")
noun  = input("請輸入名詞:")
adj_2 = input("請輸入第2個形容詞:")
verb  = input("請輸入動詞:")
adj_3 = input("請輸入第3個形容詞:")

print(f"今天我去了一個{adj_1}的動物園,在展覽中我看到了{noun}這個{noun}很{adj_2}正在{verb}我感到很{adj_3}")
# 練習二:計算矩形面積
Length = float(input("請輸入矩形的長度"))
width = float(input("請輸入矩形的寬度"))
#寬與長相乘
area = Length*width
print(f"面積為{area}平方公分")
# 練習三:購物車程
item = input("你想要買什麼物品")
price = float(input("價格多少"))
quantity = int(input("你需要多少件?"))
#價格與數量相乘
total = price*quantity

print(f"你購買了{quantity}{item}總價格${total}")