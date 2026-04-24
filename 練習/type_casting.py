#顯示隱示型別轉換
#顯示型別轉換
name = "wilson"
age =21
gpa = 3.3
student = True

student = str(student)
print(student)
print(type(student))

gpa =int(gpa)
print(gpa)
print(type(gpa))


age = float(age)
print(age)
print(type(age))

#隱式類別轉換
x=10
y=2.0
x=x/y
print(x)
print(type(x))

#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(student))