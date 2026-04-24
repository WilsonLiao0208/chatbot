
with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

content_upper = content.upper()

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(content_upper)c

print("转换完成！")
