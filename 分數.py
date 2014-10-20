#分數
s1 = int(input("score1:\n"))
s2 = int(input("score2:\n"))
s3 = int(input("score3:\n"))
a = [s1,s2,s3]
x = max(a)
z = min(a)
y = sum(a)-x-z
print("期末成績為:",x*0.5+y*0.3+z*0.2)
