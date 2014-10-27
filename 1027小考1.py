#1027小考1

a = int(input("第一次考試:"))
b = int(input("第二次考試:"))
c = int(input("第三次考試:"))

k = [a, b, c]

x = int(max(a, b, c))
z = int(min(a, b, c))
y = sum(k)-x-z

print("期末分數: ", x*0.5+y*0.3+z*0.2)
