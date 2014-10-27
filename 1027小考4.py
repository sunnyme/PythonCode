#1027小考4
a = int(input("阿尼斯的分數:\n"))
while True :
    b = int(input("猜的分數:\n"))
    if b > a:
        print("低一點")

    elif b < a:
        print("高一點")
    else:
        print("你猜對了")
        break

        
   
