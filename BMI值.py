#計算機概論實習作業
#BMI值

weight = int(input("weight(kg):\n"))
height = int(input("height(cm):\n"))

h = float(height/100)

a = weight/(h*h)
print("BMI值= " , a)
