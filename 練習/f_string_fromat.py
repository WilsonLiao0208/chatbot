#f-string的格式化字串
price_1 = 3.321
price_2 = -77
price_3 = 15.11

#小數點的精確度
print(f"價格 1 為{price_1:.2f}\n"
      f"價格 2 為{price_2}\n"
      f"價格 3 為{price_3}\n")

#加上正號或負號
print(f"價格 1 為{price_1:+.2f}\n"
      f"價格 2 為{price_2}\n"
      f"價格 3 為{price_3}\n")

#對齊 < > ^
print(f"價格 1 為{price_1:10.2f}\n"
      f"價格 2 為{price_2}\n"
      f"價格 3 為{price_3}\n")

#混合不同符號
print(f"價格 1 為{price_1:>+.2f}\n"
      f"價格 2 為{price_2}\n"
      f"價格 3 為{price_3}\n")