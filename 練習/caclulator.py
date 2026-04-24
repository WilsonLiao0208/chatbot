# Python計算機程式

operator = input('請輸入運算時(加法: + ,減法: - ,乘法:*,除法:/)')
num1 = float(input('請輸入一個數字'))
num2 = float(input('請輸入二個數字'))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*' :
    result = num1 * num2
else:
    print("運算符號無效")

print(f"運算結果是{result}")