#BMI轉換器
height = float(input("請輸入身高(公尺)"))
weight = float(input("請輸入體重(公斤)"))

bmi = round(weight / (height**2),1)
print(f"您的BMI為{bmi}")

if bmi <18.5:
    print("體重過輕")
elif bmi <24:
    print("體重正常")
else:
    print("體重過重")