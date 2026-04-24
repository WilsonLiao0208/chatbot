#python中的while迴圈第三個範例
num = int(input("請輸入1到10之間的數字:"))
while num < 1 or num >10:
    print(f"你輸入的數字{num}是無效的")
    num = int(input("請輸入 1 到 10 之間的數字:"))
print(f"你輸入了{num}")